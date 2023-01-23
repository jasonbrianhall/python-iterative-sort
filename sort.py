'''

76543210
67 45 23 01
45 67 01 23
01 23 45 67

'''


def sort(data):

    array={}
    counter=0
    for x in data:
        array[counter]=x
        counter+=1

    for x in range(0,len(array),2):
        temp=array[x]
        temp2=array[x+1]
        templen=len(temp)
        temp2len=len(temp2)
        i=0
        j=0
        buffer=""
        print("data", temp,temp2)
        exittheloop=False
        while exittheloop==False:
            print(i,j)
            if i>=templen and j>=temp2len:
                exittheloop=True
                print("going 1: ", buffer)
            elif i>=templen:
                buffer=buffer+temp2[j]
                print("Going 2: ", buffer)
                j+=1
            elif j>=temp2len:
                buffer=buffer+temp[i]
                print("going 3: ", buffer)
                i+=1
            elif temp[i]<temp2[j]:
                buffer=buffer+temp[i]
                print("going 4:", buffer)
                i+=1
            else:
                buffer=buffer+temp2[j]
                print("going 5: ", buffer)
                j+=1


data="9876543210986754"
sort(data)
