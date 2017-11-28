Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def func_1():
	print("Hello")

	
>>> func_1()
Hello
>>> def add(x,y):
	print(x+y)

	
>>> add(1,2)
3
>>> def add(x,y):
	return x+y

>>> add(2,4)
6
>>> a = {"1" : "Hello", "2" : "Bye"}
>>> a["1"]
'Hello'
>>> a.get("1")
'Hello'
>>> a = {"1" : "Hello", "2" : "Bye", "3" : add}
>>> a
{'1': 'Hello', '2': 'Bye', '3': <function add at 0x000001A86B9A0730>}
>>> a.get("3")
<function add at 0x000001A86B9A0730>
>>> a.get("3")()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.get("3")()
TypeError: add() missing 2 required positional arguments: 'x' and 'y'
>>> a.get("3")(1,2)
3
>>> def add(x,y):
	return x + y

>>> x = add(2,3)
>>> x
5
>>> print(x)
5
>>> def calc(x,y):
	return x + y, x - y, x / y, x * y

>>> calc(2,4)
(6, -2, 0.5, 8)
>>> x = calc(2,4)
>>> x
(6, -2, 0.5, 8)
>>> i,j,k,l = calc(2,4)
>>> i
6
>>> j
-2
k
>>> 
>>> k
0.5
>>> l
8
>>> "10" + "+"
'10+'
= 
>>> 10 + "+" + 12
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    10 + "+" + 12
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> eval("10+12")
22
>>> 
