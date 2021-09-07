#Outputs anagrams of user specified length into a list
#Thomas Baloyi
#12 May 2019

def program():    
    for c in [1]:
        for K in [1]:
            length = int(input('Enter word length:\n'))
            print('Searching...')
            file = input('Enter file name:\n')
            print("Writing results...")
            file_openned = open("EnglishWords.txt","r")
            line = file_openned.readlines()
            for word in line:
                one_word = word.split()
                for i in range(len(one_word)):
                    sample.append(one_word[i])
                    
            a = sample.index('START')
            sample = sample[a:]
        
            for i in range(len(sample)):
                if len(sample[i]) == length:
                    list1.append(sample[i])
    
            list1 = sorted(list1)
        try:
            limit = [0]
            for i in range(len(list1)):
                setting = []
                for k in range(len(list1)):
                    if sorted(list1[k].lower()) == sorted(list1[i].lower()):
                        setting.append(list1[k])
                if setting != [] and len(setting) > 1:
                    start.append(str(setting))
            file_openned.close()
        except:
            print('Something uncertain.')
            
    start = sorted(start)
    found = []
    for i in range(len(start)):
        if start[i] not in found:
            found.append(start[i])
            found.append('\n')
    if found != []:
        del found[-1]
        file_openned.close()        
        finale = open(file,'w')
        finale.writelines(found)
        finale.close()
    else:
        file_openned.close()        
        finale = open(file,'w')
        finale.close()    

def main():
    print('***** Anagram Set Search  *****')
    list1 = []
    start = []
    sample = []
    program()
    
if __name__ == '__main__':
    main()