---
title: models
---

### Models

You can create `type models` which are subclasses of the base `Json` class and can be used to quickly validate data, much as you can do with `BaseModel` in [pydantic](https://github.com/pydantic/pydantic), but following the `typed` philosophy:

```python
from typed        import Int, Str, List
from typed.models import Model

SomeModel = Model(
    x=Str,
    y=Int,
    z=List(Int, Str)
)

json = {
    'x': 'foo',
    'y': 'bar',
    'z': [1, 'foobar']
}
```

With the above, `isinstance(json, SomeModel)` returns `False`, since `y` is expected to be an integer. As a consequence, if you use that in a `typed function`, this will raise a `TypeError`, as follows:

```python
from typed import typed, SomeType
from some.where import SomeModel

@typed
def some_function(some_json: SomeModel) -> SomeType:
    ...

json = {
    'x': 'foo',
    'y': 'bar',
    'z': [1, 'foobar']
}

some_function(json) # a raise descriptive TypeError
```



### Validation

You can validade a model entity before calling it in a typed function using the `Instance` checker:

```python
from typed        import typed, Int, Str, List
from typed.models import Model, Instance

Model1 = Model(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json1 = {
    'arg1': 'foo',
    'arg2': 'bar',
    'arg3': [1, 'foobar']
}

model1_instance = Instance(
    model=Model1,
    entity=json1
)
```

> Such a validation is better than using just `isinstance(entity, model)` because it parses the `entity` and provides specific errors, while `isinstance` just return a boolean value.

Another way to validate an instance is to call it directly as an argument for some `model`:
```python
model1_instance = Model1({
    'arg1': 'foo',
    'arg2': 'bar',
    'arg3': [1, 'foobar']
})
```

You can also use a `kwargs` approach:

```python
model1_instance = Model1({
    arg1='foo',
    arg2='bar',
    arg3=[1, 'foobar']
})
```

> Notice that you can also use the above approaches to **create** valid instances and not only to validate **already existing** instances.


### Exact Models

In [pydantic](https://github.com/pydantic/pydantic), a model created from `BaseModel` do a strict validation: a json data is considered an instance of the model iff it exactly matches the non-optional entries.  In `typed` , the `Model` factory creates subtypes of `Json`, so that a typical type checking will only evaluate if a json data **contains** the data defined in the model obtained from `Model`. So, for example, the following will not raise a `TypeError`:

```python
from typed        import typed, Int, Str, List
from typed.models import Model, Instance

Model1 = Model(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json2 = {
    'arg1': 'foo',
    'arg2': 2,
    'arg3': [1, 'foobar']
    'arg4': 'bar'
}

model1_instance = Instance(
    model=Model1,
    entity=json2
)
```

For an exact evaluation, as occurs while using `BaseModel`, you could use the `Exact` factory from `typed.models`. It also provides a `Optional` directive, as in [pydantic](https://github.com/pydantic/pydantic):

```python
from typed        import typed, Int, Str, List
from typed.models import ExactModel, Instance

Model1 = ExactModel(
    arg1=Str,
    arg2=Optional(Int, 0),  # optional entries always expect a default value
    arg3=List(Int, Str)
)

Model2 = ExactModel(
    arg1=Str,
    arg2=Int,
    arg3=List(Int, Str)
)

json1 = {
    'arg1': 'foo',
    'arg3': [1, 'foobar']
}

json2 = {
    'arg1': 'foo',
    'arg2': 2,
    'arg3': [1, 'foobar']
}

# will NOT raise a TypeError
model1_instance = Instance(
    model=Model1,
    entity=json1
)

# will NOT raise a TypeError
model2_instance = Instance(
    model=Model2,
    entity=json2
)

# WILL raise a TypeError
model2_instance = Instance(
    model=Model2,
    entity=json1
)
```
