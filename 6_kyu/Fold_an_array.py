'''
In this kata you have to write a method that folds a given array of integers by the middle x-times.

An example says more than thousand words:
```
Fold 1-times:
[1,2,3,4,5] -> [6,6,3]

A little visualization (NOT for the algorithm but for the idea of folding):

 Step 1         Step 2        Step 3       Step 4       Step5
                     5/           5|         5\          
                    4/            4|          4\      
1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
----*----      ----*          ----*        ----*        ----*


Fold 2-times:
[1,2,3,4,5] -> [9,6]
```

As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null. The parameter runs will always be a positive integer greater than 0 and says how many runs of folding your method has to do.

If an array with one element is folded, it stays as the same array.

The input array should not be modified!

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
'''

def fold_array(array, runs):
    tmp_arr = array[:] # copy

    while runs > 0:
        l = len(tmp_arr)

        if l % 2 == 0: # is even
            left, right = tmp_arr[:int(l/2)] , tmp_arr[int(l/2):][::-1] # split arr in half
            tmp_arr = [a + b for a, b in zip(left, right)] # addition
            runs -= 1 # decrement

        else: # is odd
            if l == 1:
                return [sum(tmp_arr)]

            m_idx = int(l / 2 - 0.5)
            middle = tmp_arr[m_idx]
            tmp = tmp_arr[:m_idx] + tmp_arr[m_idx+1:] # arr without middle value 
            l = len(tmp) # update len

            left, right = tmp_arr[:int(l/2)] , tmp_arr[int(l/2)+1:][::-1] # split arr in half
            tmp_arr = [a + b for a, b in zip(left, right)] # addition
            tmp_arr.append(middle)
            runs -= 1 # decrement

    return tmp_arr