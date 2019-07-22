Dict={}
print("Empty Dictionary:")
print(Dict)

Dict={1:'Akshay',2:'Ramesh',3:'Gulhane'}
print("\n Dictionary with the use of Integers")
print(Dict)

Dict={'Name':"Akshay",1:[1,2,3,4]}
print("\n Dictionary with the use of mixed keys and values")
print(Dict)

Dict=dict({1: 'Akshay',2:'for',3:'cs-cart'})
print(" \n Dictionary with use of dict():")
print(Dict)

Dict=dict([(1,'Akshay'),(2,'for')])
print("\n Dictionary with each item as pair")
print(Dict)

Dict={}
print("Empty Dictionary")
print(Dict)

Dict[0]='Akshay'
Dict[2]='For'
Dict[3]=1
print("\n Dictionary after adding 3 elements :")
print(Dict)

Dict[2]='Welcome'
print("\nUpdated key values")
print(Dict)

Dict[3]={'Nested':{'1':'life','2':'Goals'}}
print("\nAdding a nested key")
print(Dict)

Dict={1:'akshay','name':'for',3:'President'}
print("\nAccessing a elementy using key:")
print(Dict['name'])

print("\nAccessing an element using key:")
print(Dict[1])

print("\nAccessing a element using get:")
print(Dict.get(3))

Dict={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"Nine"}
print("initial dictionary")
print(Dict)

del Dict[6]
print("\nAfter deleting a specific key")
print(Dict)

# del Dict['A'][2]
# print("\nDeleting from a nested key")
# print(Dict)

Dict.pop(4)
print("\n Popping specific elements")
print(Dict)

Dict.popitem()
print("/n Pops first element")
print(Dict)

Dict.clear()
print("\n Deleting Entire Dictionary")
print(Dict)
