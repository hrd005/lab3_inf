'''     Функции ''' 
def dictUpdate(a):     
    a.update([("x",5)])     
    print("dict in function: ",a)     
    return 
    
def dictNoUpdate(a):     
    a = a.copy()     
    a.update([("y",3)])     
    print("dict in function: ",a)     
    return 
    
def returnFunc(a):     
    def f1(a):         
        print("returned f1(a): ",a)     
    return f1 
    
d= {"v":7} 
dictUpdate(d) 
print("dict out of function: ",d) 
dictNoUpdate(d) 
print("dict out of function: ",d) 
f = returnFunc(d) 
print("f: ", f) 
f(2) 
print("\n")

# task 17
def returnMod(a):
    def f2(x):
        print(x, " mod ", a, " = ", x%a)
    return f2
    
mod15 = returnMod(15)
mod15(12456)