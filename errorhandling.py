try:
    for i in range(0,6):
        print(i/0)     
except:
    print('ERROR OCCURED')
else:
    print("program completed")
finally:
    print("hello")
