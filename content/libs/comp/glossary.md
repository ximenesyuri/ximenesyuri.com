---
title: glossary
weight: 999
---

# About

Here you will find the definition for the main concepts introduced in {lib:comp} library.

```{toc}
```

# Concepts

(jinja-string)=
> [jinja string](#jinja-string).
>
> A _jinja string_ is a Python {py:string} preppended with the keyword `jinja`, and which contains {jinja} syntax. They form a type `Jinja`, which is a subtype of `Str`, the {lib:typed} string type. 

(jinja-delimiter)=
> [jinja delimiter](#jinja-delimiter).
>
> The _jinja delimiters_ are the logic delimiters used to define code blocks, variables and comments in the {jinja} syntax. In {lib:comp} they are given by `[%`, `[[` and `[#`, respectively, but can also be customized through the envs `COMP_JINJA_BLOCK_DELIM`, `COMP_JINJA_VAR_DELIM` and `COMP_JINJA_COMMMENT_DELIM`. 
 
(jinja-inner-var)=
> [jinja inner var](#jinja-inner-var).
>
> A _jinja inner variable_ is a variable in the {jinja} syntax of a {lib:jinja string} which is defined inside the {lib:jinja string} by making use of the `[% set ... %]` block. Those variables can be accessed through the attribute `.inner_vars` of `Jinja` or through the {lib:typed function} `jinja_inner_vars`.

(jinja-free-var)=
> [jinja free var](#jinja-free-var).
>
> A _jinja free variable_ is a variable in the {jinja} syntax of a {lib:jinja string} which is __not__ defined inside the {lib:jinja string}. Their values should be included in the {lib:jinja context} in order to {lib:render} the {lib:jinja string}. They can be accessed through the attribute `.free_vars` of `Jinja` or through the {lib:typed function} `jinja_free_vars`.

(jinja-context)=
> [jinja context](#jinja-context).
>
> The _jinja context_ of a {lib:jinja string} is a Python {py:dictionary} whose keys are the {lib:free jinja vars} of the {lib:jinja string}. 

(jinja-rendering)=
> [rendering](#jinja-rendering).
>
> In the context of {lib:jinja strings}, _jinja rendering_ is the process of turning them into raw HTML by giving a {lib:jinja context}.

(jinja-factory)=
> [jinja factory](#jinja-factory). 
>
> A _jinja factory_ is a {lib:type factory} taking values into a subtype of the `Jinja` type. An example is `Tag: Tuple(Str) -> TYPE`, which assigns to a tuple of strings the subtype of `Jinja` consisting of those {lib:jinja strings} which are delimited by the HTML tag named by some of the strings in the given tuple.

(component)=
> [component](#component).
>
> A _component_ is a {lib:typed function} decorated with the `@component` {py:decorator} and that returns a subtype of `Jinja`: the type of {lib:jinja strings}. Components form the {lib:type} `COMPONENT`. Components are typically structured by some {lib:component model}.

(local-context)=
> [local context](#local-context).
>
> The _local context_  of a {lib:component} is that defined by the special variable `__context__`.

(component-leak)=
> [component leak](#component-leak).
>
> A _leak_  of a {lib:component} is a {lib:jinja free var} on its underlying {lib:jinja string} which is not declared in the {lib:local context}.

(bouded-component)=
> [bounded component](#bounded-component).
>
> A _bounded component_  is a {lib:component} without {lib:leaks}. In other words, it is a {lib:component} such that every {lib:jinja free var} is  declared in the {lib:local context}.

(inner-var)=
> [inner var](#inner-var).
>
> An _inner variable_ in a {lib:component} is a variable of type `Inner`, which is {lib:type equivalent} to `Str`.  Such variables are used to denote a placeholder for future insert inside a component.

(content-var)=
> [content var](#content-var).
>
> A _content variable_ in a {lib:component} is a variable of type `Content`, which is given by `Union(Str, Extension('md', 'rst'))`. These variables represent static content (`Markdown` of `ReStructuredText`) to be included somewhere in a component.

(component-factory)=
> [component factory](#component-factory).
>
> A _component factory_ is a {lib:type factory} that takes values into some subtype of `COMPONENT`. It is, therefore, a parameterized family of components. The main component factory is `COMPONENT`, when viewed as a callable entity. Other example is `TAG`, which receive strings `*tags` and build the subtype `TAG(*tags)` of `COMPONENT` given by the components taking values in `Tag(*tags)`.

(component-model)=
> [component model](#component-model).
>
> A _component model_ is a {lib:model} (typically an {lib:optional model}) that describes the structure of a {lib:component}.

(tag-component)=
> [tag component](#tag-component).
>
> A _tag component_ is a {lib:component} whose {lib:jinja string} is encapsulated in some HTML tag block, hence that take values into the image of the {lib:jinja factory} `Tag`. In other words, a tag component is an instance of `TAG(*tags)` for some `*tags`.

(component-operation)=
> [component operation](#component-operation).
>
> A _component operation_ is a {lib:typed function} that receive {lib:components} and return other component.

(component-join)=
> [component join](#component-join).
>
> The _component join_ is a {lib:component operation} `join: Tuple(COMPONENT) -> COMPONENT` that receive components `*comps` and return the new component `join(*comps)` whose {lib:jinja string} is the string join of the corresponding {lib:jinja strings}.

(component-concat)=
> [component concat](#component-concat).
> 
> The _component concat_ is a {lib:component operation} `join: Prod(COMPONENT(1),COMPONENT) -> COMPONENT` that evaluates the {lib:inner var} of a {lib:component} with the {lib:jinja string} of other component.


# Other Docs

```{toc-dir}
```
