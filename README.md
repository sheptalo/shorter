# Link Shorter

link shorter - a little project that can help in a various situations and attempt to make something like clck.ru and etc

## ENV

| ENV NAME   | REQUIRED | DESC                                                 |
|------------|----------|------------------------------------------------------|
| HOST       | +        | Host of site to gen links                            |
| PORT       | +        | PORT IF IT NOT 80                                    |
| BOT_TOKEN  | -        | BOT_TOKEN FOR AIOGRAM IF NOT PROVIDED BOT DONT START |
| BLACK_LIST | -        | WIP                                                  |

## Run

```bash
$ python main.py
```

## TODO

- [ ] add tests
- [ ] integrate ci/cd
- [ ] add real database
- [ ] add inline_query to bot

## Architeture

```text
link_shorter
│
├───common
│       config.py
│       exceptions.py
│       __init__.py
│
├───domain
│   │   link.py
│   │   __init__.py
│   │
│   ├───interfaces
│   │       link.py
│   │       __init__.py
│   │
│   └───use_cases
│           link.py
│           __init__.py
│
├───infrastructure
│   │   di.py
│   │   __init__.py
│   │
│   └───repositories
│           link.py
│           __init__.py
│
├───presentors
│   │   __init__.py
│   │
│   ├───aiogram
│   │       handlers.py
│   │       main.py
│   │       messages.py
│   │       __init__.py
│   │
│   ├───cli
│   │       decorator.py
│   │       handle.py
│   │       main.py
│   │       __init__.py
│   │
│   └───fastapi
│           handlers.py
│           main.py
│           __init__.py
└───tests
        test_link.py
        __init__.py


```