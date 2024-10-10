def main():
    user_input = []     #User input list
    i = 0

    #Get user input
    while i < 3:
        display_text = 'Enter string #' + str(i + 1) + ':'  #Display text
        user_input.append(input(display_text))              #Add user input to list
        i += 1

    new_string = reverse_string(user_input[0], user_input[1], user_input[2])    #Concatenated & reverses string

    print(new_string)

#Concatenate & Reverse string function
def reverse_string(s1, s2, s3):
    concat_strings = s1 + s2 + s3   #Concatenate string
    return concat_strings[::-1]     #Return reversed string

if __name__ == '__main__':
    main()