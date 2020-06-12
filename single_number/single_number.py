'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # choose a method if iterating through the array
    # rule out numbers that have duplicates
    numbers_murder = {}
    i = 0
    
    for num in arr:
        if num in numbers_murder:
            numbers_murder[num] += 1
        else:
            numbers_murder[num] = 1
            
    for k, v in numbers_murder.items():
        if v == 1:
            return k
 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
