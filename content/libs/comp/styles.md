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

# Property Strings

The vast majority of `css` classes incorporated in the framework have a single property:

```python
some_class = {
    "property": {
        "value": some_value,
        "unit": some_unit,
        "styles": [style_1, style_2, ...]
    }
}
```

Its content can be naturally represented by the following string, which works as a {lib:style string} for the underlying {lib:style property}:

```
<property>-<value><unit>-<style_1>-<style_2>-...
```

Indeed, suppose we have a {lib:component} `some_comp`, defined as follows:

```python
from typed import optional, Str
from comp import component, Jinja

@optional
class SomeCompModel:
    comp_id: Str,
    comp_class: Str,
    ...

@component
def some_comp(comp: SomeModel, ...) -> Jinja:
    ...
```

Then, suppose we created an instance of `comp` with `comp_class` containing the {lib:style string}:

```python
some_entity = SomeCompModel(
    comp_id = "some_id",
    comp_class = "<property>-<value><unit>-<style_1>-<style_2>-...",
    ...
)
```

In this case, `render(some_comp, comp=some_entity, __styled__=True)` will produce an HTML which begins with the following `<style>` tag:

```html
<style>
    .[property]-[value][unit]-[style_1]-[style-2]-... {
        [property]: [value][unit] [style_1] [style_2] ...;
    }
    ...
</style>
...
```

For example, if `comp_class = 'margin-top-10px'`, then the following will be added to the  {lib:rendered HTML}:

```html
<style>
    .margin-top-10px {
        margin-top: 10px;
    }
    ...
</style>
...
```

# Class Strings

A few `css` classes with multiples properties are available as {lib:style strings}. Instead of using the same strategy above to build them, which would become highly understandable with the increasing of the number of properties, for that cases we select a word to represent the entire class:

```
<word>-<value_1><unit_1>-<value_2><unit_2>-...
```

For example, if in `some_entity` of `SomeCompModel` we set `comp_class = 'left-10px'`, representing a left alignment with a padding of `10px`, then the following will be attached to the {lib:rendered HTML}:

```html
<style>
    .left-10px {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        padding-left: 10px;
    }
</style>
```

# Aliases

To each {lib:style string} representing a `css` class there corresponds a number of other {lib:style strings} that represents the same `css` class: the so-called {lib:style aliases}. The idea is to cover most of the user expected behavior.

For the case of {lib:style strings} associated with some {lib:style property}, the alias is of the property. On the other hand, for {lib:style strings} representing classes with multiple properties, the alias is of the word describing the class.

For instance:

1. instead of `margin-top-10px` one could use `mt-10px`
2. instead of `left-10px` one could use `lft-10px` or just `l-10px`, or even `left-center-10px`, `lft-cnt-10px`, `l-c-10px` or `lc-10px`.

# Prefixes

One time constructed a {lib:style string}, one can append it with a {lib:style prefix}, producing a new {lib:style string} which works only inside a specific {lib:style scope}.

# Notation

In the remaining part of this document we present the acceptable {lib:style strings}, their underlying {lib:style property} (if any), their meaning, their {lib:style aliases} and the available {lib:style prefixes}.

In order to do that we will use the following notations:

