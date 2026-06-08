with open ("example.txt","r")as file:
    ##content = file.read()
    file1= file.readline()

print(file1)

with open ("example.txt","r")as file:
    lines= file.readlines()
    print(lines)