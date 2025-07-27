---
title: types
desc: "the type system"
---

```{title}
```

# About

This documentation described how to use the `type system` provided by [typed](https://ximenesyuri.com/typed).

```{toc}
```

# Basics

In `typed` type system we have three kinds of entities:
1. _types_: are the basic entities
2. _factories_: are functions used to build `types`
3. _typed functions_: are functions with type hints checked at runtime.

In the following we briefly describe how they are defined, used and how they interact one each other.

# Types
 
A `type` is just a class named in `CamelCase`. Types can be organized into _primitive types_ and _derived types_. The first ones are those that comes already defined in `typed`. The other ones are those constructed by the user by making use of `factories`, as we will see in the sequence.

There are a lot of _primitive types_ in `typed`. Some of them are Python builtins.

(table-1)=
```
type        python builtin
----------------------------
Int         int
Float       float
Str         str
Bool        bool
Nill        type(None)
----------------------------
table 1
```

Other examples of _primitive types_ in `typed` which are not Python `builtin`s, include:

(table-2)=
```
type         description
-----------------------------
Any          the type of anything
Json         the type of a json entity
Path         the type of paths
...
--------------------------------
table 2
```

> For the full list of primitive and types, see [here](./lists).

# Defining Types

Although any `CamelCase` class is an acceptable type, in `typed` the types are typically subject to the following conditions: 
1. they are constructed as the concretization of a `metaclass`
2. they are a subclass of some already defined `typed` type
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

# Metatypes

A very special kind of types are the so-called _metatypes_. They are "types of types", being named in `UPPERCASE` notation instead of in `CamelCase` notation. 

- The main example of _metatype_ is `TYPE` which is the `type` of all types.

In more precise terms, a `metatype` is any object `t` such that `issubclass(t, TYPE)` is `True`. Equivalently, it is some `t` such that if `isinstance(x, t)` is `True` for some `x`, then `isinstance(x, TYPE)` is `True` as well.

> The _metatypes_ form themselves a metatype `META`.
 

# Factories

In `typed`, a _factory_ is a `CamelCase` named function that returns a type. It can receive types (i.e, instances of `TYPE`) as arguments or anything else. In the case where it receive only types as arguments, a _factory_ is viewed as a "type operation".

> Another way of thinking about a _factory_ is a [dependent type](https://en.wikipedia.org/wiki/Dependent_type), as will be discussed later.

There a lot of predefined _factories_ in `typed`. Some examples of factories that can be viewed as "type operations" are the following:

(table-3)=
```
factory       description               
------------------------------------------------------
Union         returns the union type of types                    
List          returns the type of list elements of given types
Tuple         returns the type of tuple elements of given types
Set           returns the type of set elements of given types
Dict          returns the type of dict elements of given types
...
--------------------------------
table 3
```

Other examples, which are not "type operations", are:

(table-4)=
```
factory       description               
------------------------------------------------------
Regex         returns type of strings that matches a regex                    
Len           returns the subtype of objects of a given lenght
Not           returns any object which is an instance of given types
Enum          returns the type formed by fixed values of a given type 
Single        returns the type with a single given object
...
--------------------------------
table 4
```

Similarly, a _metafactory_ is a `factory` which returns a _metatype_. As happens with metatypes, metafactories are denoted with `UPPERCASE` notation. Some examples are the following:

(table-5)=
```
metafactory       description               
------------------------------------------------------------
SUB               returns the metatype of all subtypes of given types                    
NOT               returns the metatype of all types which are not the given types
...
--------------------------------
table 5
```

> For the list and definition of all predefined factories, see [here](./lists).
 
# Defining Factories

Besides the predefined factories, you can create your own. In this case, it is recommended to use the decorator `@factory` in order to ensure type safety in factory definition. The basic structure of a factory is as follows:

```python
from typed import factory, Tuple, TYPE

@factory
def SomeFactory(*args: Tuple(...)) -> TYPE:
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

# Annotations, Models and Dependent Types

As you can note from [table above](#table-1), there is a factory to each annotation in the library `typing`. In this sense, you can also think of a `factory` as a way to implement the type annotations from `typing`. In this way:

> `typed` *can be viewed as a library in which type hints really works*.

Note that the _factories_ of `typed` that corresponds to type annotations in `typing ` are always "type operations". On other and, we commented that in `typed` there are other kinds of factories. Therefore, actually 

> `typed` *does much more than just implement type annotations*.

A special flavor of factories are the so-called _models_. They receive a bunch of arguments and produces types that have such arguments as attributes. They work similar  to [dataclasses](https://docs.python.org/3/library/dataclasses.html) or to classes that extends `BaseModel` in [pydantic](https://docs.pydantic.dev/latest/), being specially used for data validation (this will be discussed in the sequence - see [here](./models)). So:

> `typed` *provides an effective mechanism for data validation*.

A generic factory is a function `factory: X -> TYPE` that assigns a type to a collection of arguments, hence can be viewed as an "indexed family of types", hence as an implementation of [dependent types](https://en.wikipedia.org/wiki/Dependent_type) in Python:

> `typed` *implements dependent types in Python*.


# Typed Functions

In `typed`, there is a distinguished class of functions: the _typed functions_. They have the following characteristics:
1. they are defined using the `@typed` decorator;
2. each of its arguments is decorated with an annotation given by a `typed` _type_;
3. it also has a return annotation given by a `typed` _type_.

So, in essence, the structure of a _typed function_ is as follows:

```python
from typed import typed, SomeType, OtherType, ...

@typed
def my_function(some_var: SomeType, ...) -> OtherType:
    ...
```

When you define a function as a _typed function_, its type annotations are checked at runtime, ensuring type safety. This means that, if at runtime `some_var` is not an instance of `SomeType`, or if the return value of `my_function` is not an instance of `OtherType`, then a `TypeError` will be raised.

> The type errors from `typed` are as intuitive as possible. For more about them, see [errors](./3-errors).

# Typed Variables
