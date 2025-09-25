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

...

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
property           style string                 style aliases      
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
property         style string           style aliases 
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
property           style string           style aliases
--------------------------------------------------------------
float              float-left             flt-lft
float              float-right            flt-rgt
float              float-inline-start     flt-inl-st
float              float-inline-end       flt-inl-end
---------------------------------------------------------------
table 3: float styles
```

# Styles: align

(table-4)=
```
property           style string                     style aliases 
--------------------------------------------------------------------------------------
align-items        align-items-center               alg-it-cnt, alg-it-c, ai-c
align-items        align-items-start                alg-it-st, alg-it-s, ai-s
align-items        align-items-end                  alg-it-end, alg-it-e, ai-e
align-items        align-items-flex-start           alg-it-flx-st, alg-it-f-s, alg-it-fs, ai-fs
align-items        align-items-flex-end             alg-it-flx-end, alg-it-f-e, alg-it-fe, ai-fe
align-items        align-items-baseline             alg-it-bl, ai-bl
align-content      align-content-center             alg-cont-cnt, alg-cont-c, ac-c
align-content      align-content-start              alg-cont-st, alg-cont-s, ac-s
align-content      align-content-end                alg-cont-end, alg-cont-e, ac-e
align-content      align-content-flex-start         alg-cont-flx-st, alg-cont-f-s, alg-cont-fs, ac-fs
align-content      align-content-flex-end           alg-cont-flx-end, alg-cont-f-e, alg-cont-fe, ac-fe
align-content      align-content-baseline           alg-cont-bl, ac-bl
align-content      align-content-space-between      alg-cont-space-between, alg-cont-s-b, alg-cont-sb, ac-sb
align-content      align-content-space-around       alg-cont-space-around, alg-cont-s-a, alg-cont-sa, ac-sa
align-content      align-content-space-evenly       alg-cont-space-evenly, alg-cont-s-e, alg-cont-se, ac-se
--------------------------------------------------------------------------------------
table 4: align styles
```

# Styles: justify

(table-5)=
```
property           style string                    style aliases
------------------------------------------------------------------------------------------------------------------------------
justify-items      justify-items-center            just-it-center, jst-it-cnt, jst-it-c, ji-c
justify-items      justify-items-left              just-it-left, just-it-left, jst-it-lft, jst-it-l, ji-l
justify-items      justify-items-right             just-it-right, jst-it-rgt, jst-it-r, ji-r
justify-items      justify-items-start             just-it-start, jst-it-st, jst-it-s, ji-s
justify-items      justify-items-end               just-it-end, jst-it-end, jst-it-e, ji-e
justify-items      justify-items-flex-start        just-it-flex-start, jst-it-flx-st, jst-it-f-s, jst-it-fs, ji-fs
justify-items      justify-items-flex-end          just-it-flex-end, jst-it-flx-end, jst-it-f-e, jst-it-fe, ji-fe
justify-items      justify-items-baseline          just-it-bl, ji-bl
justify-content    justify-content-center          just-cont-center, jst-cont-cnt, jst-cont-c, jc-c
justify-content    justify-content-left            just-cont-left, just-cont-left, jst-cont-lft, jst-cont-l, jc-l
justify-content    justify-content-right           just-cont-right, jst-cont-rgt, jst-cont-r, jc-r
justify-content    justify-content-start           just-cont-start, jst-cont-st, jst-cont-s, jc-s
justify-content    justify-content-end             just-cont-end, jst-cont-end, jst-cont-e, jc-e
justify-content    justify-content-flex-start      just-cont-flex-start, jst-cont-flx-st, jst-cont-f-s, jst-cont-fs, jc-fs
justify-content    justify-content-flex-end        just-cont-flex-end, jst-cont-flx-end, jst-cont-f-e, jst-cont-fe, jc-fe
justify-content    justify-content-space-between   just-cont-space-between, jst-cont-s-b, jst-cont-sb, jc-sb
justify-content    justify-content-space-around    just-cont-space-around, jst-cont-s-a, jst-cont-sa, jc-sa
justify-content    justify-content-space-evenly    just-cont-space-evenly, jst-cont-s-e, jst-cont-se, jc-se
-------------------------------------------------------------------------------------------------------------------------------
table 5: justify styles
```

# Styles: flex

(table-6)=
```
description                      style string               style aliases                                              values       unities
-------------------------------------------------------------------------------------------------------------------------------------------------------------
centered                         flex-center                flx-center, flx-cnt, center, cnt, c                        ---
left-aligned centered            flex-left-center-<x><u>    flx-lft-cnt, left-center, lft-cnt, l-c, lc, left, l        Int > 0      px, em, rem, vh, vw, %     
left-aligned top-aligned         flex-left-top-<x><u>       flx-lft-cnt, left-top, lft-top, l-t, lt                    Int > 0      px, em, rem, vh, vw, %
left-aligned bottom-aligned      flex-left-bottom-<x><u>    flx-flt-bot, left-bottom, lft-bot, l-b, lb                 Int > 0      px, em, rem, vh, vw, %
right-aligned centered           flex-right-center-<x><u>   flx-rgt-cnt, right-center, rgt-cnt, r-c, rc, right, r      Int > 0      px, em, rem, vh, vw, %
right-aligned top-aligned        flex-right-top-<x><u>      flx-rgt-top, right-top, rgt-top, r-t, rt                   Int > 0      px, em, rem, vh, vw, %
right-aligned bottom-aligned     flex-right-bottom-<x><u>   flx-rgt-bot, right-bottom, rgt-bot, r-b, rb                Int > 0      px, em, rem, vh, vw, %
----------------------------------------------------------------------------------------------------------------------------------------------------------------
table 6: flex styles
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

