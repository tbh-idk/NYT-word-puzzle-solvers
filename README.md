# NYT word puzzle solvers
Helps suggest words and solutions for Wordle, Spelling Bee, and Letter Boxed.

All these would be done in the IDLE shell

## Wordle

- **Innitialize solver object**
``` python
new = wordle()
```
- **Update the object based on information gained**
```
update(self, green='', yellow='', grey=[])
```
ex.
```python
>>> new.update('**i**','*a**e',['r','s'])
```
-
  - *Param green: position of green letters. use '*' for yellow or grey letters.*
  - *Param yellow: position of yellow letters. use '*' for green or grey letters.*
  - *Param grey: list of letters not in word*
  
- **Get suggestions**
  - suggestion
  ```
  suggestion(self)
  ```
  
  - more
  ```
  more(self)
  ```
  
  - *these two methods are similar, but keep in mind that the words suggested from the 'more' function may include letters that are in the worng place or not in the word*
  - *find a full ordered list at ```self.s``` and ```self.m```*

## Spelling Bee

- Create solver object
```
hive(self, center, *Other)
```
ex.
```python
bee = hive('T','C','I','L','M','N','O')
```

- find words
```
search(self, start='', length=None)
```

- find pangrams
```
pangram(self)
```



## Letter Boxed

- Create solver object
```
unbox(self, a,b,c,d)
```
ex.
```python
box = unbox(('r','b','a'),('i','u','g'),('y','m','o'),('c','n','l'))
```

- get suggestions
```
new(self)
```

- remove word(s) that are not accepted
```
remove(self, *words)
```

- start with certain word(s)
```
using(self, *words)
```
