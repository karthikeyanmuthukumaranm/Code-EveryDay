def password_check(password):
    if len(password)<3:
        return 'invalid'
    if ' ' in password:
        return 'invalid'
    if not any(i.isupper() for i in password):
        return 'invalid'
    if not any(i.isalpha() for i in password):
        return 'invalid'
    if not any(i.isalnum() for i in password):
        return 'invalid'
    return 'valid'

password='Karthi@2009'
print(password_check(password))
