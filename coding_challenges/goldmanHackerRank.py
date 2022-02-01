# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 16:38:50 2022

@author: installadmin
"""

def plusMult(A):
    # Write your code here
    for i in range(0,len(A),2):
        print(i)
    print("done")
    for j in range(1,len(A),2):
        print(j)
 
#A = [1,2,3,4,5,5,6,6,6]
#print(plusMult(A))

A = [12,3,5,7,13,12]
#A = [10,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

def test(A):
    use = []
    for i in range(0,len(A),2):
        use.append(i)
    val = use[2:]
    ans = A[0]*A[2]
    count1 = 1
    for i in val:
        if count1%2 != 0:
            ans += A[i]
            count1+=1
        else:
            ans *= A[i]
            count1+=1
    #print(ans)
    result1 = ans % 2
    
    use2 = []
    for j in range(1,len(A),2):
        use2.append(j)
    val = use2[2:]
    ans2 = A[1]*A[3]
    count1 = 1
    for i in val:
        if count1%2 != 0:
            ans2 += A[i]
            count1+=1
        else:
            ans2 *= A[i]
            count1+=1
    #print(ans2)
    result2 = ans2 % 2
    
    if result2 > result1:
        return "ODD"
    elif result1 > result2:
        return "EVEN"
    elif result1 == result2:
        return "NEUTRAL"
    
    
print(test(A))
    
