---
title: models
desc: the models system
weight: 20
---

```{title}
```

# About

This documentation covers the _models system_ of {typed} which is used specifically to data validation.

```{toc}
```

# Overview

The _models system_ is defined in the `typed.models` module, such that:

1. it provides _model factories_, which are type factories constructing _models_;
2. the difference between the kinds of _model factories_ is how data is validated in instances of their _models_;
3. each _model factory_ has a corresponding _model type_, consisting  of all its _models_;
4. the process of creating _models_ is compatible with other sources of data validation structures, as Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) and [pydantic](https://github.com/pydantic/pydantic) `BaseModel`. 

# Model Factories

Recall that in {typed} we have _type factories_, which are functions that return a _type_, hence that take values into the _metatype_ `TYPE` of all types. Recall, yet, that we have a primitive type `Json`.

In a very general perspective, a _model factory_ is a _type factory_ such that:
1. it has only keyword arguments;
2. the value of each `kwarg` is a type;
3. the key of each `kwarg` defines an attribute in the returning type; 
4. its returning type is a subtype of `Json`.

In other words, a _type factory_ is a function `ModelFactory: Dict(TYPE) -> TYPE` such that:
1. `model = ModelFactory(**kwargs)` is a subtype of `Json`
2. `model.key` is defined for each `key` in `kwargs`.  

We have the following _model factories_:

(table-1)=
```
model factory    description
-----------------------------------------------
Model            the factory of _basic_ modes
Exact            the factory of _strict_ models
Ordered          the factory of _ordered_ models
Rigid            the factory of _rigid_ models
-----------------------------------------------
table 1: model factories
```

# Validation Conditions

In {typed}, a _model_ is precisely a _type_ which is constructed from a _model factory_. In other words, it is an instance `model = ModelFactory(**kwargs)` for some `ModelFactory` listed above, and some `kwargs` in `Dict(TYPE)`.

The difference between the _model factories_ is precisely how their _models_ are validated.
  
More precisely, since the _model factories_ produces subtypes of `Json`, it follows that if `isinstance(x, model)` is `True`, then `x` is a `Json` data. Each `key` in `kwargs` corresponds to an attribute of `model`, which, in turn, corresponds to an entry in each instance `x` of `model`, when viewed as a `Json` datas. The different flavors of _model factories_ deals, precisely, with the reciprocal question:

> Take a _model factory_ `ModelFactory`. Then, given an object `x` such that `isinstance(x, Json)` is `True`, which conditions `x` should satisfy such that `isinstance(x, model)` is `True` for `model = ModelFactory(**kwargs)` for some `kwargs` in `Dict(TYPE)`?

The answers for each question are in the following table:

(table-2)=
```
model factory        validation condition 
--------------------------------------------------------------------------
Model                the json data contains at least the defined attributes
Exact                the json data contains precisely the defined attributes
Ordered              the json data contains at least the defined attributes, but in the same ordering
Rigid                the json data contains precisely the defined attributes, and in the same ordering
----------------------------------------------------------------------------
table 2: validation conditions
```

# Model Types

Each _model factory_ defines a _type_ whose instances are its _models_:

(table-3)=
```
model factory     models type
--------------------------------------
Model             MODEL
Exact             EXACT
Ordered           ORDERED
Rigid             RIGID
--------------------------------------
table 3:  model types
```

So, `isinstance(x, MODEL)` is `True` iff `isinstance(x, TYPE)` is `True`, and `x = Model(**kwargs)` for some dictionary `kwargs` of type `Dict(TYPE)`. Analogously for the other _model factories_ and _model types_. 

# Defining Models

Let `ModelFactory` be a generic _model factory_, i.e, some of that in [table 1](#table-1). The typical way to define a model for it, is as follows:

```python
from typed import SomeType, OtherType, ...
from typed.models import ModelFactory

MyModel = ModelFactory(
    some_attr: SomeType,
    other_attr: OtherType,
    ...
)
```

So, for example, we define an instance of the _model type_ `MODEL` as below (and Analogously for the other _model factories_ and _model types_):

```python
from typed import SomeType, OtherType, ...
from typed.models import Model

MyModel = Model(
    some_attr: SomeType,
    other_attr: OtherType,
    ...
)

print(isinstance(MyModel, MODEL)) # returns True
```

# Decorators

There is another way to define models, which is using the _model decorators_. Indeed, to each _model factory_ there corresponds a namesake decorator, named in lowercase:

(table-4)=
```
model factor         decorator
---------------------------------
Model                @model
Exact                @exact
Ordered              @ordered
Rigid                @rigid
-------------------------------
table 4: model decorators
```

The decorators can be applied to any class. This will generate a model of the corresponding _model type_, based on the attributes of the given class. This can be used to quickly create models, as follows (same for other _model types_ by making use of other _model decorators_):

```python
from typed import SomeType, OtherType, ...
from typed.models import model

@model
class MyModel:
    some_attr: SomeType
    other_attr: OtherType
    ...
```

> This approach can also be used to convert models from other sources into {typed} models. In particular, this can be used to generate {typed} models from [pydantic](https://github.com/pydantic/pydantic) models and from Python [dataclasses](https://docs.python.org/3/library/dataclasses.html).

> The approach of creating {typed} models from _model decorators_ is recommended. Indeed, while created directly from a _model factory_, the model a fully dynamically entity. This means that a LSP will not collect its attributes. On the other hand, while using the _model decorators_, they are applied to static classes, whose attributes are recognized by LSPs, providing a better developing experience.

# Universal Decorator

Actually, one can use `@model` as an "universal decorator", in the sense that one can reconstruct the behavior of the other _model decorators_ from it. Indeed, `@model` contains boolean variables, as below, which, when set, introduce the corresponding decorator in the model construction.

(table-5)=
```
variable        model decorator
--------------------------------
exact           @exact
ordered         @ordered
rigid           @rigid
-----------------------------
table 5: variables in @model
```

For example, one could create an _exact model_ as follows:

```python
from typed import SomeType, OtherType, ...
from typed.models import model

@model(exact=True)
def MyModel:
    some_attr: SomeType
    other_attr: OtherType
    ...

print(isinstance(MyModel, EXACT)) # prints True
```

# Data Validation

One time defined a model, one can use it to:

1. validate existing `Json` data;
2. create already validated `Json` data.

Indeed, suppose we have a given `json_data`. The validation can be realized by calling the model with the given `Json` data:

```python

json_data = {
    "some_attr": some_value,
    "other_attr": other_value
    ...
}

validated_data = MyModel(**json_data)
```

Another way of validating a predefined `json_data` is through the `Validate` function:

```python
from typed.models import Validate

validated_data = Validate(
    model=MyModel,
    data=json_data
)
```

The simplest way to _create_ validated data is to call the model with specified `kwargs`:

```python
validated_data = MyModel(
    some_attr=some_value,
    other_attr=other_value,
    ...
)
```

Independently of the case, if some condition used in the definition of the model `MyModel` is not satisfied, a `TypeError` will be raised.

> For more on the {typed} error messages, see [errors](./errors).

# Optional Attributes

In the moment of the definition of a model, one can determine certain attributes as _optional_. If the model is defined from a _model factory_, this can be done my making use of the `Optional: TYPE x Any -> TYPE` directive, which receives an attribute and a default value:

```python
from typed import SomeType, OtherType, OptType
from typed.models import ModelFactory, Optional

MyModel = ModelFactory(
    some_attr=SomeType,
    other_attr=OtherValue,
    opt_atrr=Optional(OptType, default_value),
    ...
)
```

Then, in the validation of some `json_data` through the model `MyModel`, if there is no entry named `opt_attr`, the validated data will be appended with such entry with value given by `default_value`.

The directive `Optional` also accept to do not pass a default value, i.e, it accepts a single argument `Optional(OptType)`. In this case:
1. First it will be checked if passed type `OptType` is `nullable`. In this case, `Optional(OptType)` will return `Optional(OptType, null(OptType))`, i.e, the null object of `OptType` will be set as the default argument.
2. If `OptType` is not `nullable`, it will be checked if it can be initialized. In this case, `Optional(OptType)` will return `Optional(OptType, OptType())`.
3. Finally, if not of the above conditions are satisfied, then `None` will be set as the default value. More precisely, `Optional(OptType)` will return `Optional(Maybe(OptType), None)`.

In the definition of a model from a _model decorator_, an optional attribute can be defined by just setting a default value, or by making use of the `Optional` directive:

```python
from typed import SomeType, OtherType, OptType
from tped.models import model, Optional

@model
class MyModel:
    some_attr: SomeType
    other_attr: OtherType
    opt_attr: OptType=default_value
    ...

@model
class MyModel:
    some_attr: SomeType
    other_attr: OtherType
    opt_attr: Optional(OptType, default_value)
    ...
```

The difference, here, is that you can customize the behavior of passing a single argument to `Optional` through the variable `nullable`. Indeed, if `nullable=False` in the _model decorator_, then `Optional(OptType)` will return `Optional(Maybe(OptType), None)` directly, without checking for nullability conditions for `OptType`.

# Optional Decorator

Some times you want to define a model such that every attribute is optional. These are the so-called _optional models_ and define a type `OPTIONAL`. You can quickly create an optional model by making use of the `@optional` decorator:

```python
from typed import SomeType, OtherType
from typed.models import optional

@optional
class MyModel:
    some_attr: SomeType
    other_attr: OtherType=default_value
    ...

print(isinstance(MyModel, OPTIONAL)) # returns True
```

The above is equivalent to:

```python
from typed import SomeType, OtherType
from typed.models import model, Optional

@model
class MyModel:
    some_attr: Optional(SomeType)
    other_attr: Optional(OtherType, default_value)
    ...
```

> While using `@optional`, you can control the behavior of the single argument case of `Optional` by making use of the variable `nullable`. In other words, `@optional(nullable=False)` implements the above, but with `@model(nullable=False)`.

You can also use `optional` not to _define_ an optional model, but to turn an _already existing_ model into an optional model:

```python
from typed import optional
from some.where import MyModel

OptionalModel = optional(MyModel, nullable=False).

print(isinstance(MyModel, OPTIONAL)) # returns True
```

> The decorator `@optional` preserves the _model type_. Indeed, if `isinstance(MyModel, EXACT)` is `True`, then `isinstance(optional(MyModel), EXACT)` is `True` as well, and similarly for the other model types.

# Mandatory Attributes

If an attribute in a model is not optional, it is _mandatory_. A model in which every attribute is mandatory is a _mandatory model_, which constitute a type `MANDATORY`.

Analogously to the optional case, there is a decorator `@mandatory`. If used in the creation of a model, it ignores any introduction of the `Optional` directive or any default value:

```python
from typed import SomeType, OtherType, AnotherType
from typed.models import mandatory

@mandatory
class MyModel:
    some_attr: SomeType
    other_attr: OtherType=default_value
    another_attr: Optional(AnotherType)
    ...

print(isinstance(MyModel, MANDATORY)) # returns True
```

The above is equivalent to:

```python
from typed import SomeType, OtherType
from typed.models import model

@model
class MyModel:
    some_attr: SomeType
    other_attr: OtherType
    another_attr: AnotherType
    ...
```

The function `@mandatory` can also be used to turn any already existing model into a mandatory model preserving its _model type_:

```python
from typed import mandatory
from some.where import MyModel

OptionalModel = mandatory(MyModel).

print(isinstance(MyModel, MANDATORY)) # returns True
```

In the above, if `isinstance(MyModel, EXACT)` is `True`, then `isinstance(optional(MyModel), EXACT)` is `True` as well, and similarly for the other model types.

# Model Extension

A model can be created _extending_ other models. This ensures that the new model have at least the attributes that are defined in the model is extended. This is the _inheritance_ behavior of models.

While defining a new model from a _model factory_, the models that are being extended can be listed in a `__extends__` variable in the factory:

```python
from typed import SomeType, OtherType, ...
from typed.models import ModelFactory
from some.where import SomeModel, OtherModel, ...

MyModel = ModelFactory(
    __extends__=[SomeModel, OtherModel, ...],
    some_attr=SomeType,
    other_attr=OtherType,
    ...
)
```

In the case of using _model decorators_, the extended models are passed in the variable `extends` (in the example below, the same works for other model decorators):

```python
from typed import SomeType, OtherType, ...
from typed.models import model
from some.where import SomeModel, OtherModel, ...

@model(extends=[SomeModel, OtherModel, ...])
class MyModel:
    some_attr=SomeType,
    other_attr=OtherType,
    ...
```

> The variables `__extends__` and `extends` accept not only `List(MODEL)` type, but also other iterative types based on some model type, as  `Tuple(MODEL)`, `Set(MODEL)` or even just `MODEL` if a single model will be extended.

# Filtering Models


# Model Attributes

The _model types_ `MODEL`, `EXACT`, and so on, have certain properties, which define corresponding attributes to their models: the so-called _model attributes_. They are described below:

(table-6)=
```
attribute           meaning 
---------------------------------------------
.is_model           True for MODEL instances 
.is_exact           True for EXACT instances
.is_ordered         True for ORDERED instances
.is_rigid           True for RIGID instances
.attrs              dict of all attributes
.optional_attrs     dict of optional attributes
.mandatory_attrs    dict of mandatory attributes
-----------------------------
table 6: model attributes
```

> `setattr`, `hasattr` and `getattr` applies to models. All of that and `delattr` applies to instances of models.

# Model Operations

... TBA ...


# Other Docs

```{toc-dir}
``` 
