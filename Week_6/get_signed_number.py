def get_signed_number(string):
    n = " "
    digit = False
    dot = False
    
   
    for i, ch in enumerate(string):
        if ch.isdigit():
            n += ch
            digit = True
        elif ch in '+-' and not digit:
            if i +1 < len(string) and string[i+1].isdigit():
                n += ch
        elif ch == '.' and digit and not dot:
            n += ch
            dot = True
    return n 

print(get_signed_number('abc-2lj42k-6.ajjlsf23jh'))
print(get_signed_number('abc-a2lj42k-6b.ajjlsf23jh')) 
