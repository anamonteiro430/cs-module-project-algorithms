'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #iterate through array
    for i in range(0, len(arr)):
        #if the number is zero
        if arr[i] == 0:
            #store the popped value 
            removed = arr.pop(i)
            #append the zeros to the end of array
            arr.append(removed) 
            #decrement i to go through all the indexes
            i -= 1
             
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")