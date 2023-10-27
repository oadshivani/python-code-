print("first day python")
# list are allow duplicat members, changable,  ordered, constracted into [ ]


Name = ["shivani", 11,22,1133]
print(Name)
print(type(Name))

# retrive======   1
print(Name[0])
print(Name[2])

# add =====     2
Name.append("oad")
print(Name)

# update =====  3
print(Name[0])
print(Name[1])
Name[0] = "SHIVA"
print(Name)

# remove  ====== 4
# pop
Name.pop()
print(Name)

Name.pop(0)
print(Name)

Name.append("shivani")
Name.append("oad")
Name.append(123)
print(Name)

# remove  ===== 5
Name.remove("shivani")
print(Name)

 # if else   ===== 6
if "shivani" in Name:
    print("element is present")
else:
    print("not present")

# loop    ==== 7

for key in Name:
    print(key)

# range ======  8
for i in range(10):  # from 0 to last 2 element will be print
    print(i)
for i in range(5, 10): # from 1ele to last secend ele.
    print(i)
for i in range (5, 55, 5):
    print(i) # 5 10 15 ......50

 # len is use for count the length====   9
print(" ")
x = len(Name) # we will get total number of element no.


print(x)
for i in range(len(Name)):
    print(i) # we will get the element inder 0 1 2 3

for i in range(len(Name)):
    print(Name[i]) # we will get the all elements

# clear()  the list will be empty === 10
Name.clear()
print(Name)

# copy() ===  11 use to copy the list into another list name / variable
name = Name.copy()
print(name)
name.append("mohansing")
print(name)
print(Name)

# reverse() ==== 12
name.reverse()
print(name)

# count() ==== 13
number = [11,22,123, "55", "shivani", "oad", "55"]
n1 = number.count("55")
print(n1)


# extend
num1 = [ 11,22,33,]
num2 = ["a","b","c"]
num1.extend(num2)
print(num1)

# index ===== 14

q1 = "shivanioad"
q11= q1.index("i",1, 3)
print(q11)

#  find ===== 15

q2 = "shivanioad"
q22 = q2.index("i",5, 7)
print(q11)