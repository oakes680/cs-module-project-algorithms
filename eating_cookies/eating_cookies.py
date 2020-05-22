'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     if n == 0 or n ==1:
#         return 1
#     # elif n == 2:
#     #     return 2
#     elif n < 0:
#         return 0
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


# def eating_cookies(n):
#     store = {}
#     def helper(n):
#         if n == 0 or n ==1:
#             return 1
#         elif n == 2:
#             return 2
#         elif n in store:
#             return store[n]
#         else:
#             store[n] = helper(n-1) + helper(n-2) + helper(n-3)
#             return store[n]
#     return helper(n)

def eating_cookies(n, cache=None):
    
    if n == 0:
        return 1   
    elif n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
            #cache = {i: 0 for i in range(n+1)} 
            print(cache)
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
