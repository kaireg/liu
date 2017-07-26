#coding:utf-8

#快速排序
def kp(arr,i,j):
    if i < j:
        base = kpgc(arr,i,j)
        kp(arr,i,base)
        kp(arr,base+1,j)

def kpgc(arr,i,j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i

a = [1,9,4,45,89,456,100]
kp(a,0,len(a)-1)
print(a)