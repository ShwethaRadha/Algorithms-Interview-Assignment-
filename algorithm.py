'''
Created on Dec 2, 2019

@author: shwethar
algorithm citation: https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/


'''

def isTriplet(ar, n): 
    j = 0
      
    for i in range(n - 2): 
        for k in range(j + 1, n): 
            for j in range(i + 1, n - 1): 
                # Calculate square of array elements 
                x = ar[i]*ar[i] 
                y = ar[j]*ar[j] 
                z = ar[k]*ar[k]  
                if (x == y + z or y == x + z or z == x + y): 
                    return 1
      
    # If we reach here, no triplet found 
    return 0
