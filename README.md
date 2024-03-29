## Ohmypy

Found your Python interpreter too boring? Want to bring more colors to your console?

Here you go: OhMyPython!

Working on these features:

* A general RC file (~/.ohmypy) containing settings

* Colors thanks to colorama

* Pretty exceptions show (using pretty-errors)

* Updates

* Plugins!

### Wanna try? Let's go!

Tested on Python 3.9 (jailbroken iOS) and Python 3.11 (Windows).

Install this project. Then do one of these ways:

* Set `PYTHONSTARTUP` environment variable to the full path of `ohmypy/main.py`

* Import `ohmypy.main` anytime you use the interpreter

Voilà! Your Python is...still that, except a message that `~/.ohmypy` is not here and therefore Ohmypy will create one for you.

But with no settings inside.

Just open that file, modify everything you want, and launch Python with Ohmypy.

Voilà! You have your interpreter cooked!

### Settings

1. Python-related

a. `PS1` (str)

Python defaults to ">>> " (no quotes).

This is the prompt you see in the interpreter.

b. `PS2` (str)

Python defauts to "... " (no quotes).

Shows for function/class/loop/try-except-finally/if-else-elif indentations.

c. `ENV` (dict[str])

Environment variables to be set on Python startup.

d. `PREEXE` (list[str])

Run more startup scripts.

2. Ohmypy

a. `AUTO_UPDATE` (bool)

Not implemented, auto check for updates.

b. `UPDATE_DELAY` (str): Defaults to "3 days"

Not implemented.

c. `ACCEPT_RISKS` (bool): Defaults to False

Accept the risks made by running plugins + startup scripts.

d. `ADD_COLORS` (bool)

Add colors to prompts, if able and **asked** to.

e. `PLUGINS_TO_LOAD` (list[str])

Not implemented: plugins to load.

### Example

On `~/.ohmypy`:

```python
ENV = {"TEST": '6'}
PS1 = "[%(ASCTIME)s, Python %(PYVER)s on %(ARCH)s %(OS)s]\n> %(RED_FORE)s%(USERNAME)s%(RESET_FORE)s %(CURRDIR)s$ "
PS2 = "Indent: %(GREEN_FORE)s>>> %(RESET_FORE)s"
```

Run Python will see something like this, next to the general Python message:

```
[Fri Jan 26 21:11:14 2024, Python 3.11.5 on ('64bit', 'WindowsPE') Windows-10-10.0.22631-SP0]
> lebao3105 C:\Users\lebao3105\Projects\ohmypy$ for i in range(10):
Indent: >>>     print(i)
```

It's your prompt!

Test (default PS1):

```python
>>> import os
>>> os.environ['TEST']
'6'
```

### Writing plugins

Plugins are (Test)Pypi packages with `ohmypy-` prefix.

The module must have `main()` function for plugin initialization and `deinit()` for plugin deinitialization (optional).