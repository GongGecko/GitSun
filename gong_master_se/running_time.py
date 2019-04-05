print('............................S010101............................')
#运行时间
import time

start_timeA=time.time()
start_timeB=time.clock()
print('............................Sxxxxxx............................')
a1=set(list(range(90900))[::3]) & set(list(range(30600))[::7])#集合交集
a2=[x for x in a1]
a3=sorted(a2)
print(a1)
print(a2)
print(a3)
print('............................Sxxxxxx............................')
stop_timeA=time.time()
stop_timeB=time.clock()
running_timeA=stop_timeA-start_timeA
running_timeB=stop_timeB-start_timeB
running_timeAA=running_timeA*1000
running_timeBB=running_timeB*1000
print(start_timeA)
print(stop_timeA)
print(start_timeB)
print(stop_timeB)

if running_timeA>=10:
    print('running_timeA: %.6f s' % running_timeA)
else:
    print('running_timeA: %.3f ms' % running_timeAA)

if running_timeB>=10:
    print('running_timeB: %.6f s' % running_timeB)
else:
    print('running_timeB: %.3f ms' % running_timeBB)
print('............................S010101............................')



