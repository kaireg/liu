#coding:utf-8

#选择排序

def xzpx(arr):
    for i in range(0,len(arr)):
        k = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i],arr[k] = arr[k],arr[i]
        print(arr)

abc = [5,9,48,156,4,7,456]
xzpx(abc)

