## spelling bee NYT ##
import time as t

class hive:

    def __init__(self, center, *Other):
        self.wordlist = list(open('/usr/share/dict/words'))

        center = center.lower()
        
        if len(Other) == 1 and type(Other[0]) is list:
            other = Other[0]
        else:
            other = []
            for x in Other:
                other.append(x.lower())

                
        s = t.time()
        

        print('*', end='')
        for w in self.wordlist[:]:
            if not(center in w) or len(w) <= 4:
                self.wordlist.remove(w)
                
        print('******', end='')
        for w in self.wordlist[:]:
            for l in w:
                if (not(l in other) and not(l == center)) and l != '\n':
                    self.wordlist.remove(w)
                    
                    break
        print('*', end='')
        for w in self.wordlist[:]:
            self.wordlist[self.wordlist.index(w)] = self.wordlist[self.wordlist.index(w)].removesuffix('\n')

        print('*')

            
        e = t.time()


        print(f'words : {len(self.wordlist)}')
        print(f'{round(e-s,4)} seconds')

    def all(self):
        print(self.wordlist)

    def search(self, start=None, length=None):
        if start and not(length):
            for w in self.wordlist:
                if w.startswith(start):
                    print(w)

        elif not(start) and length:
            for w in self.wordlist:
                if len(w) == length:
                    print(w)

        elif start and length:
            for w in self.wordlist:
                if w.startswith(start) and len(w) == length:
                    print(w)

    def pangram(self):
        for w in self.wordlist:
            if len(set(w)) == 7:
                print(w)
