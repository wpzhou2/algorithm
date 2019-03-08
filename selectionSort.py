#选择排序
#在一组杂乱无序的数组中，先选一个最小的放在新的数组中
#然后在原数组弹出这个最小数，然后继续选一个最小值放入新数组中
#重复操作，最后得到一个排序的数组
#时间复杂度为O（n²）

def findSmallest(arr):
    smallest = arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest=arr[i]
            smallest_index=i
    #返回最小数的位置
    return smallest_index

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        # 得到最小数的位置
        smallest_index = findSmallest(arr)
        # 得到最小数
        smallest = arr.pop(smallest_index)
        newArr.append(smallest)
    return newArr

print(selectionSort([5,3,6,2,10]))
