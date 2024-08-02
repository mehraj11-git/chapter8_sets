# in keyword and for loop in set 
# we use this method to check whether we have that item or not

s = {'a','b','c'}

if 'a' in s:
    print('yes')
else:
    print('no')


if 'ab' in s:
    print('yes')
else:
    print('no')

# for loop
for i in s:
    print(i)

# set maths
s1 = {1,2,3,4}
s2 = {3,4,5,6}
# union method
# we use (|) pipe in this method 
union_set=s1 | s2
print(union_set)
# intersection method 
# we use & in this method
# we can store it in variable or we can directly print it
# this method gives the output which has same items 
print(s1 & s2) 