'''
The number ```$89$``` is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. 
What's the use of saying "Eureka"? Because this sum gives the same number: ```$89 = 8^1 + 9^2$```

The next number in having this property is ```$135$```:

See this property again: ```$135 = 1^1 + 3^2 + 5^3$```


## Task ##

We need a function to collect these numbers, that may receive two integers ```$a$```, ```$b$``` that defines the range ```$[a, b]$``` (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.


## Examples ##

Let's see some cases (input -> output):
```
1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
```

If there are no numbers of this kind in the range `$[a, b]$` the function should output an empty list.
```
90, 100 --> []
```
Enjoy it!!


'''

def sum_dig_pow(a, b):
    arr = [] # default return

    for i in range(a, b+1): # inclusive range
        if i > 9: # for multi digit nums
            tmp = 0 # var for summing
            num = [ i for i in str(i)] # int 99 turns into ['9', '9']

            for idx, digit in enumerate(num):
                idx += 1 # counting from one
                tmp += int(digit) ** idx # example: 9 ** 1 then 9 ** 2

            if tmp == int(''.join(num)): # compare calculated num with var i
                arr.append(tmp)
        else: # for single digit nums
            arr.append(i)

    return arr