---
title: styles
weight: 60
---


# About

```{toc}
```

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
padding                padding-<x><u>            p             Int               (px, em, rem, vh, vw, %)
padding-top            padding-top-<x><u>        pt            Int               (px, em, rem, vh, vw, %)
padding-bottom         padding-bottom-<x><u>     pb            Int               (px, em, rem, vh, vw, %)
padding-left           ppadding-left-<x><u>      pl            Int               (px, em, rem, vh, vw, %)
padding-right          padding-right-<x><u>      pr            Int               (px, em, rem, vh, vw, %)
gap                    gap-<x><u>                ---           Int               (px, em, rem, vh, vw, %)
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
border-top                 border-top-<x><u>-<s>         bt             Int         (px, em, rem, %)     (solid, dashed, etc.)
border-bottom              border-bottom-<x><u>-<s>      bb             Int         (px, em, rem, %)     (solid, dashed, etc.)
border-right               border-right-<x><u>-<s>       br             Int         (px, em, rem, %)     (solid, dashed, etc.)
border-left                border-left-<x><u>-<s>        bl             Int         (px, em, rem, %)     (solid, dashed, etc.)
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


