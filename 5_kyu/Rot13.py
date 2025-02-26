'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

```if:python
Please note that using `encode` is considered cheating.
```

```if:r
**Note:** As R is a natively vectorized language, you should write `rot13()` such that the argument `x` may be a character vector of any length. The return value should always be a character vector of the same length as `x`.
```

'''

def rot13(message):
    result = ''

    for char in message:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))

        elif ord('A') <= ord(char) <= ord('Z'):
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))

        else:
            result += char

    return result