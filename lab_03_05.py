d2 = dict(bananas=3,apples=5,oranges=2,bag="basket") 

'''     Операции cо словарями ''' 
d5 = d2.copy() 
# создание копии словаря 
print("Dict d5 copying d2 = ", d5) 

# получение значения по ключу 
print("Get dict value by key d5['bag']: ", d5["bag"]) 
print("Get dict value by key d5.get('bag'): ", d5.get('bag')) 
print("Get dict keys d5.keys(): ", d5.keys()) 
# список ключей 
print("Get dict values d5.values(): ", d5.values()) 
# список значений 
print("\n")

myInfo = {
    "surname": "Stepanoff",
    "name": "Denis",
    "middlename": "Alexandrovich",
    "day": 5,
    "month": 8,
    "year": 2002,
    "university": "ITMO, until the first session at least"
}
print(myInfo.keys())
print(myInfo.values())