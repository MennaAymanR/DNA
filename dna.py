dna=input("Enter Your DNA")
if dna.count("A")+dna.count("T")+dna.count("C")+dna.count("G")==len(dna):
    print("Valid Sequence")
    dna.upper()
    print(dna,end=" ")
    
else:
    print("invalid sequence")
def gene_(dna):
    if dna[0:3] != "ATG":
        print("invalid sequence")
    if len(dna) % 3 != 0:
        print("invalid length")
    if dna[-3::] not in ["TAG","ATT","TGA" ] :
        print("invalid end")
def ComplementSeq(dna):
    for i in dna:
        
        if i== "A":
            print("T")
        if i =="T" :
            print("A")
        if i =="C":
            print("G")
        if i=="G":
            print("C") 
        print(i,end=" ")    
               
ComplementSeq(dna)
gene_(dna)


