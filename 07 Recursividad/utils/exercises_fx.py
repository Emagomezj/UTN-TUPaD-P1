def fact(num):
    if num == 1 or num ==0:
        return 1
    else:
        return num * fact(num-1)
def fib(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fib(pos-1) + fib(pos-2)

def pot(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/(base * pot(base,abs(exp)-1))
    else:
        return base * pot(base, exp -1)

def dec_bin(num):
    if num == 0:
        return ''
    return dec_bin(num//2) + str(num%2)

def pal(string):
    string = string.replace(' ', '')
    if len(string) == 1:
        return True
    elif len(string) == 2:
        if string[0] == string[1]:
            return True
        else:
            return False
    else:
        if string[0] == string[-1]:
            return pal(string[1:-1])
        else:
            return False

def sum_dig(num):
    if num//10 == 0:
        return num
    else:
        return sum_dig(num//10) + num%10

def sm_bl(n):
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sm_bl(n-1)

def sum_val(n, v):
    if n == 0:
        return 1 if v == 0 else 0
    elif n // 10 == 0:
        return 1 if n == v else 0
    else:
        cont = 1 if n%10 == v else 0
        return cont + sum_val(n//10, v)
