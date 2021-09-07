#Looks for anagrams in a file
#Thomas Baloyi
#01 May 2019

def anagram(word1,word2):
    """Checks if words are anagrams of each other"""
    word1_letters = []
    word2_letters = []
    for i in word1:
        word1_letters.append(i)
    for i in word2:
        word2_letters.append(i)
    word1_letters.sort()
    word2_letters.sort()
    if len(word1_letters) == len(word2_letters):
        if word1_letters == word2_letters:
            return word2
        else:
            return False
    else:
        return False
            
def main():
    print('***** Anagram Finder *****')
    word = input('Enter a word: ')
    word1 = word.lower()
    word1 = word1 + '\n'
    try:
        word_dict = open('EnglishWords.txt', 'r')
    except IOError as errno:
        print("Sorry, could not find file 'EnglishWords.txt'.")
    
    all_of_file = word_dict.readlines()
    
    #adds all the relevant lines of the file to a list
    list_of_words = []
    for i in range(59,len(all_of_file)): 
        p = all_of_file[i]
        list_of_words.append(p)
    
    #adds all anagrams to a list 
    anagrams_list = []
    for i in range(len(list_of_words)-1):        
        ana = anagram(word1, str(list_of_words[i]))
        if ana != False:
            ana = ana[:len(word):]
            if ana != word:
                anagrams_list.append(ana)
                anagrams_list.sort()
                
    if anagrams_list == []:
        word = "'"+ word + "'"
        print("Sorry, anagrams of", word, "could not be found.")
    else:
        print()
        print(anagrams_list)
    word_dict.close()
    
if __name__ == '__main__':
    main()