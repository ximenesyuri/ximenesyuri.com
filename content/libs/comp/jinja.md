---
title: jinja
desc: jinja
weight: 5
---

# About

In the following we discuss  _jinja strings_, which are the return entity of an entity in {lib:comp} component system.

```{toc}
```

# Jinja Strings

The component system of {lib:comp} is based in {jinja2}. This means that the {lib:components} construct strings following {jinja2} syntax. We have a specific type `Jinja` (which is a subtype of `Str` - the string {lib:type} of {lib:typed}) whose instances are the so-called _jinja strings_. These are Python {py:strings} preppended with the "`jinja`" keyword.

So, more precisely, an instance of `Jinja` is a string as follows (see {jinja2} to discover the full valid syntax):

(jinja-string)=
```python
my_jinja_string = """jinja
[% for i in x %]
<some html>
    [% if y is True %]
    [% set w = "something" %]
    <more html>
    ...
[# my beautiful comment #]
    [[ z ]]
    ...
    </more html>
    [% endif %]
</some html>
[% endfor %]
"""
```

# Delimiters

You should note that the {jinja2} code provided in the [previous](#jinja-string) {lib:jinja string} uses delimiters differing from the standard ones: while {lib:jinja} uses `{%`, `{{` and `{#` as default for blocks, variables and comments, respectively, we are using `[`, `[[` and `[#`. 

The reason is that as we will see in [components](./components) documentation, in {lib:comp} the {lib:jinja strings} are typically returned by functions, and one would like to use variables of the function inside the return jinja string. This implies to consider the jinja strings as {py:f-strings}. But in f-strings, variables already use `{` as delimiters, causing certain conflict with the default {lib:jinja} delimiters.

If you don't like using `[` as the basic delimiter for {lib:jinja strings}, you can set one of the following options, or some mix of them:

(table-1)=
```
blocks      variables      comments        
--------------------------------------------------
[% ... %]   [[ ... ]]      [# ... #]
(% ... %)   (( ... ))      (# ... #)
<% ... %>   << ... >>      <# ... #>
--------------------------------------------------
table 1: jinja delimiters
```

This is done by setting the following environment variables:

(table-2)=
```
env                          description                     default value
------------------------------------------------------------------------------
COMP_JINJA_VAR_DELIM         delimiters for jinja vars       ("[[", "]]")
COMP_JINJA_BLOCK_DELIM       delimiters for jinja blocks     ("[%", "%]")
COMP_JINJA_COMMENT_DELIM     delimiters for jinja comments   ("[#", "#]")
-------------------------------------------------------------------------------
table 2: jinja delimiters envs
```

# Variables

When working with {lib:jinja strings} we have two kinds of variables:
1. _inner jinja variables_, which are defined as part of the jinja string through a `[% set ... %]` block;
2. _free jinja variables_, which are not defined inside the jinja string.

So, for example, in the [above](#jinja-string) jinja string, `x`, `y` and `z` are all _free jinja variables_, while `w` is an _inner jinja var_.

The variables of a {lib:jinja string} are accessible as {py:attributes} corresponding to {py:properties} of the type `Jinja`:

(table-3)=
```
attribute           meaning 
---------------------------------------------------------------------
.vars               dictionary with all vars organized by kind
.inner_vars         dict of inner vars and values of the jinja string
.free_vars          tuple of free vars of the jinja string
---------------------------------------------------------------------
table 3
```

In the case of the [above](#jinja-string) jinja string one would get:
```python
from comp import Jinja
from some.where import my_jinja_string

print(Jinja(my_jinja_string).vars)        # {"inner": {"w": "something"}, "free": ("x", "y", z")}
print(Jinja(my_jinja_string).inner_vars)  # {"w": "something"}
print(Jinja(my_jinja_string).free_vars)   # ("x", "y", "z")
```

Notice that the attributes are accessible only after initialization of the jinja strings in the `Jinja` type. However, following the {lib:functions over methods} philosophy of {lib:typed}, the properties above are actually defined through {lib:typed functions}:

(table-4)=
```
attribute              typed function         
----------------------------------------------
.vars                  jinja_vars                 
.inner_vars            jinja_inner_vars         
.free_vars             jinja_free_vars          
----------------------------------------------
table 4
```

Therefore, the same action could be taken _directly_, i.e, without initialization:

```python
from comp import jinja_vars, jinja_inner_vars, jinja_free_vars
from some.where import my_jinja_string

print(jinja_vars(my_jinja_string))        # {"inner": {"w": "something"}, "free": ("x", "y", z")}
print(jinja_inner_vars(my_jinja_string))  # {"w": "something"}
print(jinja_free_vars(my_jinja_string))   # ("x", "y", "z")
```

# Rendering

The main objective of using {lib:jinja strings} is to create "dynamic HTML", where the dynamic aspects is provided precisely by the existence of {f:free jinja vars}, which are leaved to be fixed _a posteriori_. The process of transforming jinja strings into raw HTML is called _rendering_.

Notice that  the {lib:inner vars} of a {lib:jinja string} already comes equipped with a value, which is set in the moment of its definition. To be rendered we then need to set values to its {lib:free jinja vars}. This is done by defining a _jinja context_, which is a dictionary whose keys are strings with the names of the {lib:free jinja vars}, and the values are the values that will be set to them.

As example of _jinja context_ for the [above](#jinja-string) jinja string would be:

```python
my_context = {
    "x": some_value,
    "y": other_value,
    "z": another_value
}
```

One time defined the context, one renders a {lib:jinja string} by making use of the `.render` method:

```python
from comp import Jinja
from some.where import my_jinja_string

Jinja(my_jinja_string).render(**my_context)
```

Or, without initialization, through the {lib:typed function} `render`:

```python
from comp import render
from some.where import my_jinja_string

render(my_jinja_string)
```

# Factories

Inside {lib:comp} we find some _jinja factories_. These are {lib:type factories} constructing subtypes of `Jinja`. In other words, are {lib:typed functions} taking values into `SUB(Jinja)`, the {lib:type} of subtypes of `Jinja`.

# Highlight

To conclude, let us talk briefly on how to improve syntax highlight while working with {lib:jinja strings}. We have two points to consider:
1. jinja strings are used inside files with Python filetype;
2. jinja strings use delimiters differing from the standard {jinja} delimiters.

From the first point, to get a nice highlighting one needs to mix both Python and Jinja highlights. This can be done by means of creating a custom filetype or by maintaining the Python filetype and using some regex filtering that includes Jinja highlight inside Python highlighting precisely for {lib:jinja strings}.

Since in {lib:comp} the only non-pythonic feature we will need is highlighting, the second option is highly preferable. Indeed, notice that {lib:jinja strings} are defined as:
1. Python {py:strings}
2. prefixed with `jinja`
3. that contains {jinja} syntax.

The fact that they are prefixed with a special keyword was introduced precisely to allow an easy parsing of the region that will be highlighted with Jinja syntax. Indeed: it is the region in  between a `"""jinja` and a triple quotes `"""`.

There are multiple solutions to embed syntax of a language inside the syntax of other language by giving certain delimiters. Such solutions depend on the development environment. For `vim` you can use [vim-SyntaxRange](https://github.com/inkarkat/vim-SyntaxRange). For `neovim`, try [nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter). 

In the case of `vim` with `SyntaxRange`, to embed Jinja highlight with the given delimiters you can just add the following line to your `.vimrc`:

```vim
autocmd BufWinEnter,FileType python call SyntaxRange#Include('f"""jinja', '"""', 'jinja', 'NonText')
```

Concerning the second point above, before embedding Jinja syntax inside Python syntax, one first need to modify the Jinja syntax to highlight the correct delimiters. For `vim` users, you can use [Vim-Jinja2-Syntax](https://github.com/Glench/Vim-Jinja2-Syntax) with minor modifications.

# Other Docs

```{toc-dir}
```
