from array import *

my_array = array('i',[1,2,3,4,5])

my_array = array('i', [1,2,3,4,5]) 
my_extnd_array = array('i', [7,8,9,10]) 
my_array.extend(my_extnd_array)

my_array = array('i', [1,2,3,4,5]) 
my_array.remove(4)

my_array = array('i', [1,2,3,4,5]) 
print(my_array.pop())

my_array = array('i', [1,2,3,4,5]) 
print(my_array.index(5))

my_array = array('i', [1,2,3,4,5])
print(my_array.buffer_info())

my_array = array('i', [1,2,3,3,5]) 
my_array.count(3)

my_array = array('i', [1,2,3,4,5]) 
c = my_array.tolist()

#compréhensions:
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]

[s.upper() for s in "Hello World"]

sentence = "Beautiful is better than ugly"
["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
#['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']

#fonction sorted:
#sorted(iterable, key=None, reverse=False)

# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)

#conditional List compréhensions
[x for x in range(10) if x % 2 == 0]

[2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]

#compréhensions de dictionnaires:
