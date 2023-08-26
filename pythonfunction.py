#arbitary arguments*
def func(*a):
    print("i like",a)
func('mango','apple','grapes')    
#keyword arguments
def func(c,a,b):
    print('the positive number is',a)
func(c="1",b="2",a="3")
#arbitary keyword arguments**
def func(**name):
    print("his last name is",name["l"])
func(f='bruce',l='wayne')    
#default parameter
def func(a='cs'):
    print("my favourite subject is",a)
func('maths')
func('physics')
func()
