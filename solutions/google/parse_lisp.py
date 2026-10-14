class Solution:
    def evaluate(self, expression):

        def eval_expr(expr: str, env: dict):
            if expr[0] != '(':
                if expr[0] == '-' or expr[0].isdigit():
                    return int(expr)
                
                return env[expr]
            
            inner = expr[1:-1] # remove parenthesis

            # split only at spaces at depth 0
            tokens = []
            start = 0
            depth = 0

            for i, char in enumerate(inner):
                if char == '(':
                    depth += 1
                elif char == ")":
                    depth -= 1
                elif char == " " and depth == 0:
                    tokens.append(inner[start:i])
                    start = i+1
            tokens.append(inner[start:])
            operator = tokens[0]

            # add
            if operator == "add":
                return (
                    eval_expr(tokens[1], env) + eval_expr(tokens[2], env)
                    )
            
            # mult
            if operator == "mult":
                return (
                    eval_expr(tokens[1], env) * eval_expr(tokens[2], env)
                    )
            
            # let
            local_env = env.copy()
            # tokens:
            # ["let", v1, e1, v2, e2, ..., final_expr]

            i = 1

            while i < len(tokens) - 1:
                variable = tokens[i]
                value_expr = tokens[i+1]
                value = eval_expr(value_expr, local_env)

                local_env[variable] = value
                i+=2

            return eval_expr(tokens[-1], local_env)
        return eval_expr(expression, {})