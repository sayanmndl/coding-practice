class Master:
    def guess(self, word: str) -> int:
        pass

class Solution:
    def findSecretWord(self, words: list[str], master: 'Master') -> None:

        def matches(a,b):
            return max(x==y for x,y in zip(a,b))

        candidates = words[:]
        while candidates:
            best_word = None
            best_score = float('inf')
            for word in candidates:
                groups = [0]*7

                for other in candidates:
                    m = matches(word, other)
                    groups[m]+=1

                score = max(groups[:6])
                if score < best_score:
                    best_score = score
                    best_word = word
            
            result = master.guess(best_word)
            if result == 6:
                return
            candidates = [
                word for word in candidates
                if matches(word, best_word) == result
            ]