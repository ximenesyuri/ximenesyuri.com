---
title: glossary
weight: 900
---

# About

This documentation contains the definition of the main concepts introduced in {l:typed}. They are present in logic ordering.

# Concepts

(universe)=
> [universe](#universe).
>
> The {l:typed} _universe_ is the {p:class} `__UNIVERSE__` that works as the {p:metaclass} for all {l:abstract metatypes}. It requires the implementation of a `__instancecheck__` method. Also, it provides a `__contains__` method which is implemented precisely by the given `__instancecheck__`. 

(universal-metatype)= 
> [universal metatype](#universal-metatype).
>
> A _universal metatype_ is a Python {l:class} that has the `__UNIVERSE__` as {p:metaclass}. The canonical example is `_TYPE_`: the {l:universal metatype} which is the {p:abstract metatype} of the {l:concrete metatype} `TYPE` of all {l:types}.

(abstract-metatype)= 
> [abstract metatype](#abstract-metatype).
>
> An _abstract metatype_ is a Python {p:class} which is a {p:subclass} of a {l:universal metatype}. They are named in uppercase: `SOME_META`, `OTHER_META`, ...

(type)=
> [type](#type).
> 
> A _type_ is a {p:class} that has an {l:abstract metatype} as a {p:metaclass}. Types are names in `CamelCase`: `SomeType`, `OtherType`, ...

(object)=
> [object](#object).
> 
> An _object_ of a {l:type} is an instance of some {l:type}. Thus, `x` is an object of a {l:type} `SomeType` iff `isinstance(x, SomeType)` is `True`. Equivalently, iff `x in SomeType` is `True`.

(concrete-metatype)=
> [concrete metatype](#concrete-metatype).
> 
> A _concrete metatype_ is a {l:type} `SomeType` whose {l:objects} are themselves {l:types}. There is the {l:concrete metatype} `TYPE` of all {l:types}.

(subtype)=
> [subtype](#subtype).
> 
> A {l:type} `SomeType` is a _subtype_ of another {l:type} `OtherType` if, as a {p:class} it is a {p:subclass} of `OtherType`.

(dom-hinted-function)=
> [domain hinted function](#dom-hinted-function).
> 
> A _domain hinted function_ is a {p:function} such that every {p:parameter} has a {p:type annotation}. They form a {l:type} `DomHinted`. 

(cod-hinted-function)=
> [codomain hinted function](#cod-hinted-function).
> 
> A _codomain hinted function_ is a {p:function} whose return have a {p:type annotation}. They form a {l:type} `CodHinted`.

(hinted-function)=
> [hinted function](#hinted-function).
> 
> A _hinted function_ is a {p:function} which is both {l:domain hinted} and {l:codomain hinted}. There is the {l:type} `Hinted` of all {l:hinted functions}. It is a {l:subtype} of both `DomHinted` and `CodHinted`.

(domain)=
> [domain](#domain).
>
> The _domain_ of a {l:domain hinted function} is the {p:tuple} of the {p:type annotations} of their {p:parameters}.

(codomain)=
> [codomain](#codomain).
>
> The _codomain_ of a {l:codomain hinted function} is its return {p:type annotations}.

(dom-typed-function)=
> [domain typed function](#dom-typed-function).
> 
> A _domain typed function_ is a {l:domain hinted function} whose {p:type annotations} are {l:types} or {l:dependent types} which are checked at runtime. They form a {l:type} `DomTyped` which is a {l:subtype} of `DomHinted`.

(cod-typed-function)=
> [codomain typed function](#cod-typed-function).
> 
> A _codomain typed function_ is a {l:codomain hinted function} whose return {p:type annotation} is a {l:type} or a {l:dependent type}, checked at runtime. They form a {l:type} `CodTyped` which is a {l:subtype} of `CodHinted`.

(typed-function)=
> [typed function](#typed-function).
> 
> A _typed function_ is a {p:function} which is both {l:domain hinted} and {l:codomain hinted}, so that all their {p:type annotations} are {l:types} or {l:dependent types}, being checked at runtime.  There is the {l:type} `Typed` of all {l:typed functions}. It is a {l:subtype} of both `DomTyped`, `CodTyped` and `Hinted`.

(type-factory)=
> [type factory](#type-factory).
> 
> A _type factory_ is a {l:typed function} whose {l:codomain} is `TYPE`, the {l:concrete metatype} of all {l:types}. Thus, a type factory is some process constructing a {l:type} depending on certain {p:parameters}.

(parametric-type)=
> [parametric type](#parametric-type). 
>
> A _parametric type_ is {l:type} which also is a {l:type factory}. Thus, it is a {l:type} whose {l:abstract metatype} has a `__call__` method that returns a {l:type factory}.

(dependent-type)=
> [dependent type](#dependent-type). 
>
> A _dependent type_ is {l:type} which also is a {l:type factory}. Thus, it is a {l:type} whose {l:abstract metatype} has a `__call__` method that returns a {l:type factory}.

(condition)=
> [condition](#condition).
> 
> A _condition_ (a.k.a _predicate_) is a {l:type factory} that constructs booleans, hence that take values into `Bool`.
