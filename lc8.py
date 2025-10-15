def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0 
    sign = 1
    i = 0 
    if s[0] in ["-", "+"]:
        if s[0] == "-":
            sign = -1
        i +=1
    
    num = 0
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        num = num * 10 + digit
        i += 1
    
    num*= sign

    INT_MAX = 2**31 -1
    INT_MIN = -2**3`
    if num< INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
        
        
    return num