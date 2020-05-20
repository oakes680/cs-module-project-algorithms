'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # newArr= []
    # for i in range(len(arr) -1, -1, -1):
    #     if arr[i] == 0:
    #         newArr.append(arr[i])
    #     else:
    #         newArr.insert(0, arr[i])
    # return newArr

    ########################################################################################


    for i in range(0, len(arr)):
        j=i+1
        if arr[i] == 0:
            while  j < len(arr):
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
                else:
                    j = j + 1
    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    # arr =[1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")