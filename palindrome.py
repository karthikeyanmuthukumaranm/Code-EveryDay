def is_palindrome(string):
    if string==string[::-1]:
        return 'palindrome'
    return 'not palindrome'

string='madam'
result=is_palindrome(string)
print(result)