---
title: glossary
weight: 999
---

# About

Here you will find the definition for the main concepts introduced in {l:comp} library.

```{toc}
```

# Concepts

(jinja-string)=
> [jinja string](#jinja-string).
>
> A _jinja string_ is a Python {p:string} preppended with the keyword `jinja`, and which contains {jinja} syntax. They form a type `Jinja`, which is a subtype of `Str`, the {l:typed} string type. 

(jinja-delimiter)=
> [jinja delimiter](#jinja-delimiter).
>
> The _jinja delimiters_ are the logic delimiters used to define code blocks, variables and comments in the {jinja} syntax. In {l:comp} they are given by `[%`, `[[` and `[#`, respectively, but can also be customized through the envs `COMP_JINJA_BLOCK_DELIM`, `COMP_JINJA_VAR_DELIM` and `COMP_JINJA_COMMMENT_DELIM`. 
 
(jinja-inner-var)=
> [jinja inner var](#jinja-inner-var).
>
> A _jinja inner variable_ is a variable in the {jinja} syntax of a {l:jinja string} which is defined inside the {l:jinja string} by making use of the `[% set ... %]` block. Those variables can be accessed through the attribute `.inner_vars` of `Jinja` or through the {l:typed function} `jinja_inner_vars`.

(jinja-free-var)=
> [jinja free var](#jinja-free-var).
>
> A _jinja free variable_ is a variable in the {jinja} syntax of a {l:jinja string} which is __not__ defined inside the {l:jinja string}. Their values should be included in the {l:jinja context} in order to {l:render} the {l:jinja string}. They can be accessed through the attribute `.free_vars` of `Jinja` or through the {l:typed function} `jinja_free_vars`.

(jinja-context)=
> [jinja context](#jinja-context).
>
> The _jinja context_ of a {l:jinja string} is a Python {p:dictionary} whose keys are the {l:free jinja vars} of the {l:jinja string}. 

(jinja-rendering)=
> [rendering](#jinja-rendering).
>
> In the context of {l:jinja strings}, _jinja rendering_ is the process of turning them into raw HTML by giving a {l:jinja context}.

(jinja-factory)=
> [jinja factory](#jinja-factory). 
>
> A _jinja factory_ is a {l:type factory} taking values into a subtype of the `Jinja` type. An example is `Tag: Tuple(Str) -> TYPE`, which assigns to a tuple of strings the subtype of `Jinja` consisting of those {l:jinja strings} which are delimited by the HTML tag named by some of the strings in the given tuple.

(component)=
> [component](#component).
>
> A _component_ is a {l:typed function} decorated with the `@component` {p:decorator} and that returns a subtype of `Jinja`: the type of {l:jinja strings}. Components form the {l:type} `COMPONENT`. Components are typically structured by some {l:component model}.

(inner-var)=
> [inner var](#inner-var).
>
> An _inner variable_ in a {l:component} is a variable of type `Inner`, which is {l:type equivalent} to `Str`.  Such variables are used to denote a placeholder for future insert inside a component.

(content-var)=
> [content var](#content-var).
>
> A _content variable_ in a {l:component} is a variable of type `Content`, which is given by `Union(Str, Extension('md', 'rst'))`. These variables represent static content (Markdown of ReStructuredText) to be included somewhere in a component.

(component-factory)=
> [component factory](#component-factory).
>
> A _component factory_ is a {l:type factory} that takes values into some subtype of `COMPONENT`. It is, therefore, a parameterized family of components. The main component factory is `COMPONENT`, when viewed as a callable entity. Other example is `TAG`, which receive strings `*tags` and build the subtype `TAG(*tags)` of `COMPONENT` given by the components taking values in `Tag(*tags)`.

(component-model)=
> [component model](#component-model).
>
> A _component model_ is a {l:model} (typically an {l:optional model}) that describes the structure of a {l:component}.

(tag-component)=
> [tag component](#tag-component).
>
> A _tag component_ is a {l:component} whose {l:jinja string} is encapsulated in some HTML tag block, hence that take values into the image of the {l:jinja factory} `Tag`. In other words, a tag component is an instance of `TAG(*tags)` for some `*tags`.

(component-operation)=
> [component operation](#component-operation).
>
> A _component operation_ is a {l:typed function} that receive {l:components} and return other component.

(component-join)=
> [component join](#component-join).
>
> The _component join_ is a {l:component operation} `join: Tuple(COMPONENT) -> COMPONENT` that receive components `*comps` and return the new component `join(*comps)` whose {l:jinja string} is the string join of the corresponding {l:jinja strings}.

(component-concat)=
> [component concat](#component-concat).
> 
> The _component concat_ is a {l:component operation} `join: Prod(COMPONENT(1),COMPONENT) -> COMPONENT` that evaluates the {l:inner var} of a {l:component} with the {l:jinja string} of other component.


# Other Docs

```{toc-dir}
```
