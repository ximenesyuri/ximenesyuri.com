---
title: app
---

```ruby
  /000000   /000000   /000000
 |____  00 /00__  00 /00__  00
  /0000000| 00  \ 00| 00  \ 00
 /00__  00| 00  | 00| 00  | 00
|  0000000| 0000000/| 0000000/
 \_______/| 00____/ | 00____/
          | 00      | 00
          | 00      | 00
          |__/      |__/
```

# About

`app` is a Python framework to build web applications presenting type safety, from APIs to static pages.

```{toc}
```

# Overview

The lib consists of two parts:
1. a `component system`, which allows to define components and operate between them following a functional approach, being compatible with [jinja2](https://jinja.palletsprojects.com/en/stable/), [alpine.js](), [htmx.js](), [flexsearch](), and much more;
2. an `app system`, which is an extension of [starlette](https://www.starlette.io/) to include, for example, the construction of static applications, all of that provided in a highly intuitive interface.

Both parts are constructed focused in providing type safety, which is ensured through an extensive use of {typed}.

# Install

With `pip`:
```bash
pip install git+https://github.com/ximenesyuri/app
```

With [py](https://github.com/ximenesyuri/py):
```bash
py i ximenesyuri/app
```

# Code

The code is available at the Github repository [ximenesyuri/app](https://github.com/ximenesyuri/app).

# Docs

```{toc-dir}
```


