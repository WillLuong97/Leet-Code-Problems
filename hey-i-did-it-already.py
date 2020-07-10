def solution(n,b):
    k = len(n)
    m = n 
    # a copy version of the id string into the list for easier manipulation
    copied_id = []
    #assigning values of n into the copied id list
    while m not in copied_id:
        copied_id.append(m)
        #sort the list into ascending order
        sorted_list = sorted(m)
        #create ascend and descend version of the original list
        x = ''.join(sorted_list[::-1]) #digits in descending orders
        y = ''.join(sorted_list) #digits in ascending order
        #digits of ID in base 10: 
        if b == 10:
            int_z = int(x) - int(y)
            m = str(int_z)
        else: 
            #convert the digits into base 10
            intoBase10 = int(to_base_10(x,b)) - int((to_base_10(y,b))
            m = to_base_n(str(intoBase10), b)
        
        m = (k - len(m)) * '0' + m
    #final answer:
    return len(copied_id) - copied_id.index(m)
        
# #helper method to convert into base 10
def to_base_10(into_n, n):
    x = list(into_n[::-1])
    y_base_10 = 0 
    for i, a in enumerate(x):
        y_base_10 += int(a) * (n ** i)
    return str(y_base_10)


#helper method to convert the digit into base n
def to_base_n(into_10, n):
    int_form = int(into_10)
    digits_base_n = []
    #when the integer form of the base 10 is not out of range from the base n
    while int_form >= n:
        r = int_form % n 
        digits_base_n.append(str(r))
        int_form = (int_form - r) // n
    #adding the converted into base n digits into the string. 
    digits_base_n.append(str(int_form))
    return ''.join(digits_base_n[::-1])
