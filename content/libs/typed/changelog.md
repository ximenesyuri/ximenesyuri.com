---
title: changelog
weight: 1000
---

# About

Here you will find some important changelogs for the library {lib:typed}. For the full list of tags, see [here](https://github.com/ximenesyuri/typed/tags).

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

In {lib:typed}, there are various type factories, which operate between types to construct new types.

Among these factories are the "base factories," which essentially correspond to implementations as concrete types of annotations from the `typing` library, along with a few more factories.

(example-1)=
> [Example](#example-1).
> 1. from `typing`: `Union`, `List`, `Tuple`, `Dict`, `Set`, ...
> 2. additionalib: `Prod`, `UProd`, `Null`, ...

Types have a semantics given by a certain class of sets. Among the types, we have typed functions, so we can think of the category `TYPE`, where objects are types and morphisms are typed functions.

In this sense, type factories operate at the level of `TYPE` objects, and it would be natural to try to extend them to functors `F: TYPE -> TYPE`.

In version {lib:typed} v0.1.13, this was done for the base type factories listed above.

This means, for example, that we can now take a function: `f: SomeType -> OtherType` and apply the `List`, `Tuple`, etc. operations to it:

`List(f): List(f.domain) -> List(f.codomain)`.

Furthermore, such a construction is done in a way that compositions are respected:

`List(g*f) == List(g)*List(f)`

Naturally, operations at the function level can be concatenated (just as they were at the type level).

This brings {lib:typed} closer to providing not only a "typed approach" to Python, but also a truly functional approach.

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

In version {lib:typed} v0.3.0, the decorators `@model`, `@exact`, and `@conditional` were included. These decorators can be applied to any class, collecting its attributes and passing them as arguments to the `Model`, `Exact`, and `Conditional` type factories, respectively.

This, in particular, allows you to transform other types of model constructs (such as `pydantic` models and dataclasses) into models in the `typed` sense.

This also enables better integration with LSPs (type factories are dynamic by nature, while classes are static).

# v0.4.0: inclusion of new model types

The {lib:typed} models system has been completely refactored. It is now possible to create custom model factories from the `ModelFactory` metaclass.

Additionally, new model factories have been introduced:
1.  _Ordered_: Validates data with respect to the ordering of entries.
2.  _Rigid_: Validates data with respect to the exactness and ordering of entries.

The `Conditional` model factory has been removed. It is now possible to pass a `__conditions__` variable to each of the model factories, which defines additional conditions for validation.


# v0.4.1: optional without default value

In {lib:typed}, you can create models by applying the `@model` decorator to a class. If you want an entry to be optional, you simply use the `Optional` type factory, passing the type with a default value:

```python
from typed import SomeType, OtherType
from typed.models import model, Optional

@model
class MyModelib:
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

One of {lib:typed} premisses is:

> If a type `X` is a subtype of a type `Y`, then every instance of `X` should be an instance of `Y`.

This is not a natural behavior of Python, which completely distinguishes elements of a class from the elements of any of its extensions.

Mathematically, this is not the expected behavior, something we have "fixed" within {lib:typed}'s builtin types and type factories.

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

In some cases, we need to build models where all inputs are optional. In the new version of {lib:typed}, a decorator to facilitate the construction of this type of modelib:

```python
from typed.models import optional

@optional
class MyModelib:
    some_var: SomeType
    other_var: OtherType = some_value
    ...
```

The snippet above is equivalent to the following:

```python
from typed.models import model, Optional

@model
class MyModelib:
    some_var: Optional(Maybe(SomeType), None)
    other_var: Optional(OtherType, some_value)
    ...
```

Here, `Maybe` is the type factory that receives a type and returns `Union(SomeType, None)`. This means that, by default, `@optional` assumes that if a default value is not provided, then `None` is taken as the default.

Instead of passing `None` as the default, you might want to pass the null object of the type (if it is `nullable`). To do this, simply use the `nullable` variable:

```python
from typed.models import optional

@optional(nullable=True)
class MyModelib:
    some_var: SomeType
    other_var: OtherType = some_value
    ...
```

In this case, the snippet above is equivalent to:

```python
from typed.models import model, Optional

@model
class MyModelib:
    some_var: Optional(SomeType, null(SomeType))
    other_var: Optional(OtherType, some_value)
    ...
```

# v0.4.4: introduction of model attributes

In {lib:typed} we have several types of models:
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

# v0.4.5: optional and mandatory models

In v0.4.3 it was introduced the `@optional` decorator, from which one can to quickly create _optional models_, which are models whose all attributes are optional.

In this new version, a type `OPTIONAL` of all  _optional models_ was created. Also, the `@optional` decorator was extended to be applied directory in already existing models, turning them into optional models.

Analogously, it was introduced the type `MANDATORY` of all _mandatory models_, i.e, models with none optional arguments. A decorator `@mandatory` was created, allowed to turn any model into a mandatory model.

> If applied in already existing models, both `@optional` and `@mandatory` preserves the underlying model kind, i.e, exact models are mapped into exact models, and so on.

# v0.5.0: refactor of factories

In v0.5.0 all factories were reviewed:
1. error messages are now more descriptive
2. unification of function types with function factories
3. `BoolFunc` has now the name `Condition`

So, for example:
1. `CompType` is now `Composable` which can be applied to both a function or to a pair of integers
2. `TypedFuncType` and `TypedFunc` are now just `Typed`, which can be applied to functions, types or pair of integers:
3. and so on

```python
from typed import Typed, SomeType, OtherType
from some.where import some_function

Typed # the same as the old TypedFuncType
Typed(SomeType, cod=OtherType) # the same as the old TypedFunc(SomeType, cod=OtherType)
Typed(some_function) # the same as the old TypedFunc(some_function)
...
```

# v0.5.1: introduce `__null__` in factories

In {lib:typed} we have _nullable_ types. These are the types for which the `null` function is defined. In v0.5.1 the `null` function was revisited to look for two cases:
1. predefined builtin nullable types
2. types with a `__null__` defined.

Also, all factories were reviewed to include a `__null__` attribute to the type they construct.

# v0.5.2: review the basic types

In {lib:typed}, a {lib:type} is suppose to be constructed from an {lib:inner metatype}. Previously we have applied this definition to all _constructed_ types, meaning that they are not Python _builtin types_. So, for example, previously:

(table-1)=
```
typed type          definition 
------------------------------
Str                 str
Bool                bool
Int                 int
Float               float
TYPE                type
Nill                type(None)
------------------------------
table 1
```

In version v0.5.2 these types are now {lib:typed types}, so that are constructed from {lib:inner metatypes}.

# v0.5.3: symmetrization of basic factories

Some {lib:factories} are supposed to be _symmetric_ in the sense that they should not depend on the ordering of their arguments. Examples include:
1. `Union`
2. `Inter`
3. `Tuple`
4. `List`
5. `Set`
6. `Dict`

Previously such factories were __not__ symmetric. In version v0.5.3 they were made symmetric.

# v0.6.0: reorganize structure and imports

Previously the code entries were centered in a `main.py` file which imported everything from the feature files using a `from typed.mods... import *`. The main advantage of this dynamic approach is being stable under changes in the feature files, as the addition or deletion of new {lib:types}, {lib:factories}, {lib:models}, and so on. 

However, it has some disadvantages: 
1. it requires a more complex dependencies resolution
2. it exposes to the user an API with internal functions

In v0.6.0 the code were revisited and the imports were made static. Now we have three main modules: 

(table-2)=
```
module             description 
------------------------------------
typed.types        expose all types
typed.factories    expose all factories
typed.models       expose all models
------------------------------------
table 2: new API modules
```

The use of these modules provide a better LSP experience to the user. The basic decorators `@typed` and `@factory` should be imported directly from `typed`.  Alternatively, it can still import anything directly from `typed`. Indeed, the main entry point `__init__.py` of {lib:typed} imports everything from the above modules:

```python
from typed.mods.decorators import typed, factory
from typed.types     import *
from typed.factories import *
from typed.models    import *
```

# v0.7.0: introduction of dependent types

Recall that a _dependent type_ is some type which depends on the value of its underlying term. They make the type system much more expressive and are fundamental to ensure genuine type safety.

In {lib:typed} version v0.7.0 an implementation of {lib:dependent types} was introduced. They are {lib:type factories} with a `.is_dependent_type` boolean attribute set to `True`. They can be passed as annotations to {lib:typed functions}. In this case, the arguments of the {lib:dependent type} should be {py:parameters} of the {lib:typed function}. In this sense, the type of the parameter with annotation given by the {lib:dependent type} depends on the value of the {py:parameters} from which the {lib:dependent type} depends on.

Dependent types are defined through the decorator `@dependent` and constitute a {lib:type} `Dependent`, which is a {lib:subtype} of `Factory`, which in turn is a {lib:subtype} of `Typed`.

```python
from typed import dependent, TYPE, SomeType, OtherType, ..., ReturnType

@dependent
def DepType(x: SomeType, ...) -> TYPE:
    ...

@typed
def some_function(x: SomeType, y: DepType, ...) -> ReturnType:
    ...
```
