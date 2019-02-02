import re,logging
from decimal import *
logging.basicConfig(level=logging.WARNING)# .INFO.WARNING.ERROR

units=['B','K','M','G','T','P','E','Z','Y']
decimalx,binaryx=(1000,1024)

def human2bytes(numit,base=binaryx):
    """Convert human readable size to the bytes
    `numit`: the human readable size
    Using the `binaryx` base, with a factor 1024
    >>> human2bytes('35B')
    (35, 'B')
    >>> human2bytes('   1.0k')
    (1024, 'B')
    >>> human2bytes('35 mB')
    (36700160, 'B')
    >>> human2bytes('  35.0Mb  ')
    (36700160, 'B')
    >>> human2bytes('35 GB')
    (37580963840, 'B')
    >>> human2bytes('35.0000001 GB')
    (37580963947, 'B')
    >>> human2bytes('35 TB')
    (38482906972160, 'B')
    >>> human2bytes('35 pib')
    (39406496739491840, 'B')
    >>> human2bytes('35 eb')
    (40352252661239644160, 'B')
    >>> human2bytes('35 zb')
    (41320706725109395619840, 'B')
    >>> human2bytes('35yb')
    (42312403686512021114716160, 'B')

    Using the `decimalx` base, with a factor 1000
    >>> human2bytes('35B',base=decimalx)
    (35, 'B')
    >>> human2bytes('   1.0k',base=decimalx)
    (1000, 'B')
    >>> human2bytes('35 mB',base=decimalx)
    (35000000, 'B')
    >>> human2bytes('  35.0Mb  ',base=decimalx)
    (35000000, 'B')
    >>> human2bytes('35 GB',base=decimalx)
    (35000000000, 'B')
    >>> human2bytes('35.0000001 GB',base=decimalx)
    (35000000100, 'B')
    >>> human2bytes('35 TB',base=decimalx)
    (35000000000000, 'B')
    >>> human2bytes('35 pib',base=decimalx)
    (35000000000000000, 'B')
    >>> human2bytes('35 eb',base=decimalx)
    (35000000000000000000, 'B')
    >>> human2bytes('35yb',base=decimalx)
    (35000000000000000000000000, 'B')
    >>> human2bytes('350000000000000000yb',base=decimalx)
    (350000000000000000000000000000000000000000, 'B')
    """
    # 非负浮点数：^\d+(\.\d+)?$
    # units：^[BKMGTPEZY](B|IB)?$
    mth=re.match(r'^\s*(\d+(\.\d+)?)\s*([BKMGTPEZY])(B|IB)?\s*$',numit.upper())
    if mth!=None:
        getcontext().prec=52
        value1=Decimal(mth.group(1))
        unia=mth.group(3)
        logging.info('mth.groups() is %s' % str(mth.groups()))
        res=int(value1*(Decimal(base)**Decimal(units.index(unia))))
        logging.info('type(units.index(unia)) is %s' % type(units.index(unia)))
        return (res,'B')
    else:
        raise Exception("str include number and units:'2M','3.1MB','0.4 MiB';")



def bytes2human(numis,humann=0.9,base=binaryx):
    """Convert the bytes to the human readable size
    Using the `binaryx` base, with a factor 1024
    >>> bytes2human('999899999b')
    (0.93, 'G')
    >>> bytes2human(' 1024 b')
    (1.0, 'K')
    >>> bytes2human(' 1048576 b')
    (1.0, 'M')
    >>> bytes2human(' 938700 b')
    (916.7, 'K')	
    >>> bytes2human(' 957700 b')
    (0.91, 'M')
    >>> bytes2human('0000001007')
    (0.98, 'K')
    >>> bytes2human('42312403686512021114716160')
    (35.0, 'Y')

    Using humann=1, with regular mode
    >>> bytes2human('999899999b',humann=1)
    (953.58, 'M')
    >>> bytes2human(' 938700 b',humann=1)
    (916.7, 'K')	
    >>> bytes2human(' 957700 b',humann=1)
    (935.25, 'K')
    >>> bytes2human('0000001007',humann=1)
    (1007.0, 'B')
	
    Using the `decimalx` base, with a factor 1000
    >>> bytes2human('999899999b',humann=1,base=decimalx)
    (999.9, 'M')
    >>> bytes2human(' 938700 b',humann=1,base=decimalx)
    (938.7, 'K')	
    >>> bytes2human(' 957700 b',humann=1,base=decimalx)
    (957.7, 'K')
    >>> bytes2human('0000001007',humann=1,base=decimalx)
    (1.01, 'K')
    """
    # 非负整数：^\d+$
    mtx=re.match(r'^\s*(\d+)\s*(B|b)?\s*$',numis)
    if mtx!=None:
        value2=float(mtx.group(1))# 若25位以上整数,会丢失精度,但此函数就是牺牲精度为可读性
        i=0
        while value2>=base*humann:
            value2=value2/base
            i+=1
        return (round(value2,2),units[i])
    else:
        raise Exception("str include int number and units:'323B','12b','72182';")



if __name__=='__main__':
    print(human2bytes('917.15Mb'))# (961701478, 'B')
    print(bytes2human('961706570 b'))# (917.15, 'M')
    print(human2bytes('35 Yb',base=decimalx))# (35000000000000000000000000, 'B')
    print(bytes2human('431240368652120211147161604'))# (356.71, 'Y')















