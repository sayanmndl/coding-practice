class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        n = len(words)
        i = 0

        while i < n:
            j = i
            total_chars = 0

            while j < n and total_chars + len(words[j]) + (j-i) <= maxWidth:
                total_chars+= len(words[j])
                j+=1

            line_words = words[i:j]
            gaps = j-i-1

            if j == n or gaps == 0:
                line = " ".join(line_words)
                line = line.ljust(maxWidth)

            else:
                total_spaces = maxWidth - total_chars
                spaces_per_gap = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " + (spaces_per_gap + (1 if k < extra else 0))
                line += line_words[-1]

            res.append(line)
            i=j
        return res