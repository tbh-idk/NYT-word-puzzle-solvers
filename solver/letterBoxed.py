## letter boxed NYT ##

from random import shuffle

class unbox:
    
    def __init__(self, a,b,c,d, remove=None):
        '''
        Param a,b,c,d: tuple of 3 letters
        '''

        self.wl = list(open('/usr/share/dict/words'))
        wl = self.wl
        self.allLetters = [a[0],a[1],a[2], b[0],b[1],b[2], c[0],c[1],c[2], d[0],d[1],d[2]]

        if not remove: remove = []
        else:
            for x in remove:
                remove[remove.index(x)] = x+'\n'

        unbox.remove(self, *remove)
        for w in self.wl[:]:
            for l in w:
                if l not in self.allLetters and l != '\n':
                    self.wl.remove(w)
                    break
                
        # make sure the next letter is not in the same tuple
        for w in wl[:]:
            for l in range(len(w)-1):
                if (w[l] in a and w[l+1] in a) or (w[l] in b and w[l+1] in b) or (w[l] in c and w[l+1] in c) or (w[l] in d and w[l+1] in d):
                    self.wl.remove(w)
                    break

        # remove '\n'
        for w in wl:
            if w[-1] == '\n': wl[wl.index(w)] = w[:-1]

        #print(wl)

        #unbox.new(self)

    def remove(self, *words):
        for w in self.wl:
            if w in words: self.wl.remove(w)

    def new(self):

        shuffle(self.wl)
        wl = self.wl
        
        '''
        find the word with the most unique letters
        find the word that uses the most unused words
         - keep doing that until all letters are used
        '''

        self.chain = []
        lettersLeft = self.allLetters[:]
        
        top = {'score':0,'word':'placeholder'}
        # for this loop, the score is the number of unique letters
        for w in wl:
            s = set(w)
            if len(s) > top['score']:
                top['score'] = len(s)
                top['word'] = w
                
        self.chain.append(top['word'])
        #print(self.chain)
        for x in set(self.chain[-1]):
            try: lettersLeft.remove(x)
            except: pass

        # for this loop the score is the number of new letters
        while len(lettersLeft) > 0:
            top = {'score':0,'word':'placeholder'}
            for w in wl:
                if w[0] == self.chain[-1][-1]:
                    s = list(set(w))
                    for l in s[:]:
                        if not (l in lettersLeft): s.remove(l)
                    if len(s) > top['score']:
                        top['score'] = len(s)
                        top['word'] = w
                        
            self.chain.append(top['word'])
            #print(self.chain)
            for x in set(self.chain[-1]):
                try: lettersLeft.remove(x)
                except: pass

        return(self.chain)

    def using(self, *words):
        
        shuffle(self.wl)
        wl = self.wl
        
        '''
        like unbox.new but with starting words already chosen
        '''
        
        self.chain = []
        lettersLeft = self.allLetters[:]
        
        for w in words:
            self.chain.append(w)
            for l in w:
                try: lettersLeft.remove(l)
                except: pass

        # for this loop the score is the number of new letters
        while len(lettersLeft) > 0:
            top = {'score':0,'word':'placeholder'}
            for w in wl:
                if w[0] == self.chain[-1][-1]:
                    s = list(set(w))
                    for l in s[:]:
                        if not (l in lettersLeft): s.remove(l)
                    if len(s) > top['score']:
                        top['score'] = len(s)
                        top['word'] = w
                        
            self.chain.append(top['word'])
            #print(self.chain)
            for x in set(self.chain[-1]):
                try: lettersLeft.remove(x)
                except: pass

        return(self.chain)

    
        
