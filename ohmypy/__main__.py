import os
from ohmypy import __version__, __author__
from ohmypy.main import ps1, ps2
from ohmypy.settings import *

print(f"Ohmypy {__version__}\n{__author__}\n\n")

print("Add this to PYTHONSTARTUP:\n"
      f"{os.path.dirname(__file__)}/main.py\n")

print(f"* PS1 could be like this:\n{ps1}\n")
print(f"* PS2 could be like this:\n{ps2}\n")
print("Note that these prompt strings can be dynamically changed.\n")

print("* Environment variables to be set:")
if not ENV: print("None")
else:
    for key in ENV: print(f"{key} -> {ENV[key]}")
print()

print("* Files to be executed:")
if not PREEXE: print("None.")
else: print(x for x in PREEXE)
print()

print("* Plugins to be loaded:")
if not PLUGINS_TO_LOAD: print("None.")
else: print(x for x in PLUGINS_TO_LOAD)
print()

print("* Ohmypy settings:")
print(f"{ACCEPT_RISKS=}")
print(f"{AUTO_UPDATE=}")
print(f"{UPDATE_DELAY=}")
print(f"{ADD_COLORS=}")
print(f"{ASK_ONCE_FRIK=}")
print(f"{ADD_COLORS=}")
print(f"{PRETTY_EXP=}")
print()

print("View the documentation at https://github.com/lebao3105/ohmypy.")