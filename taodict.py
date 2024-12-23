Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao1 = {'color':'green','dis':100}
>>> tao.color(tao1['color'])
>>> def rect(tao,tdict):
...     for i in range(4)
...     
SyntaxError: expected ':'
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)

>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'red','dis':50}
>>> tao2.color(tao2dict['color'])
>>> 
>>> rect(tao2,tao2dict)

>>> tao2.shape('turtle')
