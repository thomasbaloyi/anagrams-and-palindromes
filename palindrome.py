#Calculates whether a sequence of symbols is a palindrome or not
#Thomas Baloyi
#19 April 2019

def palindrome_reverse(variable):
    if variable == '':
        return variable
    else:
        return palindrome_reverse(variable[1:]) + variable[0]


seq = input('Enter a string:\n')
original_seq = seq
if palindrome_reverse(seq) == original_seq:
    print('Palindrome!')
else:
    print('Not a palindrome!')