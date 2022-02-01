# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 17:47:23 2022

@author: installadmin
"""

stock = [5,7,9,13,11,6,6,3,3]
def stockPairs(stocksProfit, target):
    pairs = []
    
    copy = stocksProfit[:]

    for i in stocksProfit:
        copy.remove(i)
        for j in copy:
            if i + j == target:
                a,b = i,j
                pairs.append((a,b))
        #copy.remove(i)
    print(pairs)
        
    use = []
    for i in pairs:
        if i not in use:
            use.append(i)

    return len(use)

    
print(stockPairs(stock, 12))

