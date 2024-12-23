Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sawatsee
SyntaxError: expected '('
def sawatsee():
    """ฟังชั่นนี้ใช้สำหรับสวัสดี"""
    print('สวัสดีจ้า')

    
help(sawatdee)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    help(sawatdee)
NameError: name 'sawatdee' is not defined. Did you mean: 'sawatsee'?
help(sawatsee)
Help on function sawatsee in module __main__:

sawatsee()
    ฟังชั่นนี้ใช้สำหรับสวัสดี

def hello(friend):
    print('Hi, {}.format(friend))
          
SyntaxError: unterminated string literal (detected at line 2)
def hello(friend):
    print('Hi, {}'.format(friend))

    
print('John')
John
hello('John')
Hi, John
def land(width,long):
    cal = width * long
    cal_wa = cal / 4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {}'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal_wa))

    
def land(width,long):
    cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {}'.format(width,long))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal_wa))
... 
...     
>>> land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางเมตร
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางเมตร
>>> print(res)
None
>>> def land(width,long):
...     cal = width * long
...     cal_wa = cal / 4
...     print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {}'.format(width,long))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
...     return cal_wa
... 
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
18.75
