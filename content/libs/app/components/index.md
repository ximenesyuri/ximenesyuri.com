---
title: component system
desc: overview
weight: 10
---

# About

Here you will find documentations on the _component system_ of the {app} library.

```{toc}
```

# Overview: Components

The component system of {app} deals with _components_. These are typed functions (in the sense of {typed}) which returns _jinja strings_, i.e, Python strings of type `Jinja`, which contains {jinja2} syntax. Components should also be defined using the `@component` decorator.

The typical way to define a component is to first define a model (in the sense of {typed}) containing the _structure_ of the component, and then take this model as argument:

```python
from typed import null, SomeType, OtherType
from typed.models import model
from app import component

@model
class MyModel:
    some_var: Optional(SomeType, null(SomeType))
    other_var: Optional(OtherType, null(OtherType))
    ...

@component
def my_comp(my_comp: MyModel) -> Jinja:
    ...
    return """jinja
    ...
"""
```

Components define a type `COMPONENT` and there are three main operations between them, each of them corresponding to an arithmetic symbol:

(table-1)=
```
operation      symbol    description
-------------------------------------------------------------------
join             +       join the jinja strings of the components
concat           *       put a jinja string inside the other
eval             /       fixes some arguments
-----------------------------
table 1: component operations
```

This means that we can construct complex components through _component equations_:

```python
my_comp = (
    (comp_1 * comp_2) +
    (comp_3 / {'some_var': some_value})
) / {"other_var": other_value}
```

(rem-1)=
> [Remark 1](#rem-1). The modules `app.models` and `app.components` provides, respectively, a plethora of already defined models and corresponding components, one for each builtin HTML tag.

# Overview: Rendering

After being constructed, components can be _rendered_, producing raw HTML. This is done using a typed function `render`:

```python
from app import render

html = render(my_comp, **context)
```

To render a component one needs to pass a _context_, which is a dictionary. It attaches values to each argument of the component, as well as to other "free variables".

The rendering process can be customized to produce optimized raw HTML by passing certain special variables to `render`:

(table-1)=
```
argument          type            description
-------------------------------------------------------------------
__minified__      Bool            return minified HTML
__styled__        Bool            auto-generate <style> for inline classes
__scripts__       List(Script)    include given script data in the HTML
__assets__        List(Asset)     include given asset data in the HTML
-----------------------------
table 1: render variables
```

(rem-2)=
> [Remark 2](#rem-2). During the construction of a component you can preview it using the `preview` function, which renders the component and creates a server that looks automatically for updates in the component file. 

# Overview: Statics

... TBA ...

# Docs

```{toc-dir}
```
