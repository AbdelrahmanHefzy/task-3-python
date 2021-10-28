import math
def perfect (list,x,y):
    list_0=[]
    for i in range (list):
        X=int(input())
        list_0.append(X)
    print(list_0)
    for j in list_0:
        if(math.sqrt(j))*(math.sqrt(j)) ==float(j):
            if j>=x and j<=y:
                perf.append(j)
perf=[]
list=int(input("Enter Numbers Of Items You Want To Add To The List :"))
x=int(input("Enter The Start OF The Range :"))
y=int(input("Enter The End OF The Range :"))
perfect(list,x,y)
print(perf,"Are Perfect Number/s.")
