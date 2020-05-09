AA_WMap= {
'G': 57,
'A': 71,
'S': 87,
'P': 97,
'V': 99,
'T': 101,
'C': 103,
'I': 113,
'L': 113,
'N': 114,
'D': 115,
'K': 128,
'Q': 128,
'E': 129,
'M': 131,
'H': 137,
'F': 147,
'R': 156,
'Y': 163,
'W': 186, }



def spectrum(seq):
    
    ls=[]
    ls.append(0)
    s=list(seq)


    #second...
    num=1
    for z in range(0,len(seq)-1):
        
        for i in range(0,len(seq)):
            total=0
            counter=0
            no_oftimes=0
            for j in range(i,i+num):
                if(counter==len(seq)):break
                if(j==len(seq) or j> len(seq)):j=j-len(seq)
                total+=AA_WMap[s[j]]
                no_oftimes=no_oftimes+1
                if(no_oftimes==num):
                    counter+=1
                    ls.append(total)
                    no_oftimes=0
        num+=1

    n=0
    #last one..
    for i in range(1,len(seq)+1):
       n+=ls[i] 
    ls.append(n)
    for i in range(0, len(ls)):
        print(ls[i])
    






seq=input("Enter the sequence : ")
spectrum(seq)