(notation-1)=
> [Notation](#notation-1).
> 1. `<x>` will represent a possible value in the `values` column
> 2. `<u>` will represent a possible value in the `unities` column
> 3. `<s>` will represent a possible value in the `styles` column

Also, the variables `<x>`, `<u>` and `<s>` will be omitted in the `aliases` column.

# Styles: display

(table-1)=
```
property           style string                 aliases      
------------------------------------------------------------------------------------------------------
display            display-none                 d-none, none
display            display-grid                 d-none, grid
display            display-inline               d-inline, d-inl, inline, inl
display            display-block                d-block, d-blk, block, blk
display            display-table                d-table d-tab, table, tab
display            display-flex                 d-flex, d-flx, flex, flx
display            display-inline-block         d-inline-block, d-inl-blk, inline-block, inl-blk
display            display-inline-flex          d-inline-flex, d-inl-flx, inline-flex, inl-flx
------------------------------------------------------------------------------------------------------
table 1: display styles
```

# Styles: position

(table-2)=
```
property         style string           aliases 
--------------------------------------------------------------
position         position-fixed         pos-fixed, pos-fix
position         position-relative      pos-relative, pos-rel
position         position-absolute      pos-absolute, pos-abs
position         position-sticky        pos-sticky, pos-stk
---------------------------------------------------------------
table 2: position styles
```

# Styles: float

(table-3)=
```
property           style string           aliases
--------------------------------------------------------------
float              float-left             flt-lft
float              float-right            flt-rgt
float              float-inline-start     flt-inl-st
float              float-inline-end       flt-inl-end
---------------------------------------------------------------
table 3: float styles
```

# Styles: align

(table-3)=
```
property           style string           aliases 
--------------------------------------------------------------
justify-items      position-fixed         pos-fixed, pos-fix
position           position-relative      pos-relative, pos-rel
position           position-absolute      pos-absolute, pos-abs
position           position-sticky        pos-sticky, pos-stk
---------------------------------------------------------------
table 3: align styles
```

# Styles: flex

(table-2)=
```
description                      style string               aliases                                                    values       unities
-------------------------------------------------------------------------------------------------------------------------------------------------------------
centered                         flex-center                flx-center, flx-cnt, center, cnt, c                        ---
left-aligned centered            flex-left-center-<x><u>    flx-lft-cnt, left-center, lft-cnt, l-c, lc, left, l        Int > 0      (px, em, rem, vh, vw, %)     
left-aligned top-aligned         flex-left-top-<x><u>       flx-lft-cnt, left-top, lft-top, l-t, lt                    Int > 0      (px, em, rem, vh, vw, %)
left-aligned bottom-aligned      flex-left-bottom-<x><u>    flx-flt-bot, left-bottom, lft-bot, l-b, lb                 Int > 0      (px, em, rem, vh, vw, %)
right-aligned centered           flex-right-center-<x><u>   flx-rgt-cnt, right-center, rgt-cnt, r-c, rc, right, r      Int > 0      (px, em, rem, vh, vw, %)
right-aligned top-aligned        flex-right-top-<x><u>      flx-rgt-top, right-top, rgt-top, r-t, rt                   Int > 0      (px, em, rem, vh, vw, %)
right-aligned bottom-aligned     flex-right-bottom-<x><u>   flx-rgt-bot, right-bottom, rgt-bot, r-b, rb                Int > 0      (px, em, rem, vh, vw, %)
----------------------------------------------------------------------------------------------------------------------------------------------------------------
table 2: flex styles
```

In the above:
1. `flex-left-center-<x><u>` will apply a left padding of `<x><u>`
2. `flex-left-top-<x><u>` will apply a left and top padding of `<x><u>`
3. and so on.

In  the case of mixed directions, as `left-top`, `left-bottom`, `right-top` and `right-bottom`, you could also specify a custom padding for each direction. So, for example, the table above could be extended to include:
1. `flex-left-top-<xl><ul>-<xt><ut>`, which will apply a left padding of `<xl><ul>` and a top padding of `<xt><ut>`
2. `flex-left-bottom-<xl><ul>-<xb><ub>`, which will apply a left padding of `<xl><ul>` and a bottom padding of `<xb><ub>`
3. and same for `right` direction
4. and so on for each alias.

# Styles: space

(table-3)=
```
property               inline                    aliases       values            unities
---------------------------------------------------------------------------------------------------------------
margin                 margin-<x><u>             m             Int > 0           (px, em, rem, vh, vw, %)
margin-top             margin-top-<x><u>         mt            Int > 0           (px, em, rem, vh, vw, %)
margin-bottom          margin-bottom-<x><u>      mb            Int > 0           (px, em, rem, vh, vw, %)
margin-left            margin-left-<x><u>        ml            Int > 0           (px, em, rem, vh, vw, %)
margin-right           margin-right-<x><u>       mr            Int > 0           (px, em, rem, vh, vw, %)
padding                padding-<x><u>            p             Int > 0           (px, em, rem, vh, vw, %)
padding-top            padding-top-<x><u>        pt            Int > 0           (px, em, rem, vh, vw, %)
padding-bottom         padding-bottom-<x><u>     pb            Int > 0           (px, em, rem, vh, vw, %)
padding-left           ppadding-left-<x><u>      pl            Int > 0           (px, em, rem, vh, vw, %)
padding-right          padding-right-<x><u>      pr            Int > 0           (px, em, rem, vh, vw, %)
gap                    gap-<x><u>                g             Int > 0           (px, em, rem, vh, vw, %)
-------------------------------------------------------------------------------------------------------------------
table 3: spacing styles
```

# Styles: size

(table-4)=
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
table 4: sizing styles
```

# Styles: border

(table-5)=
```
property                   inline                        aliases        values      unities              styles
----------------------------------------------------------------------------------------------------------------------------
border-top                 border-top-<x><u>-<s>         bt             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-bottom              border-bottom-<x><u>-<s>      bb             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-right               border-right-<x><u>-<s>       br             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-left                border-left-<x><u>-<s>        bl             Int > 0     (px, em, rem, %)     (solid, dashed, etc.)
border-radius              border-radius-<x><u>          bR, radius     Int > 0
-----------------------------------------------------------------------------------------------------------------------------
table 5: border styles
```

# Other Docs

```{toc-dir}
```
