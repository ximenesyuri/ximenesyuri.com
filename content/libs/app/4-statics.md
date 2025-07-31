---
title: statics
desc: statics
---

# Statics

# Pages

In `app` component system, a very special kind of `component` is a `page`. It is such that its rendered HTML satisfies the following:
1. its most external HTML tag is `<html>`;
2. the `<html>` block contains blocks `<head>` and `<body>`;
3. `<head>` is not inside `<block>` and vice-versa.

Thus, in sum, a `page` is a `component` that, **after being rendered**, produces an HTML in the following format:

```html
...
<html>
    ...
    <head> ... </head>
    <body> ... </body>
    ...
</html>
...
```

There is the type `Page` of all `page`s. It is actually an extension of `Component` to include two entries:
1. `assets_dir`: a directory or a list of directories from which assets are collected
2. `auto_style`: if `<style>` block will be automatically generated or not

> In the same way as `Page` is an extension of `Component`, we have `StaticPage`, which is an extension of `Static`.
