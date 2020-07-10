def solution(x):
    # Your code here
    # only lower case character are being formed
    # punctuation is still the same and uppercase letter
    
    #string of all forward lowercase letter:
    forward_string = "abcdefghijklmnopqrstuvwxyz"

    #list of all backward element:
    backward_list = []
    #adding the string chacrater into a list
    for charc in range(0, len(forward_string)):
        backward_list.append(forward_string[charc])
    forward_list = backward_list.copy()

    backward_list.reverse()    
    #final decrypted message
    decrypted_list = []
    
    #loop through original the message
    for i in x:
        #if the character in the list is a lowercase
        #based on the ascii representation
        if (ord(i) >= 97 and ord(i) <=122):
            #convert the charc in the message with the backward element in the backward list
            element = backward_list.index(i)
            current_charc = forward_list[element]
            decrypted_list.append(current_charc)
        #if not, just add the current char into the new list because it should be left untouched
        else:
            decrypted_list.append(i)
    decrypted_message = "".join(decrypted_list)
    return decrypted_message
