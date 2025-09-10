---
title: styles
weight: 60
---

# About

In this documentation we describe the styles that can be used in a {lib:component}, which are automatically converted to `css` classes during the {lib:rendering} process if the flag `__styled__` is set to `True`.

```{toc}
```

# Introduction

In `css`, _classes_ are composed of _properties_. To define a property one needs to set a `<value>`, which typically depends on some `<unit>` and can be endowed with further `<styles>`. So, in `css`  a _class_ can be typically defined as dictionary whose entries are _properties_. These, in turn, have values given by dictionaries with keys  `value`, `unit` and `styles`, as follows:

```python
some_class = {
    "some_property": {
        "value": some_value,
        "unit": some_unit,
        "styles": [style_1, style_2, ...]
    },
    "other_property": {
        "value": other_value,
        "unit": other_unit,
        "styles": [style_A, style_B, ...]
    },
    ...

}
```

You could try to incorporate all this information into a single string. In other words, one could try to consider strings representing the content of css classes, which could be used in the "class-like" attributes of {lib:components}: the so-called {lib:style strings}.

This would allow us to create an inline `css` framework for {lib:comp}, in which {lib:style strings} inside a {lib:component}, named as above, are automatically converted to underlying `css` classes, so that their content would be introduced in a `<style>` tag in the {lib:rendered HTML} obtained from {lib:rendering} the given {lib:component}.

In the following we brief describe how this framework works, whose execution is controlled by the {lib: rendering flag} `__styled__`.

# Single Properties

Let us first consider the case of a class with a single property:

```python
some_class = {
    "property": {
        "value": some_value,
        "unit": some_unit,
        "styles": [style_1, style_2, ...]
    }
}
```

Its content can be naturally represented by the following string, which will work as a {lib:style string} for the underlying {lib:style property}:

```
<property>-<value><unit>-<style_1>-<style_2>-...
```

Indeed, suppose we have a {lib:component} `some_comp`, defined as follows:

```python
from typed import optional, Str
from comp import component, Jinja

@optional
class SomeModel:
    comp_id: Str,
    comp_class: Str,
    ...

@component
def some_comp(comp: SomeModel, ...) -> Jinja:
    ...
```

Then, suppose we created an instance of `comp` with `comp_class` containing the {lib:style string}:

```python
some_entity = SomeModel(
    comp_id = "some_id",
    comp_class = "<property>-<value><unit>-<style_1>-<style_2>-...",
    ...
)
```

In this case, `render(some_comp, comp=some_entity, __styled__=True)` will produce an HTML which begins with the following `<style>` tag:

```html
<style>
    [property]-[value][unit]-[style_1]-[style-2]-... {
        [property]: [value][unit] [style_1] [style_2] ...;
    }
    ...
</style>
...
```

For example, if `comp_class = 'margin-top-10px'`, then the following will be added to the  {lib:rendered HTML}:

```html
<style>
    margin-top-10px {
        margin-top: 10px;
    }
    ...
</style>
...
```

# Multiple Properties

For the case of classes with multiple properties, one could try to use the same structure. Indeed, for a class like

```python
some_class = {
    "property_1": {
        "value": value_1,
        "unit": unit_1,
        "styles": [style_1_1, style_1_2, ...]
    },
    "property_2": {
        "value": value_2,
        "unit": unit_2,
        "styles": [style_2_1, style_2_2, ...]
    },
    ...
}
```

one could think in using:

```
(<property_1>-<value_1><unit_1>-<style_1_1>-<style_1_2>)-(<property_2>-<value_2><unit_2>-<style_2_1>-<style_2_2>)-...
```

However, notice that this becomes highly understandable when the number of property grows. At the same time, it is completely flexible, in the sense that you can control any parameter of any property of the class directly in the representing string.

The majority of the classes described by {lib:style strings} will correspond to a single property, so that the first case will apply.

# Aliases

When doing inline css, it is common to use abbreviations. To each property included in the 


(notation-1)=
> [Notation](#notation-1). In the following:
> 1. `<x>` represents a possible value in the `values` column
> 2. `<u>` represents a possible value in the `unities` column
> 3. `<s>` represents a possible value in the `styles` column


# Styles: display

(table-1)=
```
property           inline          aliases      
--------------------------------------------------------------
display            inline          inl
display            block           blk
display            table           tab
display            flex            flx
display            inline-block    inl-blk
display            inline-flex     inl-flx
--------------------------------------------------------------
table 1: display styles
```

# Styles: space

(table-2)=
```
property               inline                    aliases       values            unities
------------------------------------------------------------------------------------------------------
margin                 margin-<x><u>             m             Int               (px, em, rem, vh, vw, %)
margin-top             margin-top-<x><u>         mt            Int               (px, em, rem, vh, vw, %)
margin-bottom          margin-bottom-<x><u>      mb            Int               (px, em, rem, vh, vw, %)
margin-left            margin-left-<x><u>        ml            Int               (px, em, rem, vh, vw, %)
margin-right           margin-right-<x><u>       mr            Int               (px, em, rem, vh, vw, %)
padding                padding-<x><u>            p             Int > 0           (px, em, rem, vh, vw, %)
padding-top            padding-top-<x><u>        pt            Int > 0           (px, em, rem, vh, vw, %)
padding-bottom         padding-bottom-<x><u>     pb            Int > 0           (px, em, rem, vh, vw, %)
padding-left           ppadding-left-<x><u>      pl            Int > 0           (px, em, rem, vh, vw, %)
padding-right          padding-right-<x><u>      pr            Int > 0           (px, em, rem, vh, vw, %)
gap                    gap-<x><u>                ---           Int > 0           (px, em, rem, vh, vw, %)
------------------------------------------------------------------------------------------------------
table 2: spacing styles
```

# Styles: size

(table-3)=
```
property              inline                 aliases      values          unitites
------------------------------------------------------------------------------------------------
width                 width-<x><u>           w            Int > 0         (px, em, rem, vh, vw, %)
min-width             min-width-<x><u>       mw           Int > 0         (px, em, rem, vh, vw, %)
max-width             max-width-<x><u>       Mw           Int > 0         (px, em, rem, vh, vw, %)
height                height-<x><u>          h            Int > 0         (px, em, rem, vh, vw, %)
min-height            min-height-<x><u>      mh           Int > 0         (px, em, rem, vh, vw, %)
max-height            max-height-<x><u>      Mh           Int > 0         (px, em, rem, vh, vw, %)
----------------------------------------------------------------------------------------------
table 3: sizing styles
```

# Styles: border

(table-4)=
```
property                   inline                        aliases        values      unities              styles
----------------------------------------------------------------------------------------------------------------------------
border-top                 border-top-<x><u>-<s>         bt             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-bottom              border-bottom-<x><u>-<s>      bb             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-right               border-right-<x><u>-<s>       br             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-left                border-left-<x><u>-<s>        bl             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-radius              border-radius-<x><u>          bR, radius     Int > 0
-----------------------------------------------------------------------------------------------------------------------------
table 4: border styles
```

(table-5)=
```
property
-----------------------------

-----------------------------
table 5: 
```

# Other Docs

```{toc-dir}
```
