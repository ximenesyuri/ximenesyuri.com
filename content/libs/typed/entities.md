---
title: lists of entities
weight: 50
---

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
