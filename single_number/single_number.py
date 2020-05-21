'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr): #[1, 1, 2, 3, 3]
    #Create empty arr
    empty_arr = []

    for elem in arr:
        #append everything to the arr
        #unless it's already there
        if elem in empty_arr:
            empty_arr.remove(elem)
        else:
            empty_arr.append(elem)
    #return the only elem on the arr
    return empty_arr.pop()

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")