# set are unordereed collection of data
# we use curly brackets but we donot have key and values pairs
# it contains unique items ---->means only one item for ex:{1,1,2,3,5,1,1,3,3,} it gives {1,2,3,5}
s= {1,2,3,4,4,6,5}
print(s)
# we cant do indexing or slicing in set for ex:
# print(s[1])

# its remove the duplicate items from list
# first we have t0 convert list in set and then again convert this set int0 list 
l = [1,1,2,2,3,5,4,3,6,8,9,]
l1 = list(set(l))
print(l1)

# methods
# add methods
# for adding any item we have to like this
m ={1,2,3,4,5,6} 
m.add(50) #step 1
print(m) #step 2
# we can print like this print(m.add(10)) this will gives None as a result
# remove method
m.remove(1)
print(m)
# m.remove(11)  error
# print(m)
# suppose if you write a num in remove method which is N/A in that set it shows error
# to tackle this we use discord method
m.discard(11) # no error
print(m)
# clear method
# m.clear()
# print(m)
# copy method
m.copy()
print(m)

# we cant store list or dict or tuples in set 
# we can store number or floating number or str 
g = {1,1.2,3,4,5,'string'}
print(g)
# it is unordered collection data this will print data in unordered form