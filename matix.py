import numpy as np
'''


print("order of matrix 1")
m=int(input("row"))
n=int(input("coll"))
mst1 = []
for i in range(m):
    row = list(input("enter the row " , i ) )
    mst1.append(row)


print("order of matrix 2")
m1=int(input("row"))
n1=int(input("coll"))
mst2 = []
for i in range(m1):
    row = list(input("enter the row " , i ) )
    mst2.append(row)

print("matrix multiplication")

pro = np.dot(mst1,mst2)
print(pro)

    
'''

print("enter order of matrix 1")
# m , n =list(map(int , input().split()))
m = int(input("enter row"))
n = int(input("enter coll"))
print("enter row wise values")
mat1=[]
print(type(m))
for i in range(m):
    print("enter the row" ,i)
    # row = list(map(int , input().split()))        #map function int() to every string integer input;  <-<-<-<-<-<-
    row = list(input("enter the row").split())
    mat1.append(row)
print(mat1)