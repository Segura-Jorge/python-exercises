def is_two(n):
    if n in (2, '2', 2.0):
        return True
    else:
        return False
    
def is_vowel(somestring):
    #check that the arg is a str
    if type(somestring) == str:
        
        # if the str is 1 char and a letter
        if len(somestring) == 1 and somestring.isalpha():
            
            #return bool ans to: lower-letter in vowel list?
            return somestring.lower() in list('aeiou')
        
        #return false if string fails 1 alpha-char length
        else:
            return False
        
    # returns false if input is not a str    
    else:
        return False
    
def is_consonant(somestring):
    """
    This function will:
    - intially check the input is a string
        - and 1 char long
        - and a letter
            -if true, returns the opposite return of is_vowel, using the NOT operator
            - False otherwise
    -returns False if not a string
    """
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return (not is_vowel(somestring))
        else:
            return False
    else: 
        return False
    
def capitalize_starting_consonant(word):
    """
    This function will initially check if:
    - input is a str
        - checks if 1st char of the input is a consonant
            - if True, returns the inputted string w/1st char Capitalized
            - False otherwise
        - returns False if not a string
    """
    if type(word) == str:
        if is_consonant(word[0]):
            return word.capitalize()
        else:
            return f"{word} doesn't start with a consonant."
    else:
        return f"{word} isn't a string."
    
def calculate_tip(bill, tip_percent=.2):
    """
    tip_percent is a float number between 0-1
    """
    return f"{tip_percent*100}% tip is: $ {round(bill * tip_percent,2)}"

def apply_discount(orig_price, discount_pct):
    return (1 - discount_pct)* orig_price

def handle_commas(fakenum):
    """
    This function will:
    - check if input is a string
        -removes any commas
        -check if the stripped input is a digit
            - if True, returns input as an integer
            -False otherwise
    - if not a string, returns false stmt
    """
    if type(fakenum) == str:
        stripfakenum = fakenum.replace(",", "")
        if stripfakenum.isdigit():
            return int(stripfakenum)
        else:
            return False
    else:
        False

def get_letter_grade(somegrade):
    if type(somegrade) == int:
        if somegrade >= 90:
            return 'A'
        elif somegrade >= 80:
            return 'B'
        elif somegrade >= 70:
            return 'C'
        elif somegrade >= 60:
            return 'D'
        else: return 'F'
    else:
        return f"{somegrade} is not a digit."
    
def remove_vowels(word):
    new_word = ""
    for letter in word:
        if not is_vowel(letter):
            new_word += letter
    return new_word

def normalize_name(somestring):
    # intialize an empty string called newstring
    newstring = ""
    
    # Iterate over each char in somestring after removing leading & trailing whitespace
    for letter in somestring.strip():
        
        # check if the char is alphanum or a space
        if letter.isalnum() or letter == " ":
            
            #if it is, append ch to the newstring
            newstring += letter
    # iterate over ea char in the newstring
    for letter in newstring:
        #check if the char is alphabetic
        if letter.isalpha():
            #if alpha char is found, exit the loop
            break
        else:
            #if the char is not alphanum, remove it from the beginning of the newstring
            newstring = newstring[1:]
            
    #convert the newstring to lowercase & replace any spaces with underscores
    #then return the mod newstring as the result
    return newstring.lower().replace(" ", "_")

def cumulative_sum(oldlist):
    
    newlist=[]
    
    #intialize a variable to store the cumulative sum
    c_sum = 0
    
    for num in oldlist:
        #add the current number to the cumulative sum
        c_sum += num
        print(f"cumulative: {c_sum}")
        #append the cumulative sum to the newlist
        newlist.append(c_sum)
        print(f"newlist: {newlist}")