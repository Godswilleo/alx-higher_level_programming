#!/usr/bin/python3

def read_file(filename=""):
    with open(filename,'r', encoding='utf-8') as f:
	    line = f.readline()

        if not line:
            break
        print(line)
	    
