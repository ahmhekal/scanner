reserved=['if','then','else','end','repeat','until','read','write']
special_symbols=['+','-','*','/','=','<','>',';',')','(',':']
output=[]

def get_token(L,index): #L is the line, index is the index of the character to process
    temp=''
    if L[index].isalpha()==True:
        temp+=L[index]
        index+=1
        while L[index].isalpha():
            temp+=L[index]
            index+=1
        if temp in reserved:
            output.append(('reserved word',temp))
            return index
        else:
            output.append(('identifier',temp))
            return index

    elif L[index].isdigit()==True:
        temp+=L[index]
        index+=1
        while L[index].isdigit():
            temp+=L[index]
            index+=1
        output.append(('Number', temp))
        return index


    elif L[index] in special_symbols:
        if L[index] == ':': #':' must be follower by '='
            output.append(('special symbol', ':='))
            index+=2
        else:
            output.append(('special symbol', L[index]))
            index+=1
        return index

    elif(L[index]=='{' ): #to handle comments
        while (L[index]!='}'):
            index+=1
        return index+1

    else:
        return index+1
input_name=input("please enter the input file name, or press 'Enter' to write in the console \n")
if len(input_name)>0: #if the users entered a file name
    f=open(input_name)
    s=f.read()
    s+=" "
    index=0

    while(index<len(s)):
        index=( get_token(s,index) )

    handle = open('output.txt', 'w')
    for item in output :
        handle.write(str(item)[1:len(str(item))-1])
        handle.write('\n')
    print('The output has been successfully written in output.txt file !')
        

else:

    print("Start Writing !!, enter 'quit' to exit")
    while(1):
        output=[]
        s=input("")
        s+=" "
        if s == 'quit ' :
            break
        index=0
        while(index<len(s)):
            index=( get_token(s,index) )
        for item in output :
            print(str(item)[1:len(str(item))-1])
