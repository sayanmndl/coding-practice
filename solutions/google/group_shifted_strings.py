from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)

        for s in strings:
            shift = ord(s[0]) - ord('a')

            key = []

            for ch in s:
                normalized = (
                    ord(ch) - ord('a') - shift
                ) % 26

                key.append(chr(normalized + ord('a')))

            groups["".join(key)].append(s)
        
        return list(groups.values())