import random
size = int(input("Введите количество монет: "))
list=[]
for i in range(size):
    list.append(random.randint(0,1))
print(list)

orel=0
reshka=0
for i in range(len(list)):
    if (list[i]==0):
        orel+=1
    else :
        reshka+=1

if (orel>reshka):
    print(reshka)
else:
    print(orel)