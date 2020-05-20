import random

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
  i = 0
  arr.sort()
  while i <= len(arr) - 1:
 
    if arr[i] == arr[len(arr) - 1]:
   
        return arr[i]

    elif arr[i] == arr[i + 1]:
        i += 2
   
    else:

        return arr[i]




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5,  5, 9, 3, 3, 0, 0]
    arr = [1, 1, 0, 4, 4, 5,  5, 9, 3, 3, 0]

    print(f"The odd-number-out is {single_number(arr)}")