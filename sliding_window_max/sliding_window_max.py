'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    #k=5
    r = k
    b = 0
    newArr = []
    for i in range(len(nums) ):
        max = float("-inf")
        for j in range(b, r):
            if len(nums) < r:
                return newArr
            if nums[j] > max:
                max = nums[j]
        newArr.append(max)
        b += 1
        r += 1
    return newArr



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
