---
title: api
weight: 50
---

# About

In this documentation we present the interface to interact with {l:typed} library.

```{toc}
```

# Entry Points

The lib {l:typed} has the following entry points, organized by entity kinds:

```
typed/
  ├── meta.py ............. importing the {l:metatypes}
  ├── types.py ............ importing the {l:types}
  ├── parametrics.py ...... importing {l:parametric types}
  ├── factories.py ........ importing {l:type factories}
  ├── decorators.py ....... importing the main {p:decorators}
  ├── models.py ........... importing entities related to {l:models}
  ├── poly.py ............. importing entities relates to {l:parametric polymorphisms}
  ├── extra.py  ........... importing extra {l:types} and {l:type factories}
  └── helper.py ........... importing helper {p:functions}
```

Thus, for example, to use some {l:metatype}, a {l:type}, a {l:type factory}, and so on, you can do:

```python
from typed.meta       import SOME_META
from typed.types      import SomeType
from typed.factories  import SomeFactory
from typed.decorators import some_decorator
from typed.models     import SomeModel
...
```

There is also a main entry point which imports everything from the other entry points:

```
typed/
  ├── ...
  └── __init__.py ............. importing everything
```

So, alternatively, to use a {l:metatype}, {l:type}, and so on, ou could also do:

```python
from typed import SOME_META, SomeType, SomeFactory, ...
```

