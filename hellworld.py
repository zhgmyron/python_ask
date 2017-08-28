names=['mama','mike','jim']
def list_all(names):
    print("--------")
    for i in names:
        print (i)
list_all(names)
absent=names.pop(1)
print(absent+"can't present the party")
names.append('mao')
list_all(names)
names.insert(0,'ba')
names.insert(2,'di')
names.append("chou")

list_all(names)
a=names.pop()
print(a)
print ("--------------")
print (names)
b=len(names)
for i in range(b-3):
    print (i)
    del names[i]
print (names)