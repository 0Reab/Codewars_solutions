'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

## Examples

```javascript
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
```
```objc
pigIt(@"Pig latin is cool"); // => @"igPay atinlay siay oolcay"
pigIt(@"Hello world !");     // => @"elloHay orldway !"
```
```ruby
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```
```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```
```csharp
Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
Kata.PigIt("Hello world !");     // elloHay orldway !
```
```C++
pig_it("Pig latin is cool");   // igPay atinlay siay oolcay
pig_it("Hello world !");       // elloHay orldway
```
```Java
PigLatin.pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
PigLatin.pigIt('Hello world !');     // elloHay orldway !
```
```clojure
(piglatin/pig-it "Pig latin is cool") ; "igPay atinlay siay oolcay"
(piglatin/pig-it "Hello world !")     ; "elloHay orldway !"
```
```typescript
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
```
```cobol
      PigIt str = 'Pig latin is cool' => result = 'igPay atinlay siay oolcay'
      PigIt str = 'Hello world !'     => result = 'elloHay orldway !
```

'''

def pig_it(text):
    return ' '.join([i[1:]+i[0]+'ay' if not i.endswith(('!','?','.')) else ' '.join([i[1:]+i[0]]) for i in text.split(' ')])