for i in range(30,20,2):
    print(i)

for i in range(1,20,):
    print(i)

list = ["Geati","Gerti","Adonisi","Resa"]

for i in list:
    print(i)

print("-----------------")
for i in list:
    print(i)
    if i =="Gerti":
        break

print("-----------------")

for i in list:
    if i =="Adonisi":
        continue
    print(i)

