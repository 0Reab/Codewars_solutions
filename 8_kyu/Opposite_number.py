'''
Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:
```
1: -1
14: -14
-34: 34
```

~~~if:sql
You will be given a table: `opposite`, with a column: `number`. Return a table with a column: `res`.
~~~

'''

def opposite(number):
        return number - number * 2
