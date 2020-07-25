# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word. 

#Function to create a text format with each line length to be equal to the max width
def textJustification(word, maxWidth):
    #key variables:  
    i = 0 
    n = len(word)
    result = []
    while(i < n):
        j = i + 1
        #would count the total words that will be present in each lines
        linelength = len(word[i])
        spaceBetweenWords = j - i - 1
        #loop if the word being pointed by j is still in the word array and after adding it into the linelength, linelength is still lesser than max width
        while(j < n and (linelength + len(word[j]) + spaceBetweenWords) < maxWidth):
            linelength += len(word[j])
            j += 1
        spacesNeeded = maxWidth - linelength    
        numOfCharacter = j - i
        

        #Determine whether a line needs left justify or middle justify
        if(numOfCharacter == 1 or j >= maxWidth):
            result.append(leftJustify(word, i, j, spacesNeeded))
        
        else:
            result.append(middleJustify(word, i, j, spacesNeeded))

        i = j

    return result


#Helper method 1: Allocate right number of spaces for left justify
def leftJustify(word, i, j, spacesNeeded):
    spacesOnTheRight = spacesNeeded - (j - i - 1)
    resultString = ""
    for k in range(i + 1, len(word)):
        resultString += "" + word[k]
    return resultString
    

#Helper method 2: Allocate the right number of spaces between characters for middle justify
def middleJustify(word, i, j, spacesNeeded):
    section_of_white_space = spacesNeeded // (j - i -1)
    extra_white_space = spacesNeeded % (j - i - 1)
    #final string that contains the element
    resultString = ""

    for k in range(i+1, j):
        if extra_white_space > 0:
            spaceToApply = section_of_white_space + 1
        else:
            spaceToApply = section_of_white_space + 0
        extra_white_space -= 1
        resultString += " " * spaceToApply + word[k]
    
    return resultString



#main function to excute the program
def main():
    word = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(textJustification(word, maxWidth))
    
main()
