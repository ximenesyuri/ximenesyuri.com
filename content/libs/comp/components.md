---
title: components
desc: components
weight: 10
---

# About

In the following we will briefly describe how the _components_ in {l:comp} component system work.

```{toc}
```

# Components

In {l:comp}, a _component_ is a {l:typed function} such that:
1. it returns a {l:jinja string}, so that its returning type is the `Jinja` type;
2. it is decorated with the `@component` {p:decorator}.

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
> 2. The components form a {l:type} `COMPONENT`.

# Context

As we will see in the [rendering](./rendering) documentation, not only {l:jinja strings} but also {l:components} can be rendered. Recall that to render a jinja string we need to fix all their {l:jinja free vars}, which is done by providing a {l:jinja context}. Similarly, to render a component we need to provide a _component context_.

Instead of providing the entire context while rendering a {l:component}, one can endow it with a _local context_ along its definition, which is automatically included in the {l:component context}, simplifying a lot the rendering process. This is done through a special {l:parameter} `__context__`.

There are two cases where the use of `__context__` is strongly recommended:
1. when using {p:local vars} inside the {jinja} syntax of the {l:jinja string};
2. when calling external {l:components} inside the {l:jinja string}.

For example, these cases occur when one needs to (see below):
1. loop with `[% for ...  %]` through a {l:local var};
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
> [Remark 2](#rem-2). Recall that a {l:component} is a {l:typed function}, which means that all their {p:parameters} need to have a {p:type annotation}. An exception is the parameter `__context__`, whose type annotation `Dict(Any)` is automatically introduced by the {p:decorator} `@component`.

# Bounding

In a {l:component}, each parameter appearing in its {l:jinja string} is a {l:free jinja var}, so that it need to be fixed in the {l:jinja context}.  A _leak_ in a component is a {l:jinja free var} of the underlying jinja string which does not corresponds to a component {p:parameter}.  For example, the cases listed in the previous section are typical situations where leaks occur.

A {l:component} is said to be _bounded_ if every leak is declared in the {l:local context} `__context__`.

> The best practice is to always try to build _bounded components_.

# Factories

Some times one needs to build parameterized families of {l:components}. This can be realized through _component factories_, i.e, {l:type factories} which constructs subtypes of `COMPONENT`, hence that take values into `SUB(COMPONENT)`.

One can construct component factories by first constructing {l:jinja factories}. Indeed, if `factory: X -> SUB(Jinja)` is a {l:jinja factory}, then one can obtain a subtype `FACTORY(x)` of `COMPONENT`, by considering all {l:components} that take values into `factory(x)` for a given `x in X`. So, varying `x` we build a {l:type factory} factory `FACTORY: X -> SUB(COMPONENT)`.

# Tags
      
Typically, when one think of a "component" one imagine something which is delimited by a HTML tag. There are a class of {l:components} in {l:comp} that realizes that feeling.

More precisely, there is {l:jinja factory} `Tag: Tuple(Str) -> SUB(Jinja)` that receives a tuple of HTML tag names and returns the subtype `Tag(*tags)` of `Jinja` consisting of all {l:jinja strings} enclosed by one of the given tags.

So, for example, the following is instance of `Tag('some-tag')`:
```python
"""jinja
<some-tag>
...
</some-tag>
"""
```

With this {l:jinja factory} one can construct type safe tag-based components, the so-called _tag components_, by making use of the strategy described [above](#factories):

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

This means that for each tuple of tags there is a subtype `TAG(*tags)` of `COMPONENT` of all components whose returning string belongs to `Tag(*tags)`. There is, also, a {l:type factory} `TAG: Tuple(Str) -> SUB(COMPONENT)` that associates to each tuple the corresponding type `TAG(*tags)`.
   
# Inners
    
In {l:comp}, the components have another special kind of {p:parameters}: the _inner_ ones. They are necessarily of type `Inner`, and work as placeholders for future inserts inside the {l:component}.

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

The {l:type} `Inner` is a presentation of the `Jinja` type. This means that it only accept {l:jinja strings}. It is typically used to receive the {l:jinja string} of other {l:component}, in some sort of {l:component concatenation}.

One can filter the type `COMPONENT` by looking at {l:components} that have a fixed number of {l:inner vars}. Indeed, when viewed as a {p:callable entity}, the type `COMPONENT` accepts an integer `inners in Int` such that:
1. for `inners >= 0`, `COMPONENT(inners)` is the subtype of `COMPONENT` consisting of all {l:components} that have precisely `inners` {l:inner vars};
2. for `inners < 0`, `COMPONENT(inners)` is the subtype of `COMPONENT` of all {l:components} that have __any__ number of {l:inner vars}. Thus, of course, there is a {l:type equivalence} between `COMPONENT(inners<0)` and `COMPONENT`.

# Contents

There is one more special kind of {p:parameters} in {l:components}: that of {l:type} `Content`. They can receive:
1. `Markdown` content
2. `ReStructuredText` content
3. or a path to some `.md` or `.rst` file.

Therefore, they are used to receive _static content_, which will be automatically converted to raw HTML in the {l:rendering} process. This opens the possibility to use {l:comp} as a component system to both dynamic and static websites.

As happens with {l:inner vars}, the {l:content vars} also filter the {l:type} `COMPONENT` through a integer parameter, here called `contents`:
1. for `contents >= 0`, `COMPONENT(contents)` is the subtype of `COMPONENT` given by all {l:components} that have precisely `contents` {l:content vars};
2. for `contents < 0`, `COMPONENT(contents)` {l:type equivalent} to `COMPONENT`.

> Of course, the {l:type} of all {l:components} can be simultaneously filtered by both {l:inner vars} and {l:content vars}, producing subtypes `COMPONENT(inners, contents)`.

# Attributes

The {l:type} `COMPONENT` of all {l:components} also come equipped with some {p:properties}, which define some {l:component attributes}:

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

From the {l:functions over methods} philosophy of {l:typed}, such {p:attributes} can also be obtained from {l:typed functions}:

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

There are four main operations involving {l:components}:
1. `join: Prod(COMPONENT, n) -> COMPONENT`:
    - receives a tuple of components and creates a new component whose {l:jinja string} is the join of the {l:jinja strings} of the provided components;
2. `concat: Prod(COMPONENT(1), COMPONENT) -> COMPONENT`:
    - receives a component with a single {l:inner var} and another arbitrary component, producing a new component whose {l:jinja string} is obtained by replacing the placeholder given by {l:inner var} in the first component with the {l:jinja string} of the second component.
3. `eval: Prod(COMPONENT, Dict(Any)) -> COMPONENT`:
    - receives a {l:component} and a list with keys and values, returning the component obtained by fixing each variable associated to a _key_ with the corresponding _value_, leaving the other variables unchanged.
4. `copy: Prod(COMPONENT, Dict(Str)) -> COMPONENT`:
    - receives a {l:component} and a list with keys and values, returning a copy of the given component such that each parameter whose name is a key is renamed with the corresponding value, maintaining its type.

The intuition for each of such {l:component operations} is as follows:
1. `join`: put a component _after_ other component;
2. `concat`: put a component _inside_ other component;
3. `eval`: from a component, _fixes_ some part of it;
4. `copy`: from a component, _copy_ it.

So, for example, consider the following generic {l:components}:

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

Applying the {l:component join} to them we get a new {l:component} `join(some_comp, inner_comp)` which is equivalent to the following:

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

On the other hand, the {l:component concat} produces a {l:component} `concat(inner_comp, some_comp)` which is equivalent to:

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

Finally, `copy(inner_comp, {"inner": "other_name"})` produces the following {l:component}:

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

One should note that the {l:components} subject to the {l:component operations} could have overlapping {p:parameters}. About that, some remarks:

1. The {p:parameters} of the {l:component join} and the {l:component concat} are obtained from the union of tuple of {p:parameters} of the underlying {l:components}. This means that their multiplicity is not considered. More precisely, if components `comp_1` and `comp_2` share some parameter, then it will appear a single time in `join(comp_1, comp_2)` and in `concat(comp_1, comp_2)`.
2. If the shared parameters are of different {l:types}, a {p:type error} will be raised.

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

Then `join(comp_1, comp_3)` will raise a {p:type error}, while `join(comp_1, comp_2)` and `join(comp_2, comp_3)` will generate components equivalent to the following ones:

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

To avoid the overlapping behavior, you should make a {l:component copy} of some of the components before the {l:component join} and {l:component concat}, changing the name of the repeating {p:parameter}, as follows (this is precisely the typical use case of the {l:component copy} operation):

```python
from comp import copy
from some.where import comp_1, comp_2, comp_3

copied_2 = copy(comp_2, x="x_2")
copied_3 = copy(comp_2, x="x_3", y="y_3")
```

In this case, `join(comp_1, copied_2, copied_3)` has no overlapping, being equivalent to the following {l:component}:

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
