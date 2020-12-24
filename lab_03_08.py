'''     Анонимные функции, lambda-выражения ''' 
lfunc = lambda x, y, z = 1: x + y + z 
print("lfunc(1,2,3): ",lfunc(1,2,3)) 
print("lfunc(1,2): ",lfunc(1,2)) 
print("lfunc(x=1,y=3): ",lfunc(x=1,y=3)) 
print("lambda result: ", \
    (lambda a,b,sep=", ": 
        sep.join((a,b)))("Hello","World!")) 
print("\n") 

# task 21
lam = lambda x: x%3 == 0
x = int(input())
if lam(x):
    print(x)