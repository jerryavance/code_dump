# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 11:22:28 2022

@author: installadmin
"""
l = 5
r = 9

    
def oddNumbers(l, r):
    # Write your code here
    use = [l]
    result = []
    while l < r:
        l += 1
        use.append(l)
    for i in use:
        if i % 2 != 0:
            result.append(i)
    return result

    
print(oddNumbers(l, r))

#if __name__ == '__main__':