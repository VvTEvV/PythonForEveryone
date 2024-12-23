Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
type(tao)
<class 'turtle.Turtle'>
tao.shape('turtle')
tao.color('green')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.shape('snake')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tao.shape('snake')
  File "C:\Python313\Lib\turtle.py", line 2831, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named snake
tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.color('red')
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
for i in range(4):
    print(i)
    tao.forward(100)
    tao.left(90)

    
0
1
2
3
list(range(4))
[0, 1, 2, 3]
list(range(1,4))
[1, 2, 3]
list(range(0,10,2))
[0, 2, 4, 6, 8]
taolist = []
tao.reset()
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
tao.up()
>>> tao.goto(30,30)
>>> 
>>> tao.down()for i in range(4):
...     print(i)
...     tao.forward(50)
...     tao.left(90)
...     
SyntaxError: invalid syntax
>>> tao.down()
>>> for i in range(4):
...     print(i)
...     tao.forward(50)
...     tao.left(90)
... 
...     
0
1
2
3
>>> taolist = []
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
>>> print(taolist)
[<turtle.Turtle object at 0x00000205C3C6F230>, <turtle.Turtle object at 0x00000205C3D46490>, <turtle.Turtle object at 0x00000205C3D465D0>]
>>> taolist[0].forward(200)
>>> taolist[1].backward(200)
>>> taolist[2].color('red')
>>> taolist[2].left(90)
>>> taolist[2].forward(100)
>>> for t in taolist:
...     for i in range(4):
...         t.forward(50)
...         t.left(90)
... 
...         
