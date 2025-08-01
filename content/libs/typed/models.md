---
title: models
desc: the models system
weight: 20
---

```{title}
```

# About

This documentation covers the _models system_ of [typed](https://github.com/ximenesyuri/types), which is used specifically to data validation.

```{toc}
```

# Overview

The _models system_ is defined in the `typed.models` module, such that:
1. it provides _model factories_, which are type factories constructing _models_;
2. the difference between the _model factories_ is how data is validated in instances of their _models_;
3. each _model factory_ has a corresponding _model type_, consisting  of all its _models_;
4. the process of creating _models_ is compatible with other sources of data validation structures, as Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) and [pydantic](https://github.com/pydantic/pydantic) `BaseModel`. 


# Model Factories

Recall that in `typed` we have _type factories_, which are functions that return a _type_, hence that take values into the _metatype_ `TYPE` of all types. Recall, yet, that we have a primitive type `Json`.

In a very general perspective, a _model factory_ is a type factory such that:
1. it has only keyword arguments, i.e, its domain in `Dict(TYPE)`;
2. the value of each `kwarg` is a type;
3. the key of each `kwarg` defines an attribute in the returning type; 
4. its returning type is a subtype of `Json`.

In other words, a _type factory_ is a function `ModelFactory: Dict(TYPE) -> TYPE` such that `model = ModelFactory(**kwargs)` is a sutype of `Json`, i.e, such that `issubclass(model, Json)` is `True`, and such that `model.key` is defined for each `key` in `kwargs`.  

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
table 1
```

# Model Validation

A _model_ is precisely a _type_ which is constructed from a _model factory_. In other words, it is an instance `model = ModelFactory(**kwargs)` for some `ModelFactory` listed above, and some `kwargs` in `Dict(TYPE)`.

The difference between the _model factories_ is precisely how their _models_ are validated.
  
More precisely, since the _model factories_ produces subtypes of `Json`, it follows that if `isinstance(, model)` is `True`, then `x` is a `Json` data. Each `key` in `kwargs` corresponds to an attribute of `model`, which, in turn, corresponds to an entry in each instance `x` of `model`. The different flavors of _model factories_ deals, precisely, with the reciprocal question:

> Take a _model factory_ `ModelFactory`. Then, given an object `x` such that `isinstance(x, Json)` is `True`, which conditions `x` need to satisfy such that `isinstance(x, model)` is `True` for `model = ModelFactory(**kwargs)` for some `kwargs` in `Dict(TYPE)`?


# Model Types

Each _model factory_ defines a _type_ whose instances are its _models_:

(table-2)=
```
model factory     models type
--------------------------------------
Model             MODEL
Exact             EXACT
Ordered           ORDERED
Rigid             RIGID
--------------------------------------
table 2
```

So, `isinstance(x, MODEL)` is `True` iff `isinstance(x, TYPE)` is `True`, and `x = Model(**kwargs)` for some dictionary `kwargs` of type `Dict(TYPE)`. Analogously for the other _model factories_ and _model types_. 

# Defining Models

Let `ModelFactory` be a generic _model factory_, i.e, some of that in [table 1](#table-1).


# Model

You can create `type models` which are subclasses of the base `Json` class and can be used to quickly validate data, much as you can do with `BaseModel` in [pydantic](https://github.com/pydantic/pydantic), but following the `typed` philosophy:

```python
from typed        import Int, Str, List
from typed.models import Model

SomeModel = Model(
    x=Str,
    y=Int,
    z=List(Int, Str)
)

json = {
    'x': 'foo',
    'y': 'bar',
    'z': [1, 'foobar']
}
```

With the above, `isinstance(json, SomeModel)` returns `False`, since `y` is expected to be an integer. As a consequence, if you use that in a `typed function`, this will raise a `TypeError`, as follows:

```python
from typed import typed, SomeType
from some.where import SomeModel

@typed
def some_function(some_json: SomeModel) -> SomeType:
    ...

json = {
    'x': 'foo',
    'y': 'bar',
    'z': [1, 'foobar']
}

some_function(json) # a raise descriptive TypeError
```



### Validation

You can validade a model entity before calling it in a typed function using the `Instance` checker:

```python
from typed        import typed, Int, Str, List
from typed.models import Model, Instance

Model1 = Model(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json1 = {
    'arg1': 'foo',
    'arg2': 'bar',
    'arg3': [1, 'foobar']
}

model1_instance = Instance(
    model=Model1,
    entity=json1
)
```

> Such a validation is better than using just `isinstance(entity, model)` because it parses the `entity` and provides specific errors, while `isinstance` just return a boolean value.

Another way to validate an instance is to call it directly as an argument for some `model`:
```python
model1_instance = Model1({
    'arg1': 'foo',
    'arg2': 'bar',
    'arg3': [1, 'foobar']
})
```

You can also use a `kwargs` approach:

```python
model1_instance = Model1({
    arg1='foo',
    arg2='bar',
    arg3=[1, 'foobar']
})
```

> Notice that you can also use the above approaches to **create** valid instances and not only to validate **already existing** instances.


### Exact Models

In [pydantic](https://github.com/pydantic/pydantic), a model created from `BaseModel` do a strict validation: a json data is considered an instance of the model iff it exactly matches the non-optional entries.  In `typed` , the `Model` factory creates subtypes of `Json`, so that a typical type checking will only evaluate if a json data **contains** the data defined in the model obtained from `Model`. So, for example, the following will not raise a `TypeError`:

```python
from typed        import typed, Int, Str, List
from typed.models import Model, Instance

Model1 = Model(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json2 = {
    'arg1': 'foo',
    'arg2': 2,
    'arg3': [1, 'foobar']
    'arg4': 'bar'
}

model1_instance = Instance(
    model=Model1,
    entity=json2
)
```

For an exact evaluation, as occurs while using `BaseModel`, you could use the `Exact` factory from `typed.models`. It also provides a `Optional` directive, as in [pydantic](https://github.com/pydantic/pydantic):

```python
from typed        import typed, Int, Str, List
from typed.models import ExactModel, Instance

Model1 = ExactModel(
    arg1=Str,
    arg2=Optional(Int, 0),  # optional entries always expect a default value
    arg3=List(Int, Str)
)

Model2 = ExactModel(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json1 = {
    'arg1': 'foo',
    'arg3': [1, 'foobar']
}

json2 = {
    'arg1': 'foo',
    'arg2': 2,
    'arg3': [1, 'foobar']
}

# will NOT raise a TypeError
model1_instance = Instance(
    model=Model1,
    entity=json1
)

# will NOT raise a TypeError
model2_instance = Instance(
    model=Model2,
    entity=json2
)

# WILL raise a TypeError
model2_instance = Instance(
    model=Model2,
    entity=json1
)
```

# Other Docs

```{toc-dir}
``` 
