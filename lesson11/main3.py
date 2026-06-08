import os

lines = ["hello world\n","welcome to python\n"]

with open("example2.txt","w")as file:
    #file.write("Resa kete resht deshiron ta shenoj ne file named example2")
    file.writelines(lines)

if os.path.exists("example2.txt"):
    print("example2.txt exists")