from typing import Iterable



def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]


def replace_first(items: list) -> Iterable:
    return items[1:] + items[0:1]
    

def replace_first(items: list) -> Iterable:
    return items[1:] + [items[0]] if len(items) >= 2 else items


def replace_first(items: list) -> Iterable:
    return items[1:] + [items[0]] if len(items) > 1 else items

a,b,c,d,e=[A() for _ in range(5)]

def split_pairs(a):
    delim = 0
    lis=[]
    if len(a)%2 != 0:
        for i in  range( 2,len(a),2):
            lis.append(a[delim:i])
            delim = i   
        lis.append(a[len(a)-1]+"_")
    else:    
        for i in  range( 2,len(a)+2,2):
            lis.append(a[delim:i])
            delim = i 
    return lis

def split_pairs(a):
    new_list = []
    while a != '':
        if len(a) > 2:
            new_list.append(a[0: 2])
            a = a[2:]
        elif len(a) == 2:
            new_list.append(a)
            break
        else:
            new_list.append(a + '_')
            break
    return new_list
    
def split_pairs(a):
    # your code here
    remainder = len(a)%2 #checks if number is divisble by 2
    if (remainder != 0): a += "_" #adds the "_" at the end of the string if length is not divisible by 2
    pairs = [a[x:x+2] for x in range(0, len(a), 2)] #creates slices of length 2
    return pairs
    
    
def split_pairs(a):
    # your code here
    new_list = []
    if len(a) % 2 == 1:
        # adds '_' to the end of the list
        a += '_'
    for i in range(0, len(a), 2):
        # adds the i to the list, every 2 steps
        new_list.append(a[i:i+2])
        
    return new_list
    
    
def split_pairs(a):
    # your code here
    if len(a)%2 !=0 :
        a=a+'_'
    return [a[i]+a[i+1]  for i in range(0, len(a)-1,2) ]
    
def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]
    
from textwrap import wrap

def split_pairs(a):
    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)
    
    
def split_pairs(a):
    l = len(a)
    if l == 0:
        return []
    if l == 1:
        return [a + '_']
    else:
        return [a[:2]] + split_pairs(a[2:])
        
import itertools, operator

def split_pairs(a):
    it = itertools.chain(a, '_')
    return map(operator.add, it, it)

def beginning_zeros(number: str) -> int:
    
    return 0

# Ma version:

def beginning_zeros(number: str) -> int:
    #recursive way
    if (int(number[0]) == 0) and (len(number)>1):
        return 1 + beginning_zeros(number[1:])
    elif int(number[0]) ==0 :
        return 1
    else :
        return 0
        
#other versions:

def beginning_zeros(number: str) -> int:
    count = 0
    lista = list(number)
    
    for numb in lista:
        if int(numb) != 0:
            break
        else:
            count = count + 1
    return count
    
    
def beginning_zeros(number: str) -> int:
    count_zero = 0
    for i, num in enumerate(number):
        if num == '0':
            count_zero += 1
            if i == len(number)- 1:
                break
        elif num != '0':
            break
            
    return count_zero
    
def beginning_zeros(number: str) -> int:
    # your code here
    return len(number) - len(number.lstrip('0'))

def beginning_zeros(number: str) -> int:
    # your code here
    count = 0
    for i in number:
        if i != '0':
            break
        else:
            count += 1
    return count
    
def beginning_zeros(number: str) -> int:
    # your code here
    count = 0
    while (count < len(number)):
        if number[count] != '0':
            return count
        count += 1
    return count
    
#lstrip() returns a copy of the string with leading characters stripped.
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
    
def nearest_value(values: set, one: int) -> int:
    # your code here
    #forgot to mention the notion of ordered set
    temoin =99999999
    retour =0
    for i in values:
        if i == one:
            return one
        if i>0:
            if i>one and i-one< temoin:
                temoin = i-one
                retour = i
            elif one >i and one-i<temoin:
                temoin = one-i
                retour = i
        if i<0:
            if i<one and i-one< temoin:
                temoin = i-one
                retour = i
            elif one <i and one-i<temoin:
                temoin = one-i
                retour = i
            
    return retour
    
def nearest_value(values: set, one: int) -> int:
    return min((abs(val - one), val) for val in values)[1]


def nearest_value(values: set, one: int) -> int:
    # your code here
    diff = []
    a = []
    for x in values:
        diff.append(abs(x - one))
    a = sorted(diff)
    if (one - a[0]) in values:
        return (one - a[0])
    else:
        return (a[0]+one)
        
def nearest_value(values: set, one: int) -> int:
    return min([(abs(v - one), v) for v in values], key = lambda item: (item[0], item[1]))[1]
    
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))