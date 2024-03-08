# Name: Feyza Atabey
# Lab 4 - a function that checks if a string is a palindrome, 
#rotating a list by one position to the right.


#Part 1 

def is_palindrome(s):
    filtered_s="".join(char.lower() for char in s if char.isalnum())

    left_index= 0
    right_index = len(filtered_s) - 1

    while left_index < right_index :
        if filtered_s[left_index] != filtered_s[right_index]:
            return False
        left_index += 1 
        right_index -= 1
    return True

#Part 2

def rotate_list_right(lst):
    if not lst:
        return[]
    last_element = lst[-1]
    for i in range(len(lst) - 1, 0, -1 ):
        lst[i] = lst[i-1]
        lst[0] = last_element
        return lst

def main():
    # Examples for is_palindrome
    print("Palindrome check results:")
    print(is_palindrome("Race! car"))  # True
    print(is_palindrome("Hello, world!"))  #False

    # Examples for rotate_list_right
    print("\nList rotation results:")
    print(rotate_list_right([1, 2, 3, 4, 5]))  
    print(rotate_list_right(['a', 'b', 'c', 'd']))

if __name__ == "__main__":
    main()
