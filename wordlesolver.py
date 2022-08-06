
'''
wordle solver:

'''

##import requests
##from bs4 import BeautifulSoup
from random import randint as random
import math as m

'''''''''''''''''''''
#   old word list   #
'''''''''''''''''''''
##page = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
##soup = BeautifulSoup(page.content, 'html.parser')
##
############################
##
##wordlistAll = str(soup).split('\n') # type list
##wordlist = []
##
##for x in wordlistAll:
##    if len(x) == 5:
##        wordlist.append(x)
##
########################################


'''''''''''''''''''''
#   new word list   #
'''''''''''''''''''''
wordlist = []

wordlistAll = open('/usr/share/dict/words')
wordlistAll = list(wordlistAll)

for x in wordlistAll:
    if len(x.strip()) == 5 and x[0].islower():
        wordlist.append(x.strip())
######################################

def remove(string, strict=True, *args):
    string = list(string)
    if strict:
        for l in args:
            while True:
                try: string.remove(l)
                except ValueError: break
    else:
        for l in args:
            try: string.remove(l)
            except ValueError: pass
    return(str(''.join(x for x in string)))
    
        
class wordle:
    def __init__(self, green='*****', yellow='*****', grey=[]):
        '''
        Param green: position of green letters. use '*' for unknown. e.g., '*ince'. type string
        Param yellow: list of yellow letters. use '*' for green or grey letters
        Param grey: list of letters not in word
        '''
        self.possible = []
        self.yellow = {} # {char:[indexes]}
        
        if type(green) is str: self.template = green
        else: raise(TypeError('Param "green" must be type string'))
        
        if type(yellow) is str: wordle.addYellow(self, yellow)
        else: raise(TypeError('Param "yellow" must be type string'))
        
        if type(grey) is list: self.grey = grey
        else: raise(TypeError('Param "grey" must be type list'))

        self.green = []
        for x in self.template:
            if x != '*':
                self.green.append(x)

        wordle.solve(self)

    def update(self, green=None, yellow=None, grey=None):
        '''
        Param green: position of green letters. use '*' for unknown. e.g., '*ince'. type string
        Param yellow: position of yellow letters. use '*' for green or grey letters. type string
        Param grey: list of letters not in word
        '''
        self.possible = []
        if type(green) is str: self.template = green
        else: raise(TypeError('Param "green" must be type string'))
        
        if type(yellow) is str: wordle.addYellow(self, yellow)
        else: raise(TypeError('Param "yellow" must be type string'))
        
        if type(grey) is list: wordle.addGrey(self, *grey)
        else: raise(TypeError('Param "grey" must be type list'))

        self.green = []
        for x in self.template:
            if x != '*':
                self.green.append(x)

        wordle.solve(self)

    def addYellow(self, string):
        for x in string:
            if x in self.yellow:
                self.yellow[x].append(string.index(x))
            elif x not in self.yellow and x != '*':
                self.yellow[x] = [string.index(x)]
    def addGrey(self, *args):
        for x in args:
            if not(x in self.yellow) and not(x in self.template): self.grey.append(x)

    def solve(self):
        self.possible.clear()
        
        for x in wordlist: # matches the green letters
            matches = 0
            for n in range(0,5):
                if (self.template[n] != '*') and (x[n] == self.template[n]):
                    matches += 1
            if matches == 5-(list(self.template).count('*')):
                self.possible.append(x)

        for x in self.possible[:]: # removes words that contain grey letters
            for l in self.grey:
                if l in x:
                    self.possible.remove(x)
                    break

        for x in self.possible[:]: # removes words that do not contain the yellow words
            for l in self.yellow:
                if l not in x:
                    self.possible.remove(x)
                    break
        for x in self.possible[:]: # remoe words where yellow letters cannot be
            for l in self.yellow:
                if x.index(l) in self.yellow[l]:
                    self.possible.remove(x)
                    break

        if len(self.possible) <= 5 and len(self.possible) > 0: print('\n'.join(w for w in self.possible))
        elif len(self.possible) <= 0: print('there is no solution. try again next time')
        else: print(f'number of possible solutions is too great ({len(self.possible)})')

    def suggestion(self,r=False):
        #global rankedWords, frequency
        if False or r: # len(self.possible) >= 1000
            print(self.possible[random(0,len(self.possible)-1)])
        else:
            '''
            make new version:
              - [x] suggest words that have common letters
              - [ ] suggest words that have more unique letters
            '''
            letterScore = [*'etaoinshrdlucmfwypvbgkjqxz'] # not weighted

            rankedWords = [('eeeee',0),('zzzzz',m.inf)] #('zzzzz',m.inf)

            ##
##            for x in self.possible:
##                #print(rankedWords)
##                score = 0
##                for l in x:
##                    if self.template[x.index(l)] == '*':
##                        score += letterScore.index(l)
##                for n in rankedWords[:]:
##                    if score < n[1]:
##                        rankedWords.insert(rankedWords.index(n)-1,(x, score))
##                        break

            ##
                    
##            for x in self.possible:
##                score = []
##                for l in x:
##                    if l not in self.green:
##                        score.append(l)
##                score = list(set(score))
##
##                for n in score:
##                    score[score.index(n)] = letterScore.index(n)
##
##                score = sum(score)
##
##                for n in rankedWords[:]:
##                    if score < n[1]:
##                        rankedWords.insert(rankedWords.index(n)-1,(x, score))
##                        break
            ##
            rankedWords = {}

            frequency = {}
            for x in self.possible:
                w = remove(x, False, *self.green)
                w = remove(w, False, *self.yellow)
                for l in w:
                    if l not in frequency:
                        frequency[l] = 0
                    frequency[l] += 1
            frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
            print(frequency)

            for x in self.possible:
                w = remove(x, *self.green)
                w = remove(w, *self.yellow)
                w = (''.join(i for i in set(w)))
                score = 0
                for l in w:
                    try: score += frequency[l]
                    except KeyError: pass
                try: score /= len(w)
                except ZeroDivisionError:
                    print('ZDE')
                    print(w)
                rankedWords[x] = score
            
            rankedWords = dict(sorted(rankedWords.items(), key=lambda item: item[1]))
                    

            #print('\n'.join(x for x in list(rankedWords)[-5:]))
            sug = list(reversed(list(rankedWords)))
            print('\n'.join(f'{x} : {rankedWords[x]}' for x in sug[:5]))
            self.rw = rankedWords#
            self.s = sug

    def more(self):
        frequency = {}
        for w in self.possible:
            for l in w:
                if l in frequency: frequency[l] += 1
                else: frequency[l] = 1
        print(frequency)#
        rankedWords = {}
        for x in wordlist:
            w = ''.join(l for l in set(x))

            rankedWords[x] = 0
            for l in w:
                try: rankedWords[x] += frequency[l]
                except KeyError: pass
        rankedWords = dict(sorted(rankedWords.items(), key=lambda item: item[1]))
        print('\n'.join(f'{x} : {rankedWords[x]}' for x in list(reversed(list(rankedWords)))[:5]))
        self.m = list(reversed(list(rankedWords)))
        
                
            

            
