#!/usr/bin/env python

import string
import random
from random import randrange
random.choice(string.ascii_lowercase)


f= open("first.txt", "w+")
g= open("second.txt", "w+")
h= open("third.txt", "w+")

var1 = ""
var2 = ""
var3 = ""

for i in range(0,10):
	var1 += random.choice(string.ascii_lowercase)
print var1
var1 += "\n"
f.write(var1)

for i in range(0,10):
	var2 += random.choice(string.ascii_lowercase)
print var2
var2 += "\n"
g.write(var2)

for i in range(0,10):
	var3 += random.choice(string.ascii_lowercase)
print var3
var3 += "\n"
h.write(var3)

var4 = randrange(1, 42)
print var4

var5 = randrange(1, 42)
print var5

print (var4 * var5)