(rem-1)=
> [Remark 1](#rem-1). The first approach is LSP optimized. Indeed, before importing something you can list:
> 1. the entity kinds: `from typed.<tab>` will list the entry points
> 2. the entries of a given kind: `from typed.<kind> <tab>` will list the exposed entities of the given kind

In the following we list the entities which are exposed in each entry point.

(rem-2)=
> [Remark 2](#rem-2). The entry points are essentially disjoint. The only exception is `typed.types` and ` typed.parametric`: the last one contains a selected list of entities in the first one.

# Entities: `typed.meta`

(table-1)=
```
type              metatype         subtype of        description 
----------------------------------------------------------------------------------------------
__UNIVERSE__      type             type              metaclass of abstract meta
_TYPE_            __UNIVERSE__     ---               universal meta of types
_META_            ---              _TYPE_            abst. meta of concrete metatypes
_PARAMETRIC_      ---              _TYPE_            abst. meta of parametric types
_DISCOURSE_       ---              _TYPE_            abst. meta of iterable types
----------------------------------------------------------------------------------------------
table 1: foundational metatypes
```

(table-2)=
```
type            metatype        subtype of        description 
----------------------------------------------------------------------------------------------
TYPE            _TYPE_          ---               conc. meta of all types
META            _META_          TYPE              conc. meta of all concrete metatypes
PARAMETRRIC     _PARAMETRIC_    TYPE              conc. meta of all parametric types
DISCOURSE       _DISCOURSE_     TYPE              conc. meta of all discourses
----------------------------------------------------------------------------------------------
table 2: concrete metatypes
```

(table-3)=
```
type            metatype      subtype of      description
---------------------------------------------------------------------------
NILL            _TYPE_        ---             abst. meta for Nill type
INT             _TYPE_        ---             abst. meta for Int type
BOOL            _TYPE_        ---             abst. meta for Bool type
FLOAT           _TYPE_        ---             abst. meta for Float type
STR             _TYPE_        ---             abst. meta for Str type
ANY             _TYPE_        ---             abst. meta for Any type
----------------------------------------------------------------------------
table 3: base metatypes
```

(table-4)=
```
type        metatype        subtype of         description 
-------------------------------------------------------------------------------------------------
TUPLE       ---             _TYPE_             abst. meta for Tuple param. type
LIST        ---             _TYPE_             abst. meta for List param. type
SET         ---             _TYPE_             abst. meta for Set param. type
DICT        ---             _TYPE_             abst. meta for Dict param. type
-------------------------------------------------------------------------------------------------
table 4: base parametric abstract metatypes
```

(table-5)=
```
type             metatype      subtype of                       description 
---------------------------------------------------------------------------------------------------
CALLABLE         ---           _TYPE_                           abst. meta for Callable type
GENERATOR        ---           _TYPE_                           abst. meta for Generator type
BUILTIN          ---           CALLABLE                         abst. meta for Builtin type
BOUND_METHOD     ---           CALLABLE                         abst. meta for BoundMethod type
UNBOUD_METHOD    ---           CALLABLE                         abst. meta for UnboudMethod type
METHOD           ---           CALLABLE                         abst. meta for Method type
LAMBDA           ---           CALLABLE                         abst. meta for Lambda type
FUNCTION         ---           CALLABLE                         abst. meta for Function param. type
COMPOSABLE       ---           FUNCTION                         abst. meta for Composable type
HINTED_DOM       ---           COMPOSABLE                       abst. meta for HintedDom param. type
HINTED_COD       ---           COMPOSABLE                       abst. meta for HintedCod param. type
HINTED           ---           HINTED_DOM, HINTED_COD           abst. meta for Hinted param. type
TYPED_DOM        ---           HINTED_DOM                       abst. meta for TypedDom param. type
TYPED_COD        ---           HINTED_COD                       abst. meta for TypedCod param. type
TYPED            ---           TYPED_DOM, TYPED_COD, HINTED     abst. meta for TypedDom param. type
CONDITION        ---           TYPED                            abst. meta for Condition param. type
FACTORY          ---           TYPED                            abst. meta for Factory param. type
OPERATION        ---           FACTORY                          abst. meta for Operation param. type
DEPENDENT        ---           DEPENDENT                        abst. meta for Dependent param. type
--------------------------------------------------------------------------------------------------------
table 5: function metatypes
```

# Entities: `typed.types`

(table-6)=
```
type       metatype       subtype of       description
-------------------------------------------------------------------------------
Nill       NILL           ---              type whose only object is None
Any        ANY            ---              type whose objects are anything
Int        INT            ---              type whose objects are integers
Bool       BOOL           ---              type whose objects are booleans
Float      FLOAT          ---              type whose objects are floats
Str        STR            ---              type whose objects are strings
Tuple      TUPLE          ---              type whose objects are tuples
List       LIST           ---              type whose objects are lists
Set        SET            ---              type whose objects are sets
Dict       DICT           ---              type whose objects are dictionaries
----------------------------------------------------------------------------------
table 6: base types
```

(table-7)=
```
type           metatype         subtype of                    description
-------------------------------------------------------------------------------------------------
Callable       CALLABLE         ---                           type of generic callable objects
Generator      GENERATOR        ---                           type whose objects are generators
Builtin        BUILTIN          Callable                      type of Python builtin functions
Lambda         LAMBDA           Callable                      type whose objects are lambda functions
Function       FUNCTION         Callable                      type whose objects are user defined functions
BoundMethod    BOUND_METHOD     Callable                      type whose objects are bound methods
UnboudMethod   UNBOUND_METHOD   Callable                      type whose objects are unbound methods
Method         METHOD           Callable                      type whose objects are generic methods
Composable     COMPOSABLE       Function                      type whose objects are composable functions
HintedDom      HINTED_DOM       Function                      type whose objects are hinted domain functions
HintedCod      HINTED_COD       Function                      type whose objects are hinted codomain functions
Hinted         HINTED           HintedDom, HintedCod          type whose objects are hinted functions
TypedDom       TYPED_Dom        HintedDom                     type whose objects are typed domain functions
TypedCod       TYPED_COD        HintedCod                     type whose objects are typed codomain functions
Typed          TYPED            TypedDom, TypedCod, Hinted    type whose objects are typed functions
Condition      CONDITION        Typed                         type whose objects are conditions
Factory        FACTORY          Typed                         type whose objects are type factories
Operation      OPERATION        Factory                       type whose objects are operations
Dependent      DEPENDENT        Factory                       type whose objects are dependent types
--------------------------------------------------------------------------------------------------------
table 7: base function types
```

# Entities: `typed.parametrics`

(table-8)=
```
parametric         arguments          description 
-----------------------------------------------------
...
-----------------------------------------------------
table 8: base parametrics
```

(table-9)=
```
parametric         arguments          description
-----------------------------------------------------
...
-----------------------------------------------------
table 9: function parametrics
```

# Entities: `typed.factories`

(table-10)=
```
factory       arguments                description     
-----------------------------------------------------------------------------
Union         *types: Tuple(TYPE)      create the union type
Prod          *types: Tuple(TYPE)      create the product type
UProd         *types: Tuple(TYPE)      create the unordered product type
-----------------------------------------------------------------------------
table 10: base factories
```

(table-11)=
```
factory        arguments              description 
---------------------------------------------------------------------------------------------------------------
ATTR           attr: Str              create the conc. meta of all types that have the given attribute
SUBTYPES       typ: TYPE              create the conc. meta of all subtypes of a given type
NOT            *types: Tuple(TYPE)    create the conc. meta of all types which are not any of the given types
----------------------------------------------------------------------------------------------------------------
table 11: metafactories
```

(table-12)=
```
factory        arguments                               description 
--------------------------------------------------------------------------------------------------------------------------------------------
Inter          *types: Tuple(TYPE)                     create the intersection type
Filter         typ: TYPE, *cond: Tuple(Condition)      create the subtype of typ whose objects match the given conditions
Compl          typ: TYPE, *subs: Tuple(SUB(typ))       create the type of all objects of 'typ' which are not objects of the given subtypes
Regex          regex: Pattern                          create the subtype of 'Str' of all strings that matches the given pattern
Range          x: Int, y: Int                          create the subtype of 'Int' of integers between 'x' and 'y'
Not            *types: Tuple(TYPE)                     create the type whose objects are anything except the objects of the given types
Enum           typ: TYPE, *values: Tuple(typ)          create the subtype of 'typ' consisting of the given values
Single         obj: Any                                create the type with a single object: the given one
Null           typ: TYPE                               create the subtype of 'typ' formed by its null objects
NotNull        typ: TYPE                               create the subtype of 'typ' formed by its not null objects
Len            typ: ATTR("__len__"), len: Int          create the subtype of a sized type 'typ' of the objects with a given lenght
Maybe          typ: TYPE                               create the type whose objects are the 'None' or objects of 'typ'
--------------------------------------------------------------------------------------------------------------------------------------------
table 12: generic factories
```

# Entities: `typed.decorators`

(table-13)=
```
decorator         arguments                       description
----------------------------------------------------------------------------------------------------
@hinted           func: Function                  validate and create a {l:hinted function}
@typed            arg: Union(TYPE, Function)      validate and create a {l:typed function} or variable
@condition        func: Function                  validate and create a {l:condition}
@factory          func: Function                  validate and create a {l:type factory}
@operation        func: Function                  validate and create a {l:type operation}
@dependent        func: Function                  validate and create a {l:dependent type}
----------------------------------------------------------------------------------------------------
table 13: decorators
```

# Other Docs

```{toc-dir}
```
