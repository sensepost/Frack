#!/bin/python
# -*- coding: utf-8 -*-
#########################################################################################################
# Count the number of lines in the .orc file                                                            #
# Since PyOrc Reader doesn't have a count or lines attribute, we'll do it manually                      #
#########################################################################################################
import sys

if sys.version_info < (3, 9):
    print('Please upgrade your Python version to 3.9.0 or higher')
    sys.exit()

import pyorc

i = 0

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as data:
        reader = pyorc.Reader(data)
        print("Counting Lines...")
        for row in reader:
            if i <= 5:
                print(row)
            i += 1
        print(f'{i:,} lines in {sys.argv[1]}')
