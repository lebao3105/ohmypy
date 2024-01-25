import os, sys
from ohmypy.printtext import *
from ohmypy.settings import PS1, PS2, ADD_COLORS
from colorama import Fore, Back, Style

# Colors
Colors: dict[str, str] = {}

for attr in dir(Back):
    if attr.isupper():
        Colors[attr + "_BACK"] = getattr(Back, attr)

for attr in dir(Fore):
    if attr.isupper():
        Colors[attr + "_FORE"] = getattr(Fore, attr)

for attr in dir(Style):
    if attr.isupper():
        Colors[attr + "_STYLE"] = getattr(Style, attr)

def PromptString1():
    new = PS1 % Colors
    return new

def PromptString2():
    new = PS2 % Colors
    return new