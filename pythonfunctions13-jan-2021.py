#la difference en nombre de jours entre deux dates:

#ma solution:
from datetime import date
def days_diff(a, b):

    # your code here
    return abs((date(b[0],b[1],b[2])-(date(a[0],a[1],a[2]))).days)

#other solutions:
import datetime

def days_diff(a, b):
    # your code here
    return abs((datetime.date(*a) - datetime.date(*b)).days)

import datetime

datify = lambda x: datetime.date(x[0], x[1], x[2])
days_diff = lambda a,b: abs((datify(a) - datify(b)).days)

from datetime import date
days_diff = lambda a,b : abs(date(a[0],a[1],a[2]).toordinal()- date(b[0],b[1],b[2]).toordinal())

def days_diff(a, b):
    import datetime
    td = datetime.date(*map(int, a)) -  datetime.date(*map(int, b))
    return abs(td.days)

#count digits:
#ma solution:
def count_digits(text: str) -> int:
    # your code here
    a=0
    for x in text:
        if x.isdigit():
            a+= 1
    return a

def count_digits(text: str) -> int:
    p=text.split()
    t=[]
    q=0
    for i in range(0,len(p)):
        t=[char for char in p[i]]
        s=len(t)
        for j in range(0,s):
            if(t[j].isdigit()):
                q+=1
            else:
                q+=0
    return q

def count_digits(text: str) -> int:
    return len([word for word in text if word.isdigit()])

def count_digits(text: str) -> int:
    count = 0
    for i in text:
        if '0' <= i <= '9':
            count += 1
    return count

def count_digits(text: str) -> int:
    # your code here
    n = 0
    for i in range(len(text)) :
        if text[i].isdigit() :
            n += 1
    return n

def count_digits(text: str) -> int:
    return len(''.join(x for x in text if x.isnumeric()))

def count_digits(text: str) -> int:
    # your code here
    return sum(1 for _ in (filter(str.isdigit, text)))

def count_digits(text: str) -> int:
    # your code here
    return sum(1 for s in text if s.isdigit())

def count_digits(text: str) -> int:
    # your code here
    import re

    return len(re.findall('\d', text))

#a given string you should reverse every word , but the words should stay in their place:
#ma solution:

def backward_string_by_word(text: str) -> str:

    return " ".join([x[::-1] for x in text.split(" ")])

#sorted dictionnary list given a int and a list of dict in which second element is price
#sort by price

def bigger_price(limit: int, data: list) -> list:
#ma reponse:
  #sorted(nums, key = lambda x: x%2)
    return  sorted(data, key =lambda x : -x["price"])[:limit]

    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

#other solutions:
def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key = lambda i: i['price'], reverse=True)[0:limit]
