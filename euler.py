import time

euler_time = 0

max_prime_limit = 10
private_primes = []

def primes2(n: int) -> [int]:
    global max_prime_limit, private_primes
    if n > max_prime_limit:
        max_prime_limit = n
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    private_primes = [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
    return private_primes

def primes_between(low: int,high: int) -> [int]:
    """ Input high>low, Returns a list of primes within the range """
    ps = primes2(high)

def binary_search_low(items: list,point: int, ordered = True):
    if not ordered: items = sorted(items)
    if point < items[0] or point > items[-1]: return -1
    low  = 0
    high = len(items)
    while high-low > 1:
        mid = (high+low)//2
        if point < items[mid]:
            high = mid
        elif point > items[mid]:
            low = mid
        else:
            return mid
    return (high+low)//2

def __isPrime(n: int) -> bool:
    """ Input n >= 2, Returns True if prime else False """
    if n == 2: return True
    for f in range(2,int(n**0.5)+1):
        if n%f == 0: return False   
    return True

def isPrime(n: int) -> bool:
    if n > 229358218:
        return __isPrime(n)
    global private_primes
    if n > max_prime_limit: primes2(2*n)
    i1 = binary_search_low(private_primes,n)
    return private_primes[i1] == n


def concatenate(a:int,b:int) -> int:
    """ Input integers a and b, Returns the concatenation of a with
    b added to the right side """
    m = len(str(b))
    return a*(10**m) + b

def digits(n:int) -> [int]:
    digs = []
    while n > 0:
        digs.append(n-(n//10)*10)
        n = n//10
    return digs[::-1]

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)


def start_timer():
    global euler_time
    euler_time = time.time()

def end_timer():
    global euler_time
    return time.time() - euler_time