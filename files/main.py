# Github: EchTR
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
class txtvar:
	def __init__(self,file_name):
		self.file_name = ("{}.txt".format(file_name))
	def variables(self):
		f_file = open(self.file_name,"r")
		que2 = 0
		variables = 0
		total_l = 1
		l_l = 0
		variable_list = {}
		for i in f_file:
			total_l = total_l + 1
		f_file.seek(0)
		for i in f_file:
			l_l = l_l + 1
			if l_l == total_l:
				if i == "#":
					break
				else:
					if ">" in i:
						for k in i:
							if k == ">":
								variable_list.update({str(i[0:que2-1]):str(i[que2+2:len(i)])})
								variables = variables + 1
							que2 = que2 + 1
			else:
				if ">" in i:
					for k in i:
						if k == ">":
							variable_list.update({str(i[0:que2-1]):str(i[que2+2:len(i)-1])})
							variables = variables + 1
						que2 = que2 + 1
			que2 = 0
		return variable_list	
	def numofvars(self):
		f_file = open(self.file_name,"r")
		que2 = 0
		variables = 0
		for i in f_file:
			if ">" in i:
				for k in i:
					if k == ">":
						variables = variables + 1
					que2 = que2 + 1
			que2 = 0
		return variables	
