# list ==1
# 1. allow duplicat element
# 2. changeable
# 3. ordered
# 4. constructed into []
#         0        1  2  3   4
List = ["shiv","oad",11,22, 7.8, "oad"]
print(List, (len(List)))
print(List[2])
for i in List:
    print(i)

#     TUple == 2
# 1. allow duplicat value
# 2. not changeable
# 3.ordered collection
# 4. () round bracket
Tuple = ('shivani',11, 11,23,90.9,"oad")
print(Tuple, (len(Tuple)))
print(type(Tuple))
Tuple1 = ("shivani")
print(type (Tuple1))# o/p string
Tuple2 = ("shivani",)
print(type(Tuple2)) # o/p bcz comma given after the element
for i in Tuple:
    print(i)
print(" ")


# set ==3
# 1. not allow duplicat value
# 2. not changeable but by index changeable
# 3. unordered
# 4.  {} curly bracket
Set = {"shivani",11,22,33,11,"oad" ,9.9 } # 7
print(Set,(len(Set))) # it 7 length but show 6 bcz set not allow the duplicat value
for i in Set:
    print(i)
Set.update([111,222,333])
print(Set)
# not able to retrieve or update the element



#  Dictionary == 4
# 1. not allow duplicate value contain key and value pairs
# 1. changeable
# 3. unordered
# 4. {}

Dict = {
    "Name:":"shivani",
    "Age:":"23",
    "subject:":"python"
}
# print(Dict[1])
for i in Dict:
    print(i, Dict[i])
print(Dict["Name:"])




