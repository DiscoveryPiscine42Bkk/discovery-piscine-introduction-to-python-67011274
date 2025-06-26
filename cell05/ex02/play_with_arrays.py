#!/usr/bin/env python

array =  [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for (x > 5) in array]
print(new_array)