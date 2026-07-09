from sympy import symbols


p = symbols('p')
trace_1 =  1  
trace_cache = {0: 2, 1: trace_1}

def complicated_trace(n):
    def inner(k):
        if k in trace_cache:
            return trace_cache[k]
        val = inner(k - 1) * inner(1) - p * inner(k - 2)
        trace_cache[k] = val
        return val

    t = inner(n)
    return p**n + 1 - t


for i in range(1,8):
    print(complicated_trace(i))
