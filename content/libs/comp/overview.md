---
title: overview
weight: 1
---

# About

Here you will find an overview for the {lib:comp} library.

```{toc}
```

# Overview: Components

The lib {lib:comp} deals with _components_. These are {lib:typed functions} (in the sense of {lib:typed}) which return _jinja strings_, i.e, Python strings of type `Jinja`, which contain {jinja2} syntax. Components should also be defined using the `@component` decorator.

The typical way to define a {lib:component} is to first define a {lib:model} (in the sense of {lib:typed}, typically a {lib:optional model}) containing the _structure_ of the {lib:component}, and then take this model as argument:

```python
from typed import optional, null, SomeType, OtherType
from comp import component

@optional
class MyModelib:
    some_var:  SomeType=null(SomeType)
    other_var: OtherType=null(OtherType)
    ...

@component
def my_comp(my_compy: MyModel) -> Jinja:
    ...
    return """jinja
    ...
"""
```

Components define a {lib:type} `COMPONENT` and there are four main {lib:component operations} between them, each of them corresponding to an arithmetic symbol ({py:magic methods} in Python):

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

This means that we can construct complex {lib:components} through _component equations_:

```python
my_comp = (
    (comp_1 * comp_2) +
    (comp_3 / {'some_var': some_value})
) ^ {"some_var": new_name}
```

(rem-1)=
> [Remark 1](#rem-1). The modules `comp.models` and `comp.components` provides, respectively, a plethora of already defined {lib:models} and corresponding {lib:components}, one for each builtin HTML tag.

# Overview: Special Vars

A {lib:component} have certain _special vars_:
1. `__context__`: defines the {lib:local context} of the component, where needed information to {lib:render} it is introduced (see [below](#overview-rendering));
2. vars of type `Inner`: used as placeholder to introduced content of other components;
3. vars of type `Content`: receive _static context_ in the form of Markdown or ReStructuredText.

For example, {lib:inner vars} are used in the {lib:component concat} operation, while {lib:content vars} allows the use of {lib:comp} in both dynamic and static environments.

# Overview: Rendering

After being constructed, {lib:components} can be _rendered_, producing raw HTML. This is done using a {lib:typed function} `render`:

```python
from comp import render

html = render(my_comp, **context)
```

To {lib:render} a component one needs to pass a _context_, which is a {py:dictionary}. It attaches values to each argument of the component, as well as to other {lib:free variables}.

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
