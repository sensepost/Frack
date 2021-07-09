#!/bin/python3.9
# -*- coding: utf-8 -*-
#########################################################################################################
# Count the number of lines in the .orc file                                                            #
# Since PyOrc Reader doesn't have a count or lines attribute, we'll do it manually                      #
#########################################################################################################
import pyorc
import sys

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