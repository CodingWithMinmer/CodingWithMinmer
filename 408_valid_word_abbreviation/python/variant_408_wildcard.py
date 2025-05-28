class Solution:
    def recurse(self, word, abbr, w, a):
        if w == len(word) and a == len(abbr): return True
        if w < len(word) and a == len(abbr): return False
        if w == len(word) and a < len(abbr):
            for c in abbr[a:]:
                if c != '*': return False
            return True

        if abbr[a].isdigit():
            skip = 0
            while a < len(abbr) and abbr[a].isdigit():
                skip = skip * 10 + int(abbr[a])
                a += 1
            w += skip
            return w <= len(word) and self.recurse(word, abbr, w, a)

        if abbr[a] == '*':
            return self.recurse(word, abbr, w, a+1) or self.recurse(word, abbr, w+1, a)

        if w < len(word) and word[w] == abbr[a]:
            return self.recurse(word, abbr, w + 1, a + 1)

        return False
    
    def validWordAbbreviation(self, word, abbr):
        return self.recurse(word, abbr, 0, 0)