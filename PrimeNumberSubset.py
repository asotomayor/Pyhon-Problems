# Given k numbers which are less than n, return the set of prime numbers among them.

def primenumbersubset(k, n):
    prime_set = []
    if k < n:
        for n in range(k, n):
            if n % 2 != 0:
                prime_set.append(n)
        return prime_set
    else:
        print("n value must be greater than k value")


# test
k = 1
n = 10
print(primenumbersubset(k, n))





