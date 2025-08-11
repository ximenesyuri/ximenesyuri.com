---
title: CHANGELOG
weight: 1000
---

# About

Here you will find some important changelogs for the library {typed}. For the full list of tags, see [here](https://github.com/ximenesyuri/typed/tags).

```{toc}
```

# v0.1.9: extendable models and  exact models

The possibility of creating a _Model_ or an _ExactModel_ that inherits all components from previously constructed models has been introduced.

```python
from typed import *
from typed.models import Model

Model1 = Model(
    arg1=Str,
    arg2=List(Dict(Int)),
    # ...
)

Model2 = Model(
    argA=Float,
    argB=Union(Null(Dict(Str)), Str)
    # ....
)

Model3 = Model(
    __extends__=[Model1, Model2],
    other_arg=SomeType,
    # ....
)
```

Fully compatible with typed functions.

# v0.1.13: base type factories as functors

In {typed}, there are various type factories, which operate between types to construct new types.

Among these factories are the "base factories," which essentially correspond to implementations as concrete types of annotations from the `typing` library, along with a few more factories.

(example-1)=
> [Example](#example-1).
> 1. from `typing`: `Union`, `List`, `Tuple`, `Dict`, `Set`, ...
> 2. additional: `Prod`, `UProd`, `Null`, ...

Types have a semantics given by a certain class of sets. Among the types, we have typed functions, so we can think of the category `TYPE`, where objects are types and morphisms are typed functions.

In this sense, type factories operate at the level of `TYPE` objects, and it would be natural to try to extend them to functors `F: TYPE -> TYPE`.

In version {typed} v0.1.13, this was done for the base type factories listed above.

This means, for example, that we can now take a function: `f: SomeType -> OtherType` and apply the `List`, `Tuple`, etc. operations to it:

`List(f): List(f.domain) -> List(f.codomain)`.

Furthermore, such a construction is done in a way that compositions are respected:

`List(g*f) == List(g)*List(f)`

Naturally, operations at the function level can be concatenated (just as they were at the type level).

This brings {typed} closer to providing not only a "typed approach" to Python, but also a truly functional approach.

# v0.1.15: type safety for variables

Previously, `typed` was limited to providing factories (and models) to create new types and to check types passed as type hints to `typed functions` calls.

Now, it's also possible to use `typed` to check values assigned to variables.

Instead of:

```python
my_var = some_value
```
use:
```python
my_var = typed(ExpectedType)(some_value)
```

At runtime, the interpreter will check if the variable `my_var` has a value whose type is `ExpectedType`.

# v0.3.0: compatibility with pydantic and dataclasses

It is now possible to transform any class into a model, exact model, or conditional model.

In version {typed} v0.3.0, the decorators `@model`, `@exact`, and `@conditional` were included. These decorators can be applied to any class, collecting its attributes and passing them as arguments to the `Model`, `Exact`, and `Conditional` type factories, respectively.

This, in particular, allows you to transform other types of model constructs (such as `pydantic` models and dataclasses) into models in the `typed` sense.

This also enables better integration with LSPs (type factories are dynamic by nature, while classes are static).

# v0.4.0: inclusion of new model types

The {typed} models system has been completely refactored. It is now possible to create custom model factories from the `ModelFactory` metaclass.

Additionally, new model factories have been introduced:
1.  _Ordered_: Validates data with respect to the ordering of entries.
2.  _Rigid_: Validates data with respect to the exactness and ordering of entries.

The `Conditional` model factory has been removed. It is now possible to pass a `__conditions__` variable to each of the model factories, which defines additional conditions for validation.


# v0.4.1: optional without default value

In {typed}, you can create models by applying the `@model` decorator to a class. If you want an entry to be optional, you simply use the `Optional` type factory, passing the type with a default value:

```python
from typed import SomeType, OtherType
from typed.models import model, Optional

@model
class MyModel:
    x: SomeType
    y: Optional(OtherType, some_value)
```

The vast majority of `typed`'s builtin types (and also those constructed by its type factories) are `nullable`, meaning that a "null object" is defined for them, which can be accessed via the `null` function.

In the new update, if a value is not passed along with a type in the `Optional` function, it attempts to take that value as the null object of the type in question:

```python
Optional(SomeType) = Optional(SomeType, null(SomeType))
```

Naturally, if the type in question is not `nullable`, an error is returned.

# v0.4.2: refactoring function types

One of {typed} premisses is:

> If a type `X` is a subtype of a type `Y`, then every instance of `X` should be an instance of `Y`.

This is not a natural behavior of Python, which completely distinguishes elements of a class from the elements of any of its extensions.

Mathematically, this is not the expected behavior, something we have "fixed" within {typed}'s builtin types and type factories.

To exhibit such behavior, classes need to be constructed from specific metaclasses, in which we specify (within the `__instancecheck__` method) the necessary conditions to validate instantiation.

I noticed that some function types were not exhibiting the desired behavior. They were then refactored, and now there is a natural chain of function types, in which one is not only a subtype of the other but also preserves instantiation:

- `Callable`: general callable entities
- `Builtin`: builtin functions
- `Lambda`: lambda functions
- `Function` (or `FuncType`): user defined functions
- `CompFuncType`: composable functions
- `HintedDomFuncType`: user defined functions that have type hint in domain
- `HintedCodFuncType`: user defined functions that have type hint in codomain
- `HintedFuncType`: user defined functions that have type hint in both domain and codomain
- `TypedDomFuncType`: user defined functions with type hints in domain, which is checked at runtime
- `TypedCodFuncType`: user defined functions with type hints in codomain, which is checked at runtime
- `TypedFuncType`: user defined functions with type hints in domain and codomain, which are checked at runtime
- `BoolFuncType`: user defined typed functions whose codomain is `Bool`

# v0.4.3: introduction of `@optional` decorator

In some cases, we need to build models where all inputs are optional. In the new version of {typed}, a decorator to facilitate the construction of this type of model:

```python
from typed.models import optional

@optional
class MyModel:
    some_var: SomeType
    other_var: OtherType = some_value
    ...
```

The snippet above is equivalent to the following:

```python
from typed.models import model, Optional

@model
class MyModel:
    some_var: Optional(Maybe(SomeType), None)
    other_var: Optional(OtherType, some_value)
    ...
```

Here, `Maybe` is the type factory that receives a type and returns `Union(SomeType, None)`. This means that, by default, `@optional` assumes that if a default value is not provided, then `None` is taken as the default.

Instead of passing `None` as the default, you might want to pass the null object of the type (if it is `nullable`). To do this, simply use the `nullable` variable:

```python
from typed.models import optional

@optional(nullable=True)
class MyModel:
    some_var: SomeType
    other_var: OtherType = some_value
    ...
```

In this case, the snippet above is equivalent to:

```python
from typed.models import model, Optional

@model
class MyModel:
    some_var: Optional(SomeType, null(SomeType))
    other_var: Optional(OtherType, some_value)
    ...
```

# v0.4.4: introduction of model attributes

In {typed} we have several types of models:
1.  _Models_ (the standard type, where the instance must contain at least the defined attributes)
2.  _Exact Models_ (where the instance must contain exactly the defined attributes)
3.  _Ordered Models_ (where the instance must contain at least the defined attributes, but in the order they were defined)
4.  _Rigid Models_ (where the instance must contain exactly the defined attributes, and in the same order they were defined)

There is a type whose instances are models of each of the above classes: `MODEL`, `EXACT`, `ORDERED`, and `RIGID`.

Now, such types come with attributes that allow identifying if a given model belongs to a specific class:

1.  `MyModel.is_model`
2.  `MyModel.is_exact`
3.  `MyModel.is_ordered`
4.  `MyModel.is_rigid`

Attributes that return optional and mandatory attributes have also been added:

1.  `MyModel.attrs`: returns all attributes, with name, type, default value, and whether it is optional or not.
2.  `MyModel.optional_attrs`: returns only the optional attributes.
3.  `MyModel.mandatory_attrs`: returns only the mandatory attributes.
