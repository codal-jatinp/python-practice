#!/usr/bin/env python3
# -*- coding: utf-8 -*-

JATIN='jatin'
print(f"{JATIN!r}")

print(r'C:\some\name')
print('C:\some\name')
print("""
this string can be 
on any line\nand much more""")

print(r"""
this string can be 
on any line\nand much more""")

new_str = "con" + "catenated"

print(new_str)

new_str = "py" "thon"

print(new_str)

a = "con"
b = "cat"

new_str = a + b

print(new_str)

new_str = "co" r'n' "cat"

print(new_str)

a = 'jatin'
b: str = str(input("Enter new string: "))
c = ''.join(b.split())[:]
print(id(a), id(b), id(c))