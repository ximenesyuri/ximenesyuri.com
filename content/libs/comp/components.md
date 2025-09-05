---
title: components
desc: components
weight: 10
---

# About

In the following we will briefly describe how the _components_ in {lib:comp} component system work.

```{toc}
```

# Components

In {lib:comp}, a _component_ is a {lib:typed function} such that:
1. it returns a {lib:jinja string}, so that its returning type is the `Jinja` type;
2. it is decorated with the `@component` {py:decorator}.

Thus, a typical component is defined as follows:

(component)=
```python
from typed import SomeType, OtherType, AnotherType ...
from comp import component, Jinja

@component
def my_comp(x: SomeType, y: OtherType, z: AnotherType ...) -> Jinja:
    ...
    return f"""jinja
[% for i in x %]
<some html>
    [% if y is True %]
    <more html>
    ...
    { z }
    ...
    </more html>
    [% endif %]
</some html>
[% endfor %]
"""
```

(rem-1)=
> [Remark 1](#rem-1). 
> 1. Instead of using the `@component` decorator to define a component, you can use its short alias `@comp`.
> 2. The components form a {lib:type} `COMPONENT`.

# Context

As we will see in the [rendering](./rendering) documentation, not only {lib:jinja strings} but also {lib:components} can be rendered. Recall that to render a jinja string we need to fix all their {lib:jinja free vars}, which is done by providing a {lib:jinja context}. Similarly, to render a component we need to provide a _component context_.

Instead of providing the entire context while rendering a {lib:component}, one can endow it with a _local context_ along its definition, which is automatically included in the {lib:component context}, simplifying a lot the rendering process. This is done through a special {lib:parameter} `__context__`.

There are two cases where the use of `__context__` is strongly recommended:
1. when using {py:local vars} inside the {jinja} syntax of the {lib:jinja string};
2. when calling external {lib:components} inside the {lib:jinja string}.

For example, these cases occur when one needs to (see below):
1. loop with `[% for ...  %]` through a {lib:local var};
2. add something conditionally with `[% if ... %]` depending on a local var or an external component.

```python
from typed import SomeType, ...
from comp import component, Jinja
from some.where import some_comp

@component
def my_comp(x: SomeType,...,__context__={"some_comp": some_comp}) -> Jinja:
    ...
    local_var = [ ... ]
    __context__.update({"local_var": local_var})
    ...
    return f"""jinja
[% for i in local_var %]
<some html>
    [% if some_comp() == "something" %]
    <more html>
    ...
    </more html>
    [% endif %]
</some html>
[% endfor %]
"""
```
(rem-2)=
> [Remark 2](#rem-2). Recall that a {lib:component} is a {lib:typed function}, which means that all their {py:parameters} need to have a {py:type annotation}. An exception is the parameter `__context__`, whose type annotation `Dict(Any)` is automatically introduced by the {py:decorator} `@component`.

# Bounding

In a {lib:component}, each parameter appearing in its {lib:jinja string} is a {lib:free jinja var}, so that it need to be fixed in the {lib:jinja context}.  A _leak_ in a component is a {lib:jinja free var} of the underlying jinja string which does not corresponds to a component {py:parameter}.  For example, the cases listed in the previous section are typical situations where leaks occur.

A {lib:component} is said to be _bounded_ if every leak is declared in the {lib:local context} `__context__`.

> The best practice is to always try to build _bounded components_.

# Factories

Some times one needs to build parameterized families of {lib:components}. This can be realized through _component factories_, i.e, {lib:type factories} which constructs subtypes of `COMPONENT`, hence that take values into `SUB(COMPONENT)`.

One can construct component factories by first constructing {lib:jinja factories}. Indeed, if `factory: X -> SUB(Jinja)` is a {lib:jinja factory}, then one can obtain a subtype `FACTORY(x)` of `COMPONENT`, by considering all {lib:components} that take values into `factory(x)` for a given `x in X`. So, varying `x` we build a {lib:type factory} factory `FACTORY: X -> SUB(COMPONENT)`.

# Tags
      
Typically, when one think of a "component" one imagine something which is delimited by a HTML tag. There are a class of {lib:components} in {lib:comp} that realizes that feeling.

More precisely, there is {lib:jinja factory} `Tag: Tuple(Str) -> SUB(Jinja)` that receives a tuple of HTML tag names and returns the subtype `Tag(*tags)` of `Jinja` consisting of all {lib:jinja strings} enclosed by one of the given tags.

So, for example, the following is instance of `Tag('some-tag')`:
```python
"""jinja
<some-tag>
...
</some-tag>
"""
```

With this {lib:jinja factory} one can construct type safe tag-based components, the so-called _tag components_, by making use of the strategy described [above](#factories):

```python
from comp import component, Tag

@component
def my_tag_comp(...) -> Tag('some-tag'):
    ...
    return """jinja
<some-tag>
...
</some-tag>
"""
```

This means that for each tuple of tags there is a subtype `TAG(*tags)` of `COMPONENT` of all components whose returning string belongs to `Tag(*tags)`. There is, also, a {lib:type factory} `TAG: Tuple(Str) -> SUB(COMPONENT)` that associates to each tuple the corresponding type `TAG(*tags)`.
   
# Inners
    
In {lib:comp}, the components have another special kind of {py:parameters}: the _inner_ ones. They are necessarily of type `Inner`, and work as placeholders for future inserts inside the {lib:component}.

(inner-comp)=
```python
from comp import component, Tag, Inner

@component
def my_inner_comp(..., inner: Inner, ...) -> Tag('some-tag'):
    ...
    return """jinja
<some-tag>
    {{ inner }}
</some-tag>
"""
```

The {lib:type} `Inner` is a presentation of the `Jinja` type. This means that it only accept {lib:jinja strings}. It is typically used to receive the {lib:jinja string} of other {lib:component}, in some sort of {lib:component concatenation}.

One can filter the type `COMPONENT` by looking at {lib:components} that have a fixed number of {lib:inner vars}. Indeed, when viewed as a {py:callable entity}, the type `COMPONENT` accepts an integer `inners in Int` such that:
1. for `inners >= 0`, `COMPONENT(inners)` is the subtype of `COMPONENT` consisting of all {lib:components} that have precisely `inners` {lib:inner vars};
2. for `inners < 0`, `COMPONENT(inners)` is the subtype of `COMPONENT` of all {lib:components} that have __any__ number of {lib:inner vars}. Thus, of course, there is a {lib:type equivalence} between `COMPONENT(inners<0)` and `COMPONENT`.

# Contents

There is one more special kind of {py:parameters} in {lib:components}: that of {lib:type} `Content`. They can receive:
1. `Markdown` content
2. `ReStructuredText` content
3. or a path to some `.md` or `.rst` file.

Therefore, they are used to receive _static content_, which will be automatically converted to raw HTML in the {lib:rendering} process. This opens the possibility to use {lib:comp} as a component system to both dynamic and static websites.

As happens with {lib:inner vars}, the {lib:content vars} also filter the {lib:type} `COMPONENT` through a integer parameter, here called `contents`:
1. for `contents >= 0`, `COMPONENT(contents)` is the subtype of `COMPONENT` given by all {lib:components} that have precisely `contents` {lib:content vars};
2. for `contents < 0`, `COMPONENT(contents)` {lib:type equivalent} to `COMPONENT`.

> Of course, the {lib:type} of all {lib:components} can be simultaneously filtered by both {lib:inner vars} and {lib:content vars}, producing subtypes `COMPONENT(inners, contents)`.

# Attributes

The {lib:type} `COMPONENT` of all {lib:components} also come equipped with some {py:properties}, which define some {lib:component attributes}:

(table-1)=
```
attribute           description 
-----------------------------
.jinja              the component jinja string
.leaks              the component leaks
.inner_params       tuple of inner args
.content_params     tuple of content_args
.tags               the tuple of defining tags
.is_page            if the component is a page
-----------------------------
table 1: component attributes
```

From the {lib:functions over methods} philosophy of {lib:typed}, such {py:attributes} can also be obtained from {lib:typed functions}:

(table-2)=
```
attribute           typed function 
-----------------------------
.jinja              get_jinja
.leaks              get_leaks
.inner_params       get_inner_params
.content_params     get_content_params
.tags               get_tags
.is_page            is_page
-----------------------------
table 1: component attributes and their typed functions
```

# Operations

There are four main operations involving {lib:components}:
1. `join: Prod(COMPONENT, n) -> COMPONENT`:
    - receives a tuple of components and creates a new component whose {lib:jinja string} is the join of the {lib:jinja strings} of the provided components;
2. `concat: Prod(COMPONENT(1), COMPONENT) -> COMPONENT`:
    - receives a component with a single {lib:inner var} and another arbitrary component, producing a new component whose {lib:jinja string} is obtained by replacing the placeholder given by {lib:inner var} in the first component with the {lib:jinja string} of the second component.
3. `evalib: Prod(COMPONENT, Dict(Any)) -> COMPONENT`:
    - receives a {lib:component} and a list with keys and values, returning the component obtained by fixing each variable associated to a _key_ with the corresponding _value_, leaving the other variables unchanged.
4. `copy: Prod(COMPONENT, Dict(Str)) -> COMPONENT`:
    - receives a {lib:component} and a list with keys and values, returning a copy of the given component such that each parameter whose name is a key is renamed with the corresponding value, maintaining its type.

The intuition for each of such {lib:component operations} is as follows:
1. `join`: put a component _after_ other component;
2. `concat`: put a component _inside_ other component;
3. `eval`: from a component, _fixes_ some part of it;
4. `copy`: from a component, _copy_ it.

So, for example, consider the following generic {lib:components}:

```python
from typed import SomeType, OtherType
from comp import Jinja, component, Tag, Inner

@component
def some_comp(x: SomeType, ...) -> Jinja
    ...
    return """jinja
[[ contents of 'some_comp' jinja string ]]
"""

@component
def inner_comp(a: OtherType, inner: Inner, ...) -> Tag('some-tag')
    ...
    return f"""jinja
<some-tag>
    { inner }
</some-tag>
"""
```

Applying the {lib:component join} to them we get a new {lib:component} `join(some_comp, inner_comp)` which is equivalent to the following:

```python
@component
def joined_comp(x: SomeType, ..., a: OtherType, inner: Inner, ...) -> Jinja:
    return f"""jinja
[[ contents of 'some_comp' jinja string ]]
<some-tag>
    { inner }
</some-tag>
"""
```

On the other hand, the {lib:component concat} produces a {lib:component} `concat(inner_comp, some_comp)` which is equivalent to:

```python
@component
def concat_comp(a: OtherType, x: SomeType, ...) -> Tag('some-tag'):
    return """jinja
<some-tag>
    [[ contents of 'some_comp' jinja string ]]
</some-tag>
"""
```

Also, `eval(inner_comp, inner=Jinja(blablabla))` is the same as defining the component below.

```python
@component
def eval_comp(a: OtherType, ...) -> Tag('some-tag'):
    return """jinja
<some-tag>
    blablabla
</some-tag>
"""
```

Finally, `copy(inner_comp, {"inner": "other_name"})` produces the following {lib:component}:

```python
@component
def copied_comp(a: OtherType, other_name: Inner, ...) -> Jinja:
    return f"""jinja
<some-tag>
    { other_name }
</some-tag>
"""
```

# Overlapping

One should note that the {lib:components} subject to the {lib:component operations} could have overlapping {py:parameters}. About that, some remarks:

1. The {py:parameters} of the {lib:component join} and the {lib:component concat} are obtained from the union of tuple of {py:parameters} of the underlying {lib:components}. This means that their multiplicity is not considered. More precisely, if components `comp_1` and `comp_2` share some parameter, then it will appear a single time in `join(comp_1, comp_2)` and in `concat(comp_1, comp_2)`.
2. If the shared parameters are of different {lib:types}, a {py:type error} will be raised.

So, for example, consider the following components:

```python
from typed import SomeType, OtherType, AnotherType, ...
from comp import component, Jinja

@component
def comp_1(x: SomeType, y: OtherType, ...) -> Jinja:
    ...

@component
def comp_2(x: SomeType, z: AnotherType, ...) -> Jinja:
    ...

@component
def comp_3(x: SomeType, y: AnotherType, ...) -> Jinja:
    ...
```

Then `join(comp_1, comp_3)` will raise a {py:type error}, while `join(comp_1, comp_2)` and `join(comp_2, comp_3)` will generate components equivalent to the following ones:

```python
from typed import SomeType, OtherType, AnotherType, ...
from comp import component, Jinja

@component
def comp_1_2(x: SomeType, y: OtherType, z: AnotherType) -> Jinja:
    ...

@component
def comp_2_3(x: SomeType, z: AnotherType, y: OtherType) -> Jinja:
    ...
```

To avoid the overlapping behavior, you should make a {lib:component copy} of some of the components before the {lib:component join} and {lib:component concat}, changing the name of the repeating {py:parameter}, as follows (this is precisely the typical use case of the {lib:component copy} operation):

```python
from comp import copy
from some.where import comp_1, comp_2, comp_3

copied_2 = copy(comp_2, x="x_2")
copied_3 = copy(comp_2, x="x_3", y="y_3")
```

In this case, `join(comp_1, copied_2, copied_3)` has no overlapping, being equivalent to the following {lib:component}:

```python
from typed import SomeType, OtherType, AnotherType, ...
from comp import component, Jinja, copy

@component
def joined_comp(
        x:   SomeType,
        y:   OtherType,
        x_2: OtherType,
        z:   AnotherType,
        x_3: OtherType,
        y_3: AnotherType
    ) -> Jinja:
    ...
```

# Arithmetic

In the type `COMPONENT`, the operations `join` and `concat` corresponds, respectively to implementations of the class functions `__sum__` and `__mul__`. This means that instead of writing `join(comp_1, comp_2)` you can just write `comp_1 + comp_2`. Similarly, instead of `concat(comp_1, comp_2)`, you can write `comp_1 * comp_2`.

Therefore, the `COMPONENT` type has an internal "component arithmetic" that can be used to build complex components from smaller ones.

# Other Docs

```{toc-dir}
```
