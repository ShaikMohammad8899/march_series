Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatype conversions

#integer
int(8)
8
int(6.8)
6
int("hello")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
int(9+8j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(9+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float

float(6)
6.0
float(6.9)
6.9
float("hi)
      
SyntaxError: unterminated string literal (detected at line 1)
float("hi")
      
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(8+6j)
      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(8+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
      
1.0
float(False)
      
0.0

#string
      
str(6)
      
'6'
str(8.9)
      
'8.9'
str("hello world")
      
'hello world'
str(3+4j)
      
'(3+4j)'
str(True)
      
'True'
str(False)
      
'False'

#complex
      
complex(1)
      
(1+0j)
complex(5.9)
      
(5.9+0j)
>>> complex("hi everyone")
...       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("hi everyone")
ValueError: complex() arg is a malformed string
>>> complex(4+9j)
...       
(4+9j)
>>> complex(True)
...       
(1+0j)
>>> complex(False)
...       
0j
>>> 
>>> #boolean
...       
>>> bool(5)
...       
True
>>> bool(5.9)
...       
True
>>> bool("hello python")
...       
True
>>> bool(5+8j)
...       
True
>>> bool(True)
...       
True
>>> bool(False)
...       
False
