---
title: glossary
weight: 900
---

# About

This documentation contains the definition of the main concepts introduced in {lib:typed}. They are present in logic ordering.

# Concepts

(universe)=
> [universe](#universe).
>
> The {lib:typed} _universe_ is the {py:class} `__UNIVERSE__` that works as the {py:metaclass} for all {lib:abstract metatypes}. It requires the implementation of a `__instancecheck__` method. Also, it provides a `__contains__` method which is implemented precisely by the given `__instancecheck__`. 

(universal-metatype)= 
> [universal metatype](#universal-metatype).
>
> A _universal metatype_ is a Python {lib:class} that has the `__UNIVERSE__` as {py:metaclass}. The canonical example is `_TYPE_`: the {lib:universal metatype} which is the {py:abstract metatype} of the {lib:concrete metatype} `TYPE` of all {lib:types}.

(abstract-metatype)= 
> [abstract metatype](#abstract-metatype).
>
> An _abstract metatype_ is a Python {py:class} which is a {py:subclass} of a {lib:universal metatype}. They are named in uppercase: `SOME_META`, `OTHER_META`, ...

(type)=
> [type](#type).
> 
> A _type_ is a {py:class} that has an {lib:abstract metatype} as a {py:metaclass}. Types are names in `CamelCase`: `SomeType`, `OtherType`, ...

(object)=
> [object](#object).
> 
> An _object_ of a {lib:type} is an instance of some {lib:type}. Thus, `x` is an object of a {lib:type} `SomeType` iff `isinstance(x, SomeType)` is `True`. Equivalently, iff `x in SomeType` is `True`.

(concrete-metatype)=
> [concrete metatype](#concrete-metatype).
> 
> A _concrete metatype_ is a {lib:type} `SomeType` whose {lib:objects} are themselves {lib:types}. There is the {lib:concrete metatype} `TYPE` of all {lib:types}.

(subtype)=
> [subtype](#subtype).
> 
> A {lib:type} `SomeType` is a _subtype_ of another {lib:type} `OtherType` if, as a {py:class} it is a {py:subclass} of `OtherType`.

(dom-hinted-function)=
> [domain hinted function](#dom-hinted-function).
> 
> A _domain hinted function_ is a {py:function} such that every {py:parameter} has a {py:type annotation}. They form a {lib:type} `DomHinted`. 

(cod-hinted-function)=
> [codomain hinted function](#cod-hinted-function).
> 
> A _codomain hinted function_ is a {py:function} whose return have a {py:type annotation}. They form a {lib:type} `CodHinted`.

(hinted-function)=
> [hinted function](#hinted-function).
> 
> A _hinted function_ is a {py:function} which is both {lib:domain hinted} and {lib:codomain hinted}. There is the {lib:type} `Hinted` of all {lib:hinted functions}. It is a {lib:subtype} of both `DomHinted` and `CodHinted`.

(domain)=
> [domain](#domain).
>
> The _domain_ of a {lib:domain hinted function} is the {py:tuple} of the {py:type annotations} of their {py:parameters}.

(codomain)=
> [codomain](#codomain).
>
> The _codomain_ of a {lib:codomain hinted function} is its return {py:type annotations}.

(dom-typed-function)=
> [domain typed function](#dom-typed-function).
> 
> A _domain typed function_ is a {lib:domain hinted function} whose {py:type annotations} are {lib:types} or {lib:dependent types} which are checked at runtime. They form a {lib:type} `DomTyped` which is a {lib:subtype} of `DomHinted`.

(cod-typed-function)=
> [codomain typed function](#cod-typed-function).
> 
> A _codomain typed function_ is a {lib:codomain hinted function} whose return {py:type annotation} is a {lib:type} or a {lib:dependent type}, checked at runtime. They form a {lib:type} `CodTyped` which is a {lib:subtype} of `CodHinted`.

(typed-function)=
> [typed function](#typed-function).
> 
> A _typed function_ is a {py:function} which is both {lib:domain hinted} and {lib:codomain hinted}, so that all their {py:type annotations} are {lib:types} or {lib:dependent types}, being checked at runtime.  There is the {lib:type} `Typed` of all {lib:typed functions}. It is a {lib:subtype} of both `DomTyped`, `CodTyped` and `Hinted`.

(type-factory)=
> [type factory](#type-factory).
> 
> A _type factory_ is a {lib:typed function} whose {lib:codomain} is `TYPE`, the {lib:concrete metatype} of all {lib:types}. Thus, a type factory is some process constructing a {lib:type} depending on certain {py:parameters}.

(parametric-type)=
> [parametric type](#parametric-type). 
>
> A _parametric type_ is {lib:type} which also is a {lib:type factory}. Thus, it is a {lib:type} whose {lib:abstract metatype} has a `__call__` method that returns a {lib:type factory}.

(dependent-type)=
> [dependent type](#dependent-type). 
>
> A _dependent type_ is {lib:type} which also is a {lib:type factory}. Thus, it is a {lib:type} whose {lib:abstract metatype} has a `__call__` method that returns a {lib:type factory}.

(condition)=
> [condition](#condition).
> 
> A _condition_ (a.k.a _predicate_) is a {lib:type factory} that constructs booleans, hence that take values into `Bool`.
