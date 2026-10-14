def format_number(s, x):
    integer, dot, fraction = s.partition('.')

    if x <= len(integer):
        integer = integer[:x] +'0'*(len(integer)-x)
        fraction = ""

    else:
        remaining = x - len(integer)
        fraction = fraction[:remaining]

    integer = f"{int(integer):,}"
    if fraction:
        return integer + '.' + fraction
    
    return integer