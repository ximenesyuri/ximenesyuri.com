---
title: components
desc: components
weight: 10
---

# About

In the following we will briefly describe how the _components_ in `app` component system work.

```{toc}
```

# Jinja Strings

The component system of `app` is based in {jinja2}. This means that the components constructs strings following {jinja2} syntax. We have a specific type `Jinja` (which is a subtype of `Str`) whose instances are the so-called _jinja strings_: Python strings preppended with the "`jinja`" keyword.

So, more precisely, an instance of `Jinja` is a string as follows (see {jinja2} to discover the full valid syntax):

```python
my_jinja_string = """jinja
{% for i in x %}
<some html>
    {% if y is True %}
    <more html>
    ...
    </more html>
    {% endif %}
</some html>
{% endfor %}
"""
```

Above, `x` and `y` are _jinja variables_, which must be defined inside some _context_, for example as part of a component, before converting the _jinja string_ to HTML (see the [rendering](./3-rendering) documentation). 

# Components

The basic unities of `app` component systems are, of course, the _components_. A _component_ is a typed function (in the sense of {typed}) such that:
1. it returns a _jinja string_, so that its returning type is the `Jinja` type;
2. it is decorated with the `@component` decorator.

Thus, a typical component is defined as follows:

```python
from typed import SomeType, OtherType
from app import component, Jinja

@component
def my_comp(x: SomeType, y: OtherType, ...) -> Jinja:
    ...
    return """jinja
{% for i in x %}
<some html>
    {% if y is True %}
    <more html>
    ...
    </more html>
    {% endif %}
</some html>
{% endfor %}
"""
```

One should note that local variables of a component are automatically included in the context of the returning jinja string. This means that _local variables_ defined in the body of a component can be directly used as _jinja vars_:

```python
from typed import SomeType, OtherType
from app import component, Jinja

@component
def my_comp(x: SomeType, y: OtherType, ...) -> Jinja:
    ...
    some_var = some_value
    ...
    return """jinja
{% for i in x %}
<some html>
    {% if y is True %}
    <more html>
        {{ some_var }}
    </more html>
    {% endif %}
</some html>
{% endfor %}
"""
```

