'''
Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

## Examples
```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```
'''

def reverse_words(txt):
    return ' '.join([ i[::-1] for i in txt.split(' ')])