(table-7)=
```
property               style string             style aliases       values            unities
---------------------------------------------------------------------------------------------------------------
margin                 margin-<x><u>             m                  Int > 0           px, em, rem, vh, vw, %
margin-top             margin-top-<x><u>         mt                 Int > 0           px, em, rem, vh, vw, %
margin-bottom          margin-bottom-<x><u>      mb                 Int > 0           px, em, rem, vh, vw, %
margin-left            margin-left-<x><u>        ml                 Int > 0           px, em, rem, vh, vw, %
margin-right           margin-right-<x><u>       mr                 Int > 0           px, em, rem, vh, vw, %
padding                padding-<x><u>            p                  Int > 0           px, em, rem, vh, vw, %
padding-top            padding-top-<x><u>        pt                 Int > 0           px, em, rem, vh, vw, %
padding-bottom         padding-bottom-<x><u>     pb                 Int > 0           px, em, rem, vh, vw, %
padding-left           ppadding-left-<x><u>      pl                 Int > 0           px, em, rem, vh, vw, %
padding-right          padding-right-<x><u>      pr                 Int > 0           px, em, rem, vh, vw, %
gap                    gap-<x><u>                g                  Int > 0           px, em, rem, vh, vw, %
-------------------------------------------------------------------------------------------------------------------
table 7: spacing styles
```

# Styles: size

(table-8)=
```
property              style string           style aliases      values          unitites
------------------------------------------------------------------------------------------------
width                 width-<x><u>           w                  Int > 0         px, em, rem, vh, vw, %
min-width             min-width-<x><u>       mw                 Int > 0         px, em, rem, vh, vw, %
max-width             max-width-<x><u>       Mw                 Int > 0         px, em, rem, vh, vw, %
height                height-<x><u>          h                  Int > 0         px, em, rem, vh, vw, %
min-height            min-height-<x><u>      mh                 Int > 0         px, em, rem, vh, vw, %
max-height            max-height-<x><u>      Mh                 Int > 0         px, em, rem, vh, vw, %
----------------------------------------------------------------------------------------------
table 8: sizing styles
```

# Styles: border

(table-9)=
```
property                   style string                  style aliases          values      unities              styles
----------------------------------------------------------------------------------------------------------------------------
border-top                 border-top-<x><u>-<s>         bt                     Int > 0     px, em, rem, %       solid, dashed, etc
border-bottom              border-bottom-<x><u>-<s>      bb                     Int > 0     px, em, rem, %       solid, dashed, etc
border-right               border-right-<x><u>-<s>       br                     Int > 0     px, em, rem, %       solid, dashed, etc
border-left                border-left-<x><u>-<s>        bl                     Int > 0     px, em, rem, %       solid, dashed, etc
border-radius              border-radius-<x><u>          bR, radius             Int > 0
-----------------------------------------------------------------------------------------------------------------------------
table 9: border styles
```

# Styles: text

(table-11)=
```
property         style string             style aliases
---------------------------------------------------------------------------------------------------------
text-align       text-align-center        txt-alg-center, txt-alg-cnt, txt-alg-c, ta-c
text-align       text-align-left          txt-alg-left, txt-alg-lft, txt-alg-l, ta-l
text-align       text-align-right         txt-alg-right, txt-alg-rgt, txt-alg-r, ta-r
text-align       text-align-start         txt-alg-start, txt-alg-st, txt-alg-s, ta-s
text-align       text-align-end           txt-alg-end, txt-alg-e, ta-e
text-align       text-align-justify       txt-alg-justify, txt-alg-just, txt-alg-jst, txt-alg-j, ta-j
---------------------------------------------------------------------------------------------------------
table 10: text align styles
```

(table-11)=
``` 
property           style string                 style aliases
--------------------------------------------------------------------------------------
text-justify       text-justify-none            txt-just-none, tj-none, tj-n
text-justify       text-justify-auto            txt-just-auto, tj-auto, tj-a
text-justify       text-justify-distribute      txt-just-distribute, tj-dist, tj-d
text-justify       text-justify-word            text-just-word, tj-word, tj-w
text-justify       text-justify-character       text-just-char, tj-char, tj-c
--------------------------------------------------------------------------------------
table 11: text justify styles
```

