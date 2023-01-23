def sort(data):

    array={}
    array2={}
    counter=0
    for x in data:
        array[counter]=x
        counter+=1

    exittheloop=False
    while exittheloop==False:
        counter=0
        for x in range(0,len(array),2):
            temp=array.get(x)
            temp2=array.get(x+1)
            if not temp2==None:
                templen=len(temp)
                temp2len=len(temp2)
            i=0
            j=0
            buffer=""
            exittheloop2=False
            while exittheloop2==False and not temp2==None:
                if i>=templen and j>=temp2len:
                    exittheloop2=True
                elif i>=templen:
                    buffer=buffer+temp2[j]
                    j+=1
                elif j>=temp2len:
                    buffer=buffer+temp[i]
                    i+=1
                elif temp[i]<temp2[j]:
                    buffer=buffer+temp[i]
                    i+=1
                else:
                    buffer=buffer+temp2[j]
                    j+=1
            array2[counter]=buffer
            counter+=1
        del array
        array=array2.copy()
        del array2
        array2={}
        if len(array)==1:
            exittheloop=True
    return array[0]

data="9876543210abccowabunga98675444444444444444444444444444444444444444444444444444444444444444444444334142314321234321342321484848"
print(sort(data))
