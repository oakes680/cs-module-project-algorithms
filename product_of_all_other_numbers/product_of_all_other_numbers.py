'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    #[1,7,3,4]   -->  [7*3*4] = 84,   [1*3*4] = 12,  [1*7*4] = 28,  [1*7*3] = 21  
    ccc =[]
    # for i in range(len(arr)):
    #     product = 1
    #     for j in range(len(arr)):
    #         if i == j:
    #             product = product *1
    #         else:
    #             product = product * arr[j]
                
    #     ccc.append(product)
            
    # return ccc

    prod = 1
    aaa= []
    for i in arr:
        prod *= i
    print(prod)
    for i in arr: 
        aaa.append(prod//i)
    newlst = [prod//i for i in arr]
    return aaa
       
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [2, 7, 3, 4]
    # arr =[7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
