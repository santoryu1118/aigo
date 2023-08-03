from math import sqrt

# https://velog.io/@cjy0029/41%EB%B2%88-%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84
"""
15 : [(1,15), (3,5), (5,3), (15,1)]
16 : [(1,16), (2,8), (4,4) (8,2), (16,1)]
# 이렇게 가운데 약수까지만 확인을 하면됨. 그래서 sqrt(n) 까지만 확인하면 돼
time complexity of O(sqrt(n))
"""
def is_prime_num(n):
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


"""
Sieve of Eratosthenes (에라토스테네스의 체)
The outer loop runs n times.
The inner loop runs for multiples of each number found to be prime, which would be approximately n/2 
for the first prime (2), n/3 for the next (3), n/5 for the next (5), and so on. 
So, the total amount of work in the inner loop is proportional to n * (1/2 + 1/3 + 1/5 + 1/7 + 1/11 + ... up to 1/p, 
where p is the largest prime <= n).
The sum in parentheses is the sum of the reciprocals of the prime numbers. 
It is a known result in number theory that this sum is approximately log log n.
total time complexity of O(n log log n)
"""
def get_prime_nums(n):
    # list의 index가 숫자를 represent 할 수 있게 : 0,1,2,3....
    is_prime = [False] * 2 + [True] * (n - 1)
    for num in range(2, n + 1):
        if is_prime[num]:
            i = 2
            while num * i <= n:
                is_prime[num * i] = False
                i += 1

    prime_nums = [idx for idx, val in enumerate(is_prime) if val is True]
    print(prime_nums, len(prime_nums))


get_prime_nums(10000)
