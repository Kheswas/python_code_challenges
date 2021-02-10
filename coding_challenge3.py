isPalindrome = int(input("Please Enter a number:  "))
temp = isPalindrome
reverse_number = 0
while isPalindrome > 0:
    digit = isPalindrome % 10
    reverse_number = reverse_number * 10 + digit
    isPalindrome = isPalindrome // 10

if temp == reverse_number:
    print(True)
else:
    print(False)


is_palindrome_string = str(input("Please enter a String:  "))
if is_palindrome_string == is_palindrome_string[:: -1]:
    print(True)
else:
    print(False)




