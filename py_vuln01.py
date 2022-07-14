# -*- coding: utf-8 -*-
import os

file_location = input('\nType location: ')

# open and read file
file = open(file_location, "r")
print(f"File content:\n{file.read()}")

# foo/bar.txt
# /Users/flpachin/.kube/config