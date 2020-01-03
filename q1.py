'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    # implement here
    cnt = 1
    c = [b for b in  [digitarray[i:i + x + 1] for x in range(len(digitarray)) for i in range(len(digitarray) - x)] if len(b)==2 and int(b)>=0 and int(b)<=25 and not b.startswith('0')]
    print cnt+len(c)
