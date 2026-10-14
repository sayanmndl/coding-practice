def letter_combination(digits):
    if not digits: return []

    phone_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    result = []
    current = []

    def backtrack(idx):
        if idx == len(digits):
            result.append(''.join(current))
            return

        letters = phone_map[digits[idx]]

        for letter in letters:
            current.append(letter)
            backtrack(idx+1)
            current.pop()
        
    backtrack(0)
    return result