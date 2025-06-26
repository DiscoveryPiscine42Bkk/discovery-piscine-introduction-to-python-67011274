#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    word = sys.argv[1]
    sentence = sys.argv[2]
    count = sentence.split().count(word)
    print(count)