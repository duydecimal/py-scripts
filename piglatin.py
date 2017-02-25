pig = 'ay' 
original = raw_input('Enter a word:') #store input into variable “original”
word = original.lower() #converts all input to lower case and stores in “word”
first = word[0] #stores first index of word into variable “first”
new_word = new_word[1:len(new_word)] #looks for indexes between 1 and last index of the word
new_word = word + first + pig #concatenation for new word
if len(original) > 0 and original.isalpha(): #validation 
    print new_word[1:len(new_word)] #prints pig latin conversion of word
else:
    print 'empty'
