---
title: models
desc: models
---

```{title}
```

# About

In this documentation we described the use of _models_ in the `app` component system.

```{toc}
```

# Review

Recall that in the `app` component system, a _component_ is a typed function (in the sense of {typed}) such that:
1. it returns a _jinja string_, i.e, its codomain is a subtype of `Jinja`;
2. it is decorated with the `@component` decorator.

A component may contains certain _special variables_, as:
1. the `__depends_on__` variable, which lists the components that a defining component depends on;
2. the _inner vars_, which are variables of type `Inner`
2. the _content vars_, which are variables of type `Content` (these will be discussed in [Statics](./4-statics)).

# Models

By definition, there is no restriction on the _domain_ of a component, except by the fact that it can contains certain special variables, as described above. This means that the "typical variables" may have any type.
 
However, a better way to organize the components is to work with _models_ (in the sense of {typed}), grouping the "typical variables" in a more semantic entity.

So, for example, consider the following component:

```python
from typed import SomeType, OtherType
from app import component, Jinja

@component
def my_comp(some_var: SomeType,  other_var: OtherType, ...) -> Jinja:
    return """jinja
    ...
"""
```

You could join `some_var` and `other_var` into a single entity (for full details on using models, see {typed/models}):
    
```python
from typed import SomeType, OtherType, ...
from typed.models import model, Optional

@model
class MyComp:
    some_var:  Optional(SomeType, SomeType())
    other_var: Optional(OtherType, OtherType())
    ...
```

Then, one could rewrite `my_comp`  as follows:

```python
from app import component, Jinja
from some.where import MyComp

@component
def my_comp(my_comp: MyComp, ...) -> Jinja:
    return """jinja
    ...
"""
```

(rem-1)=
> [Remark 1](#rem-1). The recommendation is to create models with the decorator `@model` and all variables being `Optional` (in the sense of {typed/models}). This will allow more flexibility in the rendering of the component, as described in [Rendering](./3-rendering), without breaking type safety. However, you are free to create the models as you want, say using more rigid decorators, as `@exact`, `@ordered` and `@rigid`, or avoiding `Optional` arguments.

# Accessing Values

To each internal variable of a _model_ there corresponds a namesake attribute. This means that if `SomeModel` is a model with a variable `some_var` and if `model: SomeModel` is a variable of type `SomeModel`, you could access the values `some_var` as `model.some_var`.

In terms of the component `my_comp` defined above, one could then access `my_comp.some_var` and `my_comp.other_var` in the _body_ of the component function, i.e, as _local variables_:

```python
from app import component, Jinja
from some.where import MyComp

@component
def my_comp(my_comp: MyComp, ...) -> Jinja:
    some_value  = my_comp.some_var
    other_value = my_comp.other_var
    ...
    return """jinja
    ...
"""
```

In this case, since local variables of components are automatically added to context of the component, `some_value` and `other_value` could then be used inside the returning _jinja string_:

```python
from app import component, Jinja
from some.where import MyComp

@component
def my_comp(my_comp: MyComp, ...) -> Jinja:
    some_value  = my_comp.some_var
    other_value = my_comp.other_var
    ...
    return """jinja
    ...
    {{ some_value }}
    ...
    {{ other_value }}
    ...
"""
```

The remarkable point here is that, in the construction of the `@component` decorator, if a variable is defined with type being a model, then all attributes are directly added in the context as well. Therefore, you could use `my_comp.some_var`, etc, directly inside the _jinja string_:

```python
from app import component, Jinja
from some.where import MyComp

@component
def my_comp(my_comp: MyComp, ...) -> Jinja:
    ...
    return """jinja
    ...
    {{ my_comp.some_var }}
    ...
    {{ my_comp.other_var }}
    ...
"""
```

# Builtins Models

Inside the module `app.models` you will encounter a plethora of ready to use models, one for each basic HTML tag.

(table-1)=
```
model       tag
--------------------------------
Div         <div>
Text        <p>
Title       <h1>, <h2>, ... <h6>
Link        <a>
Image       <img>
Figure      <figure>
Button      <button>
Script      <script>
Asset       <link>
...
-------------------------------
table 1
```

The attributes of the builtin models correspond to (mostly of) the {HTML tag attributes} of the underlying HTML tags. There is also a `Globals` model, which contains the {HTML global attributes}, which are shared across all HTML tags. 

The global attributes can be accessed in each builtin model from a `globals` variable. The only exception are the global attributes `id` and `class`, which appears as independent variables inside each model, named according to the tag name:

(table-2)=
```
model       tag                       attributes
-----------------------------------------------------------------------    
Div         <div>                     div_id, div_class, ...
Text        <p>                       text_id, text_class, ...
Title       <h1>, <h2>, ... <h6>      title_id, title_class, ...
Link        <a>                       link_id, link_class,  ...
Image       <img>                     img_id, img_class, ...
...
-------------------------------------------------------------------------
table 2
```

# Model Components

To each _builtin model_, say associated with a tag `model-tag`, there corresponds a namesake _builtin component_, which has a namesake variable of the given model type, and eventually a single _inner var_, maybe depending on others builtin components. These are the so-called _model components_.

(table-3)=
```
model       component
--------------------------------
Div         div
Text        text
Title       title
Link        link
Image       img
Figure      figure
Button      button
Script      script
Asset       asset
...
-------------------------------
table 3: model components
```

So, the generic structure of a _model component_ is as follows:

```python
from app import component
from app.models import SomeModel

@component
def some_model(some_model: SomeModel=SomeModel(), inner: Inner=Inner(), __depends_on__=[...]) -> Tag('model-tag'):
    ...
    return """
<model-tag>
    ...
    {{ inner }}
    ...
</model-tag>
"""
```

Actually, the `<model-tag>` in a _model component_ is dynamically constructed with all attributes of the model `SomeModel` that are not null in the instance `some_model`. So, for example, if `some_model.some_attr` is set to `some_value`, then it will appear in the returning _jinja string_:

```python
@component
def some_model(some_model: SomeModel=SomeModel(), inner: Inner=Inner(), __depends_on__=[...]) -> Tag('model-tag'):
    ...
    return """
<model-tag some_attr="some_value">
    ...
    {{ inner }}
    ...
</model-tag>
"""
```

Otherwise, i.e, if `some_model.some_attr` is not set, then the  field `some_attr` is _not_ included in the returning `<model-tag>`, turning the code much more clean.

> This happens because the _jinja string_ of a model component is constructed with the help of `if_` helper functions from `app.helper`. 

# Constructing

Recall that there are certain operations in the type `COMPONENT` of all components:
1. `join`: corresponding to `+`;
2. `concat`: corresponding `*`;
3. `eval`: corresponding `/`.

Using the builtin _model components_ and the operations above, you can build derived components very quickly. For instance, suppose you want to build a `div` with a title followed by a paragraph. You can just take:

```python
from app.components import div, title, text

my_comp = div * (title + text)
```

The obtained component have the variables `div: Div`, `title: Title` and `text: Text`, whose attributes can then be fixed to produce concrete instances of `my_comp`.

# Other Docs

```{toc-dir}
```
