'''
计算两个非负正数p和q的最大公约数：
若q是0，则最大公约数为p。否则，将
p除以q的到的余数r，p和q的最大公约
即为q和r的最大公约数。故用递归的方法。
'''
def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)

if __name__ == '__main__':
	print gcd(24, 8)