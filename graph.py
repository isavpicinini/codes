#chose a prime number n
n = 19

#this creates an empty list which will be filled with edge representatives
#for every i, it decides which j is such that R^j is the same edge as R^i
E=[]
for i in range(0,n):
    w=[]
    w.append(i)
    for j in range(0,n):
        if (1+i*j)%n==0:
            w.append(j)
    E.append(w)

#redE is the reduction of E
#if i,j are equivalent then [i,j] and [j,i] show up in E
#the loop tests for each pair in E if there is some other vector with coordinates swapped     
redE=E.copy()
for i in range(0,len(E)):
    for j in range(0,i):
        if len(E[i])==2:
            if E[i][1]==E[j][0]:
                redE.remove(E[i])

#this creates an empty list which will be filled with vertex representatives
#for every i, it decides what other vertices are equivalent to it
#R^0 is always equivalent to R^(n-1) and to S 
#0 and n-1 produce a pair, other integers produce triples          
V=[]
for i in range(0,n):
    w=[]
    w.append(i)
    for j in range(0,n):
        if (1+i+i*j)%n==0:
            w.append(j)
        elif (1+j+i*j)%n==0:
            w.append(j)
    V.append(w)
        
V.remove(V[len(V)-1])

#redV is the reduction of V
redV=V.copy()
for i in range(0,len(V)):
    if len(V[i])==3:
        for j in range(0,i):
            if V[i][1]==V[j][0]:
                redV.remove(V[i])
                break
            if V[i][2]==V[j][0]:
                redV.remove([i])
                break

#each coset representative R^k is an edge from R^k to R^(k-1)
#this runs through the reduced representatives and creates edges [k,k-1]            
edges=[[0,0]]
for i in range(1,len(redE)):
    w=[]
    if redE[i][0]==redE[i][1]:
        w.append(redE[i][0])
        w.append(redE[i][0])
    else:
        w.append(redE[i][0]-1)
        w.append(redE[i][0])
    edges.append(w)

#corE corrects the list of edges by swapping [k,k-1] for [r,s] if k~r and k-1~s in V
corE=edges.copy()
for i in range(1,len(edges)):
    if edges[i][0]!=edges[i][1]:
        for j in range(0,2):
            for k in range(0,len(redV)):
                if edges[i][j]==redV[k][1]:
                    corE[i][j] = redV[k][0]
                elif len(redV[k])==3:
                    if edges[i][j]==redV[k][2]:
                        corE[i][j] = redV[k][0]
                        
print(corE)
                        
                