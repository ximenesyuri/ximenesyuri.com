The following is a curated list of dev projects that I have been developed, mostly to cover my own daily needs.
```

shell
----------
```

1. [dot](https://github.com/ximenesyuri/dot): a universal and fully customizable terminal utility tool.
    - **::desc::** Use a dot "." to do everything you need in your daily terminal use, including quickly navigation, creation of files and directories, listing, searching, safe deletion, and so on. Customizable with `yaml`. With completion script.
    - **::lang::** `bash`  
    - **::deps::** just `bash` and `yq`
    - **::stage::** usable (I use it all the time)
2. [web](https://github.com/ximenesyuri/web): a web searcher and bookmark manager CLI to quickly access web pages.
    - **::desc::** create/list/delete bookmarks and make web searches through multiples search engines. Customizable with `yaml`. With completion script.
    - **::lang::** `bash`
    - **::deps::** just `bash` and `yq`
    - **::stage::** usable (I use it all the time)
3. [comma](https://github.com/ximenesyuri/comma): a universal project manager in the form of a CLI
    - **::desc::** Manage projects on different git platforms, as Github, Gitlab, Gitea, Bitbucket, etc., through a unified CLI. Define custom pipelines and hooks, work with issues and PRs/MRs, etc. Commands focused on a project-level perspective. Customizable with `yaml`. With completion script.
    - **::lang::** `bash`
    - **::deps::** `bash`, `yq` and `fzf` 
    - **::stage::** need a lot of improvements. Currently I use it only to handle issues.
    - **::plan::** I plan to migrate the entire project to Python and use [cly](https://github.com/pythonalta/cly), my CLI builder.
4. [py](https://gitub.com/ximenesyuri/py): a minimalist and manager agnostic solution to handle projects in Python
    - **::desc::** Works as an interface for `pip`, as a `venv` and Python versions manager, package builder, and so on. Fully agnostics: using `py` dot not compromises your project with it, as the other solutions (`poetry`, `uv`, etc.) do.
    - **::lang::** `bash`
    - **::deps::** just `bash` 
    - **::stage::** usable (I use it all the time)

```

python
----------
```

1. [f-utils](https://gitub.com/f-utils): a Python framework that provides type safety and universal constructions 
    - **::desc::** Defines "typed functions", which are functions with runtime check for its type hints. Provides a lot of operations between types. Include the concept of `spectra` which allows to build type safe parametric polymorphisms. Provides a lot of utilities, all of that built using spectra and typed functions.  
    - **::lang::** `python`
    - **::deps::** just `python >= 3.9` 
    - **::stage::** usable (with caution: probably will have structural changes)
    - **::plan::** review the construction of the main libraries: [f](https://github.com/f-utils/f) and [f-core](https://github.com/f-utils/f-core). Create new utility libraries.
2. [cly](https://github.com/cly): a minimal fastAPI inspired solution to build clean Python CLIs
    - **::desc::** build CLIs as you build apps in fastAPI. Add commands, options and subcommands as you add endpoints. Aggregate commands in groups as you aggregate endpoints in routers. Automatically build bash completion scripts. Customizable help messages. Without dependencies.
    - **::lang::** `python`
    - **::deps::** just `python >= 3.9` 
    - **::stage::** usable
3. [sphinx-\*](https://github.com/search?q=owner%3Apythonalta+sphinx&type=repositories): some minimal extensions for the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation system
    - **::desc::** The extensions verse from allowing the use of markdown frontmatters in the construction of Jinja templates to the build of json indexes to be consumed for full-text search engines, as [flexsearch.js](https://github.com/nextapps-de/flexsearch).
    - **::lang::** `python`
    - **::deps::** `python`, `sphinx` and `myst-parser` (for some of them) 
    - **::stage::** usable

For more Python projects, see [github.com/pythonalta](https://github.com/pythonalta).


```

other
----------
```
