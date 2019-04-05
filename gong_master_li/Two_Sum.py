print('............................S010101............................')
#LeetCode
#两数之和,数组nums中两数之和等于target,返回两数数组下标
import random
def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    aa=[(nums.index(m),len(nums)-nums[::-1].index(n)-1) for m in nums for n in nums[:] if m+n==target and m==n and nums.index(m)!=len(nums)-nums[::-1].index(n)-1]#选择1.4.6,过滤7
    bb=[(nums.index(m),nums[:].index(n)) for m in nums for n in nums[:] if m+n==target and nums.index(m)<nums[:].index(n)]#选择1.2.3.5.7.8.9

    if max(nums)>1000:print(max(nums))
    print([list(x) for x in set(aa+bb)])


twoSum([2,2,1,3],4)#1
twoSum([2,7,11,15],9)#2
twoSum([4,7,4,5],12)#3
twoSum([4,7,4,15],8)#4
twoSum([2,5,4,3],7)#5
twoSum([4,7,4,15,3,3],8)#6
twoSum([2,1,3],4)#7
#twoSum(list(range(60600))[::3],58056)#8#运行时间67.4s
#twoSum(list(range(36700))[::3],24528)#9#运行时间22.0s
twoSum(list(range(random.randint(25000,45000)))[::3],24528)
print('............................S010101............................')


print('............................S010102............................')
#LeetCode
#两数之和,数组nums中两数之和等于target,返回两数数组下标

'a test module'
#文档注释,print('..Sxx..')删除,否则print(__doc__)#None
import os

def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res=[]
    for i in range(len(nums)):
	    if res!=[]:break
	    for j in range(i+1,len(nums)):
	        if nums[i]+nums[j]==target:
	    	    res.append(i)
	    	    res.append(j)
	    	    break
    print(res)

twoSum([2,2,1,3],4)
twoSum([2,7,11,15],9)
twoSum([4,7,4,5],12)
twoSum([4,7,4,15],8)
twoSum([2,5,4,3],7)
twoSum([4,7,4,15,3,3],8)
twoSum([2,1,3],4)
twoSum(list(range(60600))[::3],58056)
twoSum(list(range(36700))[::3],24528)
print(__doc__)#a test module
print(__file__)#C:/EDisk/BT_1/Python3Gong/gtemp2.py
#相对路径,注意与绝对路径,斜杠反斜杠区别
s1=os.path.abspath(__file__)#需要import os
#绝对路径
s2=os.path.dirname(s1)
print(s1)#C:\EDisk\BT_1\Python3Gong\gtemp2.py
print(s2)#C:\EDisk\BT_1\Python3Gong
#sys.path.append(s2)#添加搜索目录,需要import sys
print('............................S010102............................')

