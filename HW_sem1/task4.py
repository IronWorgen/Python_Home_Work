#   Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#   если разрешается сделать один разлом по прямой между дольками

m=int(input("Введите n "))
n=int(input("Введите m "))
k = int(input("Введите k "))

if (k%n==0  ):
    if(k//n<m):
        print("yes")
    else: 
        print("no")
elif(k%m==0):
    if(k//m<n):
        print("yes")
    else: 
        print("no")
else: 
    print("no")
