#快速排序，常用排序方法，D&C(分而治之)典范

#使用递归的方法
# 1.选定数组中某个值作为基准值
# 2.将数组分为两个小组，一小组全都大于该基准值，另一组全小于
# 3.对两个小组也进行快速排序
# 4.将排好序的两个小组以及基准值进行合并

# 快速排序每层都要全遍历，最佳层数是每次基准值都对半开，即有log n层，最糟情况有 O(n) 层
# 最糟情况下，运行时间为O（n²）
# 最佳/平均情况下，运行时间为O（n log n）
# 合并排序的运行时间也为O（n log n），但快速排序的常量比较小，故一般选用快速排序

# 基准值的选择极为重要，实际上最好每次都随机选数组中的一个数作为基准值最好

def quicksort(array):
    #基线条件：当数组只有0个或1个元素则有序，直接返回
    if len(array)<2:
        return array
    else:
        pivot=array[0] #暂选择数组第一个元素作为基准值
        # 将数组分为两个小组，一小组全都大于该基准值，另一组全小于
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>=pivot]
        #对两个小组也进行快速排序，并将排好序的两个小组以及基准值进行合并
        return quicksort(less)+[pivot]+quicksort(greater)

print(quicksort([10,5,2,3]))