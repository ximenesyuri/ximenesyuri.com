---
title: types
---

# About

In this documentation

# Basics

In `typed` we have three kinds of entities:
1. `types`: are the basic entities
2. `factories`: are functions used to build `types`
3. `typed functions`: are functions with type hints checked at runtime.

In the following we briefly describe how they are defined, used and how they interact one each other.

### Types
 
In `typed`, a `type` is just a class named in `CamelCase`. There are a lot of `primitive types`, which are the building blocks for new `types`. Some of them are Python `builtin`s.

```
type        python builtin
------------------------------
Int         int
Float       float
Str         str
Bool        bool
Nill        type(None)
```

Other examples of `primitive types` in `typed` which are not Python `builtin`s, include:

```
type         description
-----------------------------
Any          the type of anything
Json         the type of a json entity
Path         the type of paths
...
```


Although any `CamelCase` class is acceptable as a `type`, in `typed` the `types` are typically subject to the following conditions: 
1. they are constructed as the concretization of a `metaclass`
2. they are a subclass of some already defined `type`
3. they have a explicit `__instancecheck__` method
4. they may contains a explicit `__subclasscheck__` method

So, a typical definition of `type` is as follows:

```python
# the metaclass
class _SomeType(type(existing_type)):
    ...
    def __instancecheck__(cls, instance):
        ...
    def __subclasscheck__(cls, subclass):
        ...

# the new type
SomeType = _SomeType('SomeType', (existing_type,) {})
```

> A special kind of `type` is the so-called `metatype`. They are "types of types", being named in `UPPERCASE` notation. The main example of `metatype` is `TYPE` which is the `type` of all types. Thus, a `metatype` is any  type `t` such that `issubclass(t, TYPE)` is `True`. Equivalently, it is a type `t` such that if `isinstance(x, t)` is `True` for some `x`, then `isinstance(x, TYPE)` is `True` as well.    
> The metatypes form itself a metatype `META`.
 

### Factories

In `typed`, a `factory` is a `CamelCase` named function that returns a `type`. It can receive `types` as arguments or anything else. In the case where it receive only `types` as arguments, a `factory` is viewed as a `type operation`. Another way of thinking about a `factory` is a [dependent type](https://en.wikipedia.org/wiki/Dependent_type).

There a lot of predefined `factories` from `typed`. Some of them are listed below.

```
factory       description               
------------------------------------------------------
Union         union of types                    
List          list of elements of given types
Tuple         tuple of elements of given types
Set           set of elements of given types
Dict          dict of elements of given types
...
```

Similarly, a `metafactory` is a `factory` which returns a `metatype`. Some examples are the following:

```
metafactory       description               
------------------------------------------------------------
SUB              metatype of all subtypes of given types                    
NOT              metatype of all types which are not the given types
...
```
 
> For the list and definition of all predefined factories, see [here]().

Besides the provided factories, you can create your own. In this case, you should use the decorator `@factory` to ensure type safety in the proper factory definition:

```python
from typed import factory, TYPE,

@factory
def 
```

Since `types` have a predefined form, `factories` (which are functions returning `types`) also have a predefined form:

```python
def SomeFactory(*args):
    ...
    # 1. do something
    ...
    # 2. constructs a metaclass involving the '*args'
    class _SomeType(type(...)):
        ...
        def __instancecheck__(cls, instance):
            ...
        def __subclasscheck__(cls, subclass):
            ...
    # 3. returns a concrete class
    ...
    return _SomeType('SomeType', (...,), {...})
```

> 1. As you can see, there is a factory to each annotation in the library `typing`. In this sense, you can also think of a `factory` as a way to implement the type annotations from `typing`. In this way,  *typed can be viewed as a library in which type hints really works*.
> 2. The `factories` of `typed` that corresponds to type annotations in `typing ` are the "type operations". So, `typed` do much more than just implementing type annotations. Indeed, besides type operations, `typed` provides another example of factories: the so-called `models`, as will be discussed in the sequence.

### Typed Functions

Just use custom types created from `type factories` as type hints for `typed functions`, which are created with the `typed` decorator.

```python
# import 'typed' decorator 
from typed import typed
# import some 'type factories'
from typed import List, Int, Str

# then define a 'typed function'
@typed
def my_function(x: Int, y: Str) -> List(Int, Str):
    return [x, y]
```

If at runtime the type of `x` does not matches `Int` (respectively the type of `y` does not matches `Str` or the return type of `my_function` does not matches `List(Int, Str)`), then a descriptive `Type Error` message is provided, presenting the received types and the expected types.

# Primitive Types

The following  is the list of the primitive `typed` types, from which, using `type factories`, one can build other derived types.

```
primitive Python types
------------------------
type        definition 
--------------------------------------------- 
Int         int
Str         str
Bool        bool
Float       float
Nill        type(None)
```

```
additional typed types
--------------------------
type         definition 
---------------------------------------------
Any          isinstance(x, Any) is True everywhere
Path         Union(Regex(...), Null(Str))
Pattern      isinstance(x, Patter) is True if x is r"..."
Json         Union(Dict(Any), List(Any), Set(Any))
```

```
function types
---------------------------
type           definition
---------------------------------------------
PlainFuncType  ...
HintedFuncType
TypedFuncType
```

# Factories


# Derived Types

```
typed.examples
```

# Use Cases
