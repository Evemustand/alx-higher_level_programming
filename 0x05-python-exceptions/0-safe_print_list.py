#!/usr/bin/python3
def safe_print_list(my_list-[]; x-0):

*** 
Print x elements of a list.
   Args:
	my_list(list). The list to print elements from
	x (list): The number of elements of mt_list to print
  Returns:
	The number of elements printed
***

ret = 0
for i in range (x):
try:
	print ("()".format(my_list[i], end="")
	ret += i
	except IndexError:
	break
print("")
return (ret)
