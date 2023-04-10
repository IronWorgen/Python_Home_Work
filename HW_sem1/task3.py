num = str(int(input("Введите номер билета: ")))

while(len(num)%2!=0):
    num = str(int(input("Введите номер билета: ")))

a=0
b=0

for i in range(len(num)//2):
    a+=int(num[i])
    b+=int(num[-i-1])

if (a==b):
    print ("YES")
else:
    print ("NO")