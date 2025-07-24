```ruby
   /00                                         /00
  | 00                                        | 00
 /000000   /00   /00  /000000   /000000   /0000000
|_  00_/  | 00  | 00 /00__  00 /00__  00 /00__  00
  | 00    | 00  | 00| 00  \ 00| 00000000| 00  | 00
  | 00 /00| 00  | 00| 00  | 00| 00_____/| 00  | 00
  |  0000/|  0000000| 0000000/|  0000000|  0000000
   \___/   \____  00| 00____/  \_______/ \_______/
           /00  | 00| 00|                          
          |  000000/| 00|                          
           \______/ |__/
```

# About

`typed` is a Python framework providing type safety and allowing universal constructions.

<!-- toc --> 

- [About](#about)
- [Overview](#overview)
- [Install](#install)
- [Docs](#docs)

<!-- end -->

# Overview

The lib provides a lot of `type factories`, which can be used to build custom types, which are **subtypes** of already existing types. This means that initalization is not needed during the runtime type checking. The lib also provides a class of `typed functions`, for which type hints are checked at runtime. 

So, with `typed` you have a framework ensuring type safety by:
1. defining custom types from `type factories`
2. using those custom types as type hints for `typed functions`
3. checking the type hints at runtime.

> `typed` includes a lot ready to use classes from different contexts.
    
You can also use `typed` to create and validate data models similar to [pydantic](https://github.com/pydantic/pydantic). 

# Install

With `pip`:
```bash
pip install git+https://github.com/ximenesyuri/typed  
``` 

With [py](https://github.com/ximenesyuri/py)
```bash
py i ximenesyuri/typed  
```

# Docs

1. [types](./types)
2. [models](./models)
