'''

76543210
67 45 23 01
45 67 01 23
01 23 45 67

'''


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
            templen=len(temp)
            temp2len=len(temp2)
            i=0
            j=0
            buffer=""
            print("data", temp,temp2)
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
        data=[]
        for x in array:
            data.append(x)
        for x in data:
            del array[x]
        array=array2.copy()
        data=[]
        for x in array2:
            data.append(x)
        for x in data:
            del array2[x]
        if len(array)==1:
            exittheloop=True
    print(array)

data="9876543210986754"
sort(data)
