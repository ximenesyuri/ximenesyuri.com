---
title: overview
weight: 1
---

# About

Here you will find an overview for the {l:comp} library.

```{toc}
```

# Overview: Components

The lib {l:comp} deals with _components_. These are {l:typed functions} (in the sense of {l:typed}) which return _jinja strings_, i.e, Python strings of type `Jinja`, which contain {jinja2} syntax. Components should also be defined using the `@component` decorator.

The typical way to define a {l:component} is to first define a {l:model} (in the sense of {l:typed}, typically a {l:optional model}) containing the _structure_ of the {l:component}, and then take this model as argument:

```python
from typed import optional, null, SomeType, OtherType
from comp import component

@optional
class MyModel:
    some_var:  SomeType=null(SomeType)
    other_var: OtherType=null(OtherType)
    ...

@component
def my_comp(my_comp: MyModel) -> Jinja:
    ...
    return """jinja
    ...
"""
```

Components define a {l:type} `COMPONENT` and there are four main {l:component operations} between them, each of them corresponding to an arithmetic symbol ({p:magic methods} in Python):

(table-1)=
```
operation      symbol    description
-------------------------------------------------------------------
join             +       join the jinja strings of the components
concat           *       put a jinja string inside the other
eval             /       fixes some arguments
copy             ^       copy a component, eventually changing var names
-----------------------------
table 1: component operations
```

This means that we can construct complex {l:components} through _component equations_:

```python
my_comp = (
    (comp_1 * comp_2) +
    (comp_3 / {'some_var': some_value})
) ^ {"some_var": new_name}
```

(rem-1)=
> [Remark 1](#rem-1). The modules `comp.models` and `comp.components` provides, respectively, a plethora of already defined {l:models} and corresponding {l:components}, one for each builtin HTML tag.

# Overview: Special Vars

A {l:component} have certain _special vars_:
1. `__context__`: defines the {l:local context} of the component, where needed information to {l:render} it is introduced (see [below](#overview-rendering));
2. vars of type `Inner`: used as placeholder to introduced content of other components;
3. vars of type `Content`: receive _static context_ in the form of Markdown or ReStructuredText.

For example, {l:inner vars} are used in the {l:component concat} operation, while {l:content vars} allows the use of {l:comp} in both dynamic and static environments.

# Overview: Rendering

After being constructed, {l:components} can be _rendered_, producing raw HTML. This is done using a {l:typed function} `render`:

```python
from comp import render

html = render(my_comp, **context)
```

To {l:render} a component one needs to pass a _context_, which is a {p:dictionary}. It attaches values to each argument of the component, as well as to other {l:free variables}.

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

# Other Docs

```{toc-dir}
```
