'''
An **anagram** is the result of rearranging the letters of a word to produce a new word (see [wikipedia](https://en.wikipedia.org/wiki/Anagram)).

**Note:** anagrams are case insensitive

Complete the function to return `true` if the two arguments given are anagrams of each other; return `false` otherwise.


## Examples

* `"foefet"` is an anagram of `"toffee"`

* `"Buckethead"` is an anagram of `"DeathCubeK"`

'''

# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())