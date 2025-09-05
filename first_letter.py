def first_letter(sentence):
    word=sentence.split()
    result=''
    for i in word:
        result+=i[0]
    return result

sentence='world health organization'
print(first_letter(sentence))