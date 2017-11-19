### Primitive types
# Integer values variable
x = 5

print(x)
print(2*x)

# Real-valued variable
y = 2.5 # float

print(y)

# Text-valued variable
s = "Bahar Bazargan" #string

print(s)

# Array-valued variable
array = ["Nazanin Nader","Bahar Bazargan"]

print(array)

array.append("Nima Hamidi")
array.append("Ali Bitaraf")

# or in one command
array.extend(["a","b"])

print(array)

array.extend("taghi")

print(array)

# Dictionary
d = {"nima":5,"nazanin":6.5,"bahar":[4,2,4,1,2,4,3,1]}

print(d)
# End of Primitive types


# Conditionals
if y > 0:
    print(y)
else:
    print(-y)

y=-3.7

if y > 0:
    print(y)
else:
    print(-y)

# Loop
print("Before for")
for i in array:
    print(i)

print("")
print("Printing keys of dictionary:")
for k in d.keys():
    print(k)
for j in d.values():
    print(j)

print("Printing items of dictionary:")
for k in d.keys():
    print(k, ": ", d[k])

# This way is more pythonic:
for k,v in d.items():
    print(k, ":", v)



