def program():    
    list1 = []
    for k in [1]:
        for i in range(len(file_data) - (''.join(file_data).count('"""DEBUG"""'))):
            if '"""DEBUG"""' in file_data[i]:
                del file_data[i]
                file.close()
                file = open(filename,"w")
                file.writelines(file_data)
                file.close()
                base.insert(0,False)  
        if base[0] == True:   
            for i in range(len(file_data)):
                if 'def' in file_data[i]:
                    colon = file_data[i].find('(')
                    if file_data[i][colon-1] == ' ':
                        edition = file_data[i][4:colon-1]
                    else:
                        edition = file_data[i][4:colon]
                    appendent = '    """DEBUG""";print(\''+edition+'\')\n'
                    newline.append(file_data[i])
                    newline.append('')
                    newline.append(appendent)
                elif '#' in file_data[i]:
                    list1.insert(0,1)
                    newline.append(file_data[i])
                else:
                    newline.append(file_data[i])
            if list1[0] == 1:
                newline.insert(0,'"""DEBUG"""\n')
            file.close()
            file = open(filename,'w')
            file.writelines(newline)
            file.close()
            print('Inserting...Done')
        else:
            print('Program contains trace statements\nRemoving...Done')


def main():
    filename = input('Enter the name of the program file: ')
    file = open(filename,"r")
    file_data = file.readlines()
    newline = []
    base = [True] #Boolean expression turned into list
    print('***** Program Trace Utility *****')
    program()

if __name__ == '__main__':
    main()