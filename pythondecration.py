def outer(func):
    def inner():
        print("good morning")
        func()
        print("thank you")
      return inner
def greeting():
    print("welcome to ocean acadamy")
x=outer(greeting)
x()
