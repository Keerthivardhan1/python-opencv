# from collection import namedtupple
# from collection import Counter

# fruit = namedtupple('fruit' , 'number' , 'varity' , 'color')

# apple = fruit(number =2 , varity = " adsf" , color = "blue")

# print(apple.color)

from collections import namedtuple
from collections import Counter
fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
apple = fruit(number=5,variety='Granny Smith',color='red')
print(guava.color)
print(apple.variety)
c = Counter('abcacdabcacd') #With Strings
print(c)
lst = [5,6,7,1,3,9,9,1,2,5,5,7,7] #With Lists
c = Counter(lst)
print(c)
s = 'the lazy dog jumped over another lazy dog' #With Sentence
words = s.split()
c=Counter(words)
print(c)
c = Counter(a=3, b=10, c=6, d=-2)
print( "this ----", sorted(c.elements()))
print(  "values -----",sorted(c.values()))
s = 'the lazy dog jumped over another lazy dog'
words = s.split()
print(Counter(words).most_common(3))
print(sum(c.values()))               # total of all counts 
print(list(c))                        # list unique elements 
print(set(c))                          # convert to a set 
print(dict(c))                         # convert to a regular dictionary c.items()     
