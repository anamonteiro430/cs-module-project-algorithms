'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    mult = [1] * len(arr)
    print(mult)
    prod=1
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j:
                prod *= arr[j]
                print(arr[j], prod)
        mult[i] = prod
        prod = 1


        
    return mult
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9]
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