(rem-1)=
> [Remark 1](#rem-1). There is the type `COMPONENT` whose instances are precisely the `app` components. It is constructed as a subtype of `TypedFunc(Any, cod=Jinja)`, i.e., of all typed functions whose codomain is `Jinja`.  

# Tags
      
Typically, components are delimited by a HTML tag. In `app` there is a _type factory_ (in the sense of {typed})  `Tag: Tuple(Str) -> SUB(Jinja)` that receives a tuple of HTML tag names and returns the subtype `Tag(*tags)` of `Jinja` of all _jinja strings_ enclosed by one of the given tags.

```python
# example of instance of 'Tag('some-tag')'
"""jinja
<some-tag>
...
</some-tag>
"""
```

With such type factory one can construct type safe tag-based components:

```python
from app import component, Tag

@component
def my_tag_comp(...) -> Tag('some-tag'):
    ...
    return """jinja
<some-tag>
...
</some-tag>
"""
```

For each tuple of tags there is a subtype `TAG(*tags)` of `COMPONENT` of all components whose returning string belongs to `Tag(*tags)`. There is, actually, a supplementary type factory `TAG: Tuple(Str) -> SUB(COMPONENT)` that associates to each tuple the corresponding type `TAG(*tags)`.

So, for the component `my_tag_comp` above:

```python
from app import TAG

# the following returns True
print(isinstance(my_tag_comp, TAG('some-tag')))
```

# Dependences
  
Components can depend one each others. More precisely, a component has a special optional variable `__depends_on__`, which lists other already defined components of which the defining component depends on. 

One time listed in the `__depends_on__` variable, the dependent components are included into the context, so that they are turned into _jinja vars_ and can be called inside the _jinja string_ of the defining component, as follows:

```python
from app import Jinja, Tag, component

@component
def comp_1(...) -> Jinja:
    ...
    return """jinja
    ...
"""

@component
def comp_2(...) -> Tag('some-tag'):
    ...
    return """jinja
<some-tag>
    ...
</some-tag>
"""

@component
def main_comp(..., __depends_on__=[comp_1, comp_2]) -> Jinja:
    ...
    return """jinja
    ...
{{ comp_1(...) }}
    ...
{{ comp_2(...) }}
"""
```

> Recall that components are _typed functions_, which means that all their arguments must have type annotations, which are checked at runtime. The `__depends_on__`, however, is an exception: if a type annotation is _not_ provided, then `List(COMPONENT)` is automatically attached to it. On the other hand, if a type annotation is provided, it must be a subtype of `List(COMPONENT)`.

# Free Variables

When a _jinja var_ is in the _jinja string_ returned by a component, it typically corresponds to one of the following cases:

1. it is component argument;
2. it is a local variable defined in the body of the component;
3. it is another component listed in the `__depends_on__` argument.

A _jinja var_ which does not satisfies some of the conditions above is called a _free jinja var_.

(rem-2)=
> [Remark 2](#rem-2). It is _not_ a best practice to have _free jinja vars_ in a component. Indeed, as will de discussed in [Rendering](./3-rendering), a free jinja var need to be explicitly included in the context during the rendering of a context. The problem is that, unlike component arguments, they are not true Python components, which makes difficult to remember their existence.  
   
# Inners
    
In `app`, the components may have another special kind of variables: the _inner_ ones. They are necessarily of type `Inner`, and work as placeholders for future inserts inside the component.

(inner-comp)=
```python
from app import component, Tag, Inner

@component
def my_inner_comp(..., inner: Inner, ...) -> Tag('some-tag'):
    ...
    return """jinja
<some-tag>
    {{ inner }}
</some-tag>
"""
```

The type `Inner` is a presentation of the `Jinja` type.  

> The components may also admit _content vars_ (of type `Content`), characterizing them as _static components_, which can be used to introduced `Markdown` and `RST` content inside the component. This will be discussed in [Statics](./4-statics). 

# Component Factory

There is a type factory `Component: Int -> SUB(COMPONENT)` that to each integer `n>=0` returns the subtype `Component(n)` of `COMPONENT` of all components that have exactly `n` inner vars.

This decomposes the type `COMPONENT` into distinct subtypes of components with a fixed amount of `inner` variables.

So, for example, for the `my_inner_comp` defined [above](#inner-comp) one would have: 

```python
from app import Component

print(isinstance(my_inner_comp, Component(1)) # will return 'True'
print(isinstance(my_inner_comp, Component(0)) # will return 'False' 
```

> By definition, if `n<0`, then `Component(n)` is set precisely to `COMPONENT`, meaning that the component may have any number of `inner` variables, including zero.

# Attributes

The type `COMPONENT` of all components has some properties, which define some attributes to the components:

(table-1)=
```
attribute           description 
-----------------------------
.jinja              code of the component _jinja string_
.jinja_vars         tuple of _jinja vars_
.jinja_free_vars    tuple of _jinja free vars_
.inner_args         tuple of _inner args_
.content_args       tuple of _content_args_
.tags               the tuple of tags that defines the component 
-----------------------------
table 1: component attributes
```

# Operations

There are three main operations involving components:
1. `join: COMPONENT x COMPONENT -> COMPONENT`:
    - receive a tuple of components and creates a new component whose _jinja string_ is the join of the _jinja strings_ of the provided components;
2. `concat: Component(1) x COMPONENT -> COMPONENT`:
    - receive a component with a single _inner var_ and another arbitrary component, producing a new component whose _jinja str_ is obtained by replacing the placeholder given by _inner var_ in the first component with the _jinja string_ of the second component.
3. `eval: COMPONENT x Dict(Any) -> COMPONENT`:
    - receive a component and a list of key-values and returns the component obtained by fixing each variable associated to a _key_ with the corresponding _value_, leaving the other variables unchanged.

The intuition for each of such operations is as follows:
1. `join`: put a component _after_ other component
2. `concat`: put a component _inside_ other component
3. `eval`: from a component, _fixes_ some part

So, for example, consider the following generic components:

```python
from typed import SomeType, OtherType
from app import Jinja, component, Tag, Inner, join, concat, eval

@component
def some_comp(x: SomeType, ...) -> Jinja
    ...
    return """jinja
{{ contents of 'some_comp' jinja string }}
"""

@component
def inner_comp(a: OtherType, inner: Inner, ...) -> Tag('some-tag')
    ...
    return """jinja
<some-tag>
    {{ inner }}
</some-tag>
"""
```

The resulting joined component `join(some_comp, inner_comp)` is equivalent to the following component:

```python
@component
def joined_comp(x: SomeType, ..., a: OtherType, inner: Inner, ...) -> Jinja:
    return """jinja
{{ contents of 'some_comp' jinja string }}
<some-tag>
    {{ inner }}
</some-tag>
"""
```

On the other hand, `concat(inner_comp, some_comp)` is equivalent to:

```python
@component
def concat_comp(a: OtherType, x: SomeType, ...) -> Tag('some-tag'):
    return """jinja
<some-tag>
    {{ contents of 'some_comp' jinja string }}
</some-tag>
"""
```

Finally, `eval(inner_comp, inner="blablabla")` is the same as defining the component below.

```python
@component
def eval_comp(a: OtherType, ...) -> Tag('some-tag'):
    return """jinja
<some-tag>
    blablabla
</some-tag>
"""
```

> In both `join` and `concat` operations, the `__depends_on__` variable is the obtained as the concatenation of the `__depends_on__` of the underlying components. In the `eval` operation, on the other hand, the `__depends_on__` is maintained the same.

# Arithmetic

In the type `COMPONENT`, the operations `join` and `concat` corresponds, respectively to implementations of the class functions `__sum__` and `__mul__`. This means that instead of writing `join(comp_1, comp_2)` you can just write `comp_1 + comp_2`. Similarly, instead of `concat(comp_1, comp_2)`, you can write `comp_1 * comp_2`.

Therefore, the `COMPONENT` type has an internal "component arithmetic" that can be used to build complex components from smaller ones.

# Other Docs

```{toc-dir}
```
