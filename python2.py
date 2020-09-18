import keyword
print (keyword.kwlist)

a,b,c = 1,'bouhou',9.1



#sequences and collections

tuple= (1,2,"coco")
liste1= [a,b,[c,a]]

#set, an unirdered collection of unique values, Items must be hashable

set1={1,2,'a'}

dict1={1: "nico",2:"Carole"}

dict2= {"tomate": "fruit","saucisse":"pas végan"}

print(type(dict1))

if isinstance(a, int):
    a += 1

chaine =str(a) + "nounou"

print(chaine)

liste3=list(chaine)
set2=set(chaine)
print(liste3)
print(set2)

for i in range(0,len(liste3)):
    print(liste3[i])
    
liste3.insert(4,'tonton-david')

for i in range(0,len(liste3)):
    print(liste3[i])
    
index1=liste3.index('tonton-david')
print(index1)

print("liste3.count 'n':"+str(liste3.count('n')))
print("liste3.reverse()")
liste3.reverse()
print(liste3)
liste3[::-1]
print(liste3.pop())
print("liste3:", end=str(liste3))

un_membre_tuple =('membre',) #noter la virgule
deuxieme_option = 'membre',

#troisieme_option = tuple(['membre'])

vitesses ={30:'troisieme',60:'quatrieme',70:'cinquieme'}

print(vitesses[30])

for k in vitesses.keys():
    print('{} est la vitesse pour rouler en {}'.format(k,vitesses[k]))
    
#A set is a collection of elements with no repeats and without insertion order but sorted order. They are used in situations where it is only important that some things are grouped together, and not what order they were included. For large groups of data, it is much faster to check whether or not an element is in a set than it is to do the same for a list.

prénoms = {'coco','cucu','poupou'}

liste7=['roro','rara','yoyo']
my_set= set(liste7)

if 'roro' in my_set:
    print('roro')
    
from collections import defaultdict
vitesses = defaultdict(lambda : 'connais pas')

print(vitesses[180])
    
print(dir())

print(dir(__builtins__))

#help(vars)

import math as concombre

print("math(sqrt(16)):"+str(concombre.sqrt(16)))
print(dir(concombre))#dir(): to check the buit in fonctions.

print(concombre.__doc__)

entree=input("comment ca va?") #input always string

import python_docstring_test
print(python_docstring_test.__doc__)

from python_docstring_test import bonjour #importer la fonction bonjour dans le module python_docstring


#str() and repr()
s="""'t""otal'"""
print(repr(s))
print(str(s))

import datetime

today = datetime.date.today()
print(today)

#sets
print({1,2,'ro',5}.intersection({'ro',5}))

seta={1,5,6,7}
seta.add(10)
print(seta)

#the best way to get unique elements of a list is to turn them into a set:

resto = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]

unique_resto = set(resto)
print(list(unique_resto))

print(~4)
#~ alt + n sur mac

print (bin(5^4))#xor
print (bin(40&30))#and
print(bin(40|70))#| alt+maj+l OR

#décalage à gauche
print(bin(2<<2))
#a droite >>

#nonlocal nested scope
#global

x= 5
del x



i=0
while i < 7:
    print(i) 
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

for i in (0, 1, 2, 3, 4, 5): 
    if i == 2 or i == 4:
        continue 
    print(i)
    
for i in range(3): 
    print(i)
else: 
    print('done')
    
while i < 3: 
    print(i)
i += 1 else:
    print('done')
    
#pass

d={'roro':1,'toto':4,'uiui':5}

for key in d:
    print(key)

collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]

for i1, i2, i3 in collection:
    print()

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for s in lst:
    print s[:1] # print the first letter


for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))