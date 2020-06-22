#Python program Validate if a given string can be interpreted as a decimal number
#Valid input: 
#  Numbers: 0-9; Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
#Example: 0 - True, aabc -> false, 0.1 -> true

class Solution: 
    def isNumber(self, s: str) -> bool:
        #trim any whitespaces from the string: 
        s = s.strip()
        #different boolean variable to check for the valid entries
        eSeen = False
        dotSeen = False
        numSeen = False

        #loop through the string to check for valid entries
        for i in range(len(s)):
            #check if the string contains mostly digits:
            if(s[i].isdigit()):
                numSeen = True
            elif(s[i] == '.'):
                #the dot has to be seen before the e
                if(dotSeen or eSeen):
                    return False
                dotSeen = True
            elif(s[i] == 'e'):
                #if "e" is found and but no number has been found, and another e has been found before
                #this should be a false
                if (eSeen or not numSeen):
                    return False
                eSeen = True
                numSeen = False
            elif(s[i] == '-' or s[i] == '+'):
                if((i > 0) and (s[i-1] != 'e')):
                    return False
            else:
                return False

        return numSeen


#driver code: 

string = "0.1e2"
answer = Solution()


print(answer.isNumber(string))                
             

