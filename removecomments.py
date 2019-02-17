#!/usr/bin/python
# -*- coding: utf-8 -*-

f=open("comments.py","r",encoding="utf8")
lines = f.readlines()
f.close()

f=open("comments.py","w",encoding="utf8")

for line in lines:
	if "#" in line:
		l=line.strip()


	else:
		print (line)
		f.write(line)

f.close()
