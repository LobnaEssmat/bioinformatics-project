import sys
from operator import eq
import itertools as it

mass=[57, 71, 87, 97, 99, 101, 103, 113, 114,115, 128, 129, 131, 137, 147, 156, 163, 186]
def cut_peptide(peptide):
    result=[] #create initial list
    for cut in range(1,len(peptide)):
        for i in range (len(peptide)-cut):
            result.append(peptide[i:i+cut])
            result.append(peptide[i+cut:]+peptide[:i]) #cyclic peptide
            result.append(peptide)
            return result
        
def expand(l):
     lc=l[:] #list for copy
     for i in lc:
         l.remove(i)
         for m in mass:
             temp=i[:] #copy list in temp list
             temp.append(m)
             l.append(temp)
                    
def isconsistent(peptide,specturm):
     sc=specturm[:] #copy specturm
     for sp in peptide:
         if sp not in sc:
             return false
         else:
            sc.remove(sp)
            return true

def comparelist(x,y):
    if len(x)==len(y):
        for i in range(len(x)):
            if x[i]==y[i]:
                count
            else:
               return false
               return true
        else:
           return false

def cyclopeptidesequencing(specturm):
    l=[[]]
    while len(1)!=0:
        expand(l)
        for peptide in l:
            ps=[0]+[sum(s) for s in cut(peptide)] #print peptide
            if sorted(ps)==specturm:
                print([str(z) for z in peptide])
                l.remove(peptide)
            else:
                if not isconsistent(peptide,spectrurm):
                    l.remove(peptide)
                        
           
