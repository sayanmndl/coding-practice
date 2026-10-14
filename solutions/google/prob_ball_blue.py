from functools import lru_cache

def probability_last_blue():
    @lru_cache(None)
    def dp(red, blue, prev_blue):
        if blue == 0: return 0.0
        if red == 0: return 1.0
        total = red+blue
        p_red = red/total
        p_blue = blue/total

        # if drae red
        result = p_red * dp(red-1, blue, False)
        if prev_blue:
            # second consecutive blye
            result += p_blue * dp(red, blue - 1, True)
        else:
            result += p_blue * dp(red, blue, True)
        return result
    
    return dp(2,2,False)

    