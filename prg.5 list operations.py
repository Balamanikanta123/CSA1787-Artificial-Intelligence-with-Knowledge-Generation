a=["python","c","c++","java"]
print("length:",len(a))
b=["javascript","C#","ruby"]
print("concatenation:",a+b)
#iteration
for word in a:
    print(word)
#slicing
print(a[1:3])
print(b[:])
#indexing
print(a[0])
print(b[2])
#nested list
c=[1,2,[3,5],6]
print(c[2][1])
#membership
print('c' in a)
print('ruby' in b)