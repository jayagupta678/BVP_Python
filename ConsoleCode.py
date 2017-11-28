Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> 
=============== RESTART: C:/Users/asus/Desktop/BVP/01-Hello.py ===============
Hello world
>>> a = 10
>>> b = 12
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a+b
22.5
>>> a-b
-1.5
>>> a/b
0.875
>>> a*b
126.0
>>> a = 12
>>> b = 7
>>> a/b
1.7142857142857142
>>> a//b
1
>>> a**4
20736
>>> a
12
>>> b
7
>>> a,b = b,a
>>> a
7
>>> b
12
>>> 
============= RESTART: C:/Users/asus/Desktop/BVP/02-ForLoops.py =============
10
11
12
13
14
15
16
17
18
19
Hello
>>> a = "Hello"
>>> a*5
'HelloHelloHelloHelloHello'
>>> for i in range(6):
	print(i * '*')

	

*
**
***
****
*****
>>> for i in range(6):
	print(' ' * (6-i) + '*' * (2*i + 1))

	
      *
     ***
    *****
   *******
  *********
 ***********
>>> print("Hello\n"*5)
Hello
Hello
Hello
Hello
Hello

>>> a = "Hello\n"
>>> a*5
'Hello\nHello\nHello\nHello\nHello\n'
>>> a = [10,11,12,13,"Hello", 10.5, True]
>>> a[0]
10
>>> a[1]
11
>>> a[0:4]
[10, 11, 12, 13]
>>> a[-1]
True
>>> a[::-1]
[True, 10.5, 'Hello', 13, 12, 11, 10]
>>> b = "Hello"
>>> b in a
True
>>> a = [12,11,45,23,1,4,32]
>>> a.sort()
>>> a
[1, 4, 11, 12, 23, 32, 45]
>>> a.sort(reverse = True)
>>> a
[45, 32, 23, 12, 11, 4, 1]
>>> a
[45, 32, 23, 12, 11, 4, 1]
>>> a = [12,11,45,23,1,4,32]
>>> sorted(a)
[1, 4, 11, 12, 23, 32, 45]
>>> a
[12, 11, 45, 23, 1, 4, 32]
>>> b = sorted(a)
>>> b
[1, 4, 11, 12, 23, 32, 45]
>>> x = a.sort()
>>> x
>>> type(x)
<class 'NoneType'>
>>> a
[1, 4, 11, 12, 23, 32, 45]
>>> x = a
>>> a = (12,11,45,23,1,4,32)
>>> a[2]
45
>>> a[2:5]
(45, 23, 1)
>>> list_1 = [12,11,45,23,1,4,32]
>>> a = (12,11,45,23,1,4,32)
>>> list_1[0] = "Hello"
>>> list_1
['Hello', 11, 45, 23, 1, 4, 32]
>>> a[0] = "Helllo"
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a[0] = "Helllo"
TypeError: 'tuple' object does not support item assignment
>>> dict_1 = {'id':101, "Name":"Ram", "Age":20}
>>> dict_1[1]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict_1[1]
KeyError: 1
>>> dict_1["id"]
101
>>> dict_1["Name"]
'Ram'
>>> set_1 = {1,2,3,4,5}
>>> set_2 = {4,5,6,7,8}
>>> even = []
>>> 
============== RESTART: C:/Users/asus/Desktop/BVP/03-IfElse.py ==============
Even
>>> for i in range(1,101):
	if i % 2 == 0:
		even.append(i)

		
Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    even.append(i)
NameError: name 'even' is not defined
>>> even = []
>>> for i in range(1,101):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> even = [i for i in range(1,101) if i % 2 == 0]
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> str_1 = "Hello"
>>> str_1 = 'Hello'
>>> str_1[0]
'H'
>>> str_1[0:4]
'Hell'
>>> str_1[::-1]
'olleH'
>>> 