(table-12)=
```
property         style string               style aliases
------------------------------------------------------------------------------------------------------
text-wrap        text-wrap                  wrap, txt-wrap, tw, 
text-wrap        text-nowrap                nowrap, txt-nowrap, txt-wrap-none, tw-none, tw-no, tw-n
text-wrap        text-wrap-balance          txt-wrap-bal, tw-bal, tw-b
text-wrap        text-wrap-pretty           txt-wrap-pretty, txt-wrap-pty, tw-pretty, tw-pty, tw-p
-------------------------------------------------------------------------------------------------------
table 12: text wrap styles
```

(table-13)=
```
property            style string                                    style aliases                                            value       unities            styles 1    styles 2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
text-decoration     text-decoration-underline-<x><u>-<s1>-<s2>      underline, under, txt-decor-under, td-under, td-u        Int > 0     px, em, rem, %     HEX, RGB    solid, dashed, etc
text-decoration     text-decoration-overline-<x><u>-<s1>-<s2>       overline, txt-decor-over, td-over, td-o                  Int > 0     px, em, rem, %     HEX, RGB    solid, dashed, etc.
text-decoration     text-decoration-through-<x><u>-<s1>-<s2>        through, txt-decor-thr, td-thr, td-t                     Int > 0     px, em, rem, %     HEX, RGB    solid, dashed, etc.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
table 13: text decoration styles
```

(table-14)=
```
property            style string                    style aliases
--------------------------------------------------------------------------------------------------------------
text-transform      text-transform-uppercase        uppercase, upper, txt-trans-upper, tt-upper, tt-u
text-transform      text-trasform-lowercase         lowercase, lower, txt-trans-lower, tt-lower, tt-l
text-transform      text-transform-capitalize       capitalize, cap, txt-trans-cap, tt-cap, tt-c
--------------------------------------------------------------------------------------------------------------
table 14: text transform styles
```

# Styles: font

(table-15)=
```
property          style string              style aliases           value
---------------------------------------------------------------------------------------------------------------------------
font-family       font-family-<x>           ff                      'Font Family', ('Some Family', 'Other Family', ...)
font-family       font-family-sans-<x>      sans, ff-sans, ff-ss    'Font Family', ('Some Family', 'Other Family', ...)
font-family       font-family-serif-<x>     serif, ff-serif, ff-s   'Font Family', ('Some Family', 'Other Family', ...)
font-family       font-family-mono-<x>      mono, ff-mono, ff-m     'Font Family', ('Some Family', 'Other Family', ...)
---------------------------------------------------------------------------------------------------------------------------
table 15: font family styles
```

(table-16)=
```
property        style string            style aliases                               value       unties
--------------------------------------------------------------------------------------------------------------------
font-size       font-size-<x><u>        fz                                          Int > 0     px, em, rem, %
font-size       font-size-xx-small      xx-small, fz-xx-small, fz-xx-s, fz-xxs      ---         ---
font-size       font-size-x-small       x-small, fz-x-small, fz-x-s, fz-xs          ---         ---
font-size       font-size-small         small, fz-small, fz-s                       ---         ---
font-size       font-size-medium        medium, fz-medium, fz-m                     ---         ---
font-size       font-size-large         large, fz-large, fz-l                       ---         ---
font-size       font-size-x-large       x-large, fz-x-large, fz-x-l, fz-xl          ---         ---
font-size       font-size-xx-large      xx-large, fz-xx-large, fz-xx-l, fz-xxl      ---         ---
font-size       font-size-huge          huge, fz-huge, fz-h, fz-xxx-l, fz-xxxl      ---         ---
--------------------------------------------------------------------------------------------------------------------
table 16: font size style
```

(table-17)=
```
property          style string                  style aliases                                                              value
-----------------------------------------------------------------------------------------------------------------------------------------------
font-weight       font-weight-xx-light          xx-light, fw-xx-l, fw-xxl                                                  ---
font-weight       font-weight-x-light           x-light, fw-extra-light, fw-x-l, fw-xl                                     ---
font-weight       font-weight-light             light, fw-light, fw-l                                                      ---
font-weight       font-weight-normal            normal, fw-normal, fw-n                                                    ---
font-weight       font-weight-x-normal          x-normal, semi-bold, fw-x-normal, fw-semi-bold, fw-sb, fw-x-n, fw-xn       ---
font-weight       font-weight-bold              bold, fw-bold, fw-b                                                        ---
font-weight       font-weight-x-bold            x-bold, fw-x-bold, fw-x-b, fw-xb                                           ---
font-weight       font-weight-xx-bold           Bold, xx-bold, fw-xx-bold, fw-black, fw-xxb, fw-B                          ---
font-weight       font-weight-<x>               fw                                                                         100, 200, 300, 400, 500, 600, 700 
----------------------------------------------------------------------------------------------------------------------------------------------
table 17: font weight styles
```


(table-18)=
```
property       style string             style aliases                             value
---------------------------------------------------------------------------------------------
font-style     font-style-italic        italic, it, fs-italic, fs-it, fs-i        ---
color          font-color-<x1>          color, fc                                 HEX, RGB
---------------------------------------------------------------------------------------------
table 18: other font styles
```

# Styles: background

# Styles: grid


# Other Docs

```{toc-dir}
```
