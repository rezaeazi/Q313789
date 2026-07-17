import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MOD = 998244353
    
    max_n = 200005
    fact = [1] * max_n
    inv_fact = [1] * max_n
    
    for i in range(1, max_n):
        fact[i] = (fact[i-1] * i) % MOD
        
    inv_fact[max_n-1] = pow(fact[max_n-1], MOD - 2, MOD)
    for i in range(max_n-2, -1, -1):
        inv_fact[i] = (inv_fact[i+1] * (i + 1)) % MOD

    T = int(input_data[0])
    pointer = 1
    
    output = []
    for _ in range(T):
        n = int(input_data[pointer])

        a = [int(x) for x in input_data[pointer+1 : pointer+1+n]]
        b = [int(x) for x in input_data[pointer+1+n : pointer+1+2*n]]
        pointer += 1 + 2*n
        
        k = 0
        for val in a:
            if val == 0:
                k += 1
                
        if n >= k:
            ans = (fact[n] * inv_fact[n - k]) % MOD
        else:
            ans = 0
            
        output.append(str(ans))
        
    print('\n'.join(output))

if __name__ == '__main__':
    solve()