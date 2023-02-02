a=[1,2,3,4]
a.append(5)
print("list after appending:",a)
b=[6,7]
b.extend(a)
print("list after extending:",b)
a.remove(4)
print("list after deleting:",a)
a.insert(2,8)
print("list after adding:",a)
