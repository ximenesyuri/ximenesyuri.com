---
title: lists of entities
weight: 50
---

# About

In this documentation we present a list of all existing entities in {l:typed} library.

```{toc}
```

# Entities: Metatypes

Below we list the entities accessible from `typed.meta`.

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


