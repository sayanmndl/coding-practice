from typing import List, Dict

class Solution:
    def applySubstitution(self, replacements, text):
        values = {key: value for key, value in replacements}
        memo = {}

        def resolve(key):
            # already completely resolved
            if key in memo:
                return memo[key]
            
            s = values[key]
            result = []
            i = 0

            while i < len(s):
                if s[i] != "%":
                    result.append(s[i])
                    i+=1
                    continue

                j = s.find("%", i+1)
                nested_key = s[i+1: j]
                # recursively resplve nested variable
                result.append(resolve(nested_key))
                i = j+1
            memo[key] = "".join(result)
            return memo[key]

        result = []
        i = 0
        while i < len(text):
            if text[i] != "%":
                result.append(text[i])
                i+=1
                continue

            j = text.find("%", i+1)
            key = text[i+1:j]
            result.append(resolve(key))
            i = j+1
        
        return "".join(result)

replacements = [
    ["A", "hello"],
    ["B", "%A% world"],
    ["C", "%B%!"]
]

text = "%C%"

s = Solution()
s.applySubstitution(replacements, text)