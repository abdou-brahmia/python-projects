def recherche(liste_temp,element):
    
    liste=sorted(liste_temp)
    print(liste)
    a = 0
    b = len(liste)-1
    state=False
    while (a <= b) and (state==False):
        m = (a+b)//2
        if liste[m] == element:
            state =True
        elif liste[m] > element:
            b = m-1
        elif liste[m] < element:
            a = m+1
    return [state,m]

if __name__ == "__main__":
    
    li = [5, 3, 2, 4, 6]
    a = recherche(li,3)
    print(a)
