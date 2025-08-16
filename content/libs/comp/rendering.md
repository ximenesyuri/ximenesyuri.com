---
title: rendering
desc: rendering
weight: 30
---

# About

In this documentation we will discuss the _rendering process_ in the `app` component system.

```{toc}
```

# Review

Recall that the `app` component system is composed by _components_ which are entities of type `COMPONENT`. They are functions decorated with `@component` that receive arguments and return _jinja strings_, i.e, instances of `Jinja`. A component may have special variables, as `__depends_on__`.

# Rendering

After constructed, components can be _rendered_: the process of evaluating the component in a _context_, producing raw HTML. Technically, the render is implemented as a typed function (in the sense of {typed}) `render: Component x Context -> HTML`. 

```python
from app import render

html = render(my_comp, <context>)
```

# Context

The `Context` type is a representation of `Dict(Any)`, meaning that it is a dictionary with key and values. Typically, one pass this dictionary to the `render` function as _keyword arguments_:

```python
from app import render

html = render(
    my_comp,
    some_var=some_value,
    other_var=other_value,
    ...
)
```

In the rendering process, the context should contains at least the _jinja vars_ in the returning _jinja string_ of the component to be rendered. Some data, however, is automatically included in the context:
1. local variables
2. depending components in the `__depends_on__` variable. 

In practical terms, rendering a component is similarly to using `eval` operation applied to all variables of a component, followed by a `jinja` renderization. This means that if `some_var` is a variable of some component `my_comp`, then to render `my_comp` we need to pass `some_var` with some value:

```python
from typed import SomeType
from app import component, Jinja, render

@component
def my_comp(some_var: SomeType, ...) -> Jinja:
    ...
    return """jinja
    ....
"""

html = render(my_comp, some_var=some_value, ...)
```

> We note that, if in the definition of `my_comp` the variable `some_var` has a default value, it is used in `render` if the variable is omitted.
 
# Minify 

The `render` function has certain special variables, as we pass to discuss. The first of those variables in `__minify__`. It is a boolean variable with default value to `False`. If set to `True`, the obtained HTML is returned compacted.

So, if you want to produce compacted HTML, just use:

```python
from app import render

html = render(my_comp, <context_vars>, __minify__=True)
```

# Scripts

In the sequence, we have the variable `__scripts__` of type `List(Script)`. It should be used to append a component with certain auxiliary scripts. The `Script` model has a mandatory attribute `script_src` which defines its origin.

The attribute `script_src` is of type `Union(Extension('js'), Url('http', 'https')`, which means that it accepts both:
1. a `http` or `https` url
2. a path to some `.js` file.

If in `__script__` it is passed a script object with `script_src` given by a url, then, during the rendering, the component is appended with the builtin `script` component applied the given script object. On the other hand, if the script object contains a `script_src` which is the path to a `.js` file, then the content of the file is added to the component inside a `<script>` block.

So, for example, suppose you need to incorporate a script located in the url `https://my_script_url.com` to a component `my_comp`. All you need to do is:

```python
from app import render
from app.models import Script

my_script = Script(
    script_src="https://my_script_url.com",
    script_defer=True,
    ...
)

html = render(my_comp, <context_vars>, __scripts__=[my_script])
```

# Assets

# Extensions

# Style
