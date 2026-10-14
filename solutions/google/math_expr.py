class Solution:
    def evaluare(self, expression):
        i = 0

        def parse():
            nonlocal i

            # int
            if expression[i] == '-' or expression[i].isdigit():
                sign = 1

                if expression[i] == '-':
                    sigh = -1
                    i+=1

                num = 0

                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i+=1
                
                return sign * num

            # func name
            start = i

            while expression[i].isalpha():
                i+=1
            
            operation = expression[start:i]

            # skip '('
            i+=1

            left = parse()

            # skip ','
            i+=1

            right = parse()

            # skip ')'
            i+=1

            if operation == 'add':
                return left + right
            if operation == 'sub':
                return left - right
            if operation == 'mul':
                return left * right
            if operation == 'div':
                return int(left/right)

        return parse()