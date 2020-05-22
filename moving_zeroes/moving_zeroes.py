'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = arr.count(0)
    zeros_list = [0 for i in range(count)]
    print(zeros_list)
    #iterate through array
    x = [i for i in arr if i != 0]
    print(x)
    arr= x + zeros_list
    return arr

      
        
             


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")