lista1=[{'año': 2002, 'm2': 100, 'asc': True, 'gar': True, 'hab': 3, 'zona': 3},
        {'año': 1985, 'm2': 80, 'asc': True, 'gar': True, 'hab': 3, 'zona': 4},
        {'año': 2006, 'm2': 90, 'asc': False, 'gar': True, 'hab': 3, 'zona': 5},
        {'año': 2012, 'm2': 180, 'asc': True, 'gar': True, 'hab': 4, 'zona': 2},
        {'año': 1999, 'm2': 70, 'asc': False, 'gar': True, 'hab': 3, 'zona': 1},
        {'año': 2003, 'm2': 220, 'asc': True, 'gar': True, 'hab': 5, 'zona': 6}]

"""list2=[]
list2.append(lista1[0])
list2.append(lista1[1])
list2[0]['pre']=500
list2[1]['pre']=2800
print(list2)"""
"""list2= lista1[:]
print(list2)
"""
def zona(m2:int, zona:int):
        if zona==1:
                preM2=m2*800000
        elif zona==2:
                preM2=m2*1200000
        elif zona==3:
                preM2=m2*2200000
        elif zona==4:
                preM2=m2*3400000
        elif zona==5:
                preM2=m2*5200000
        elif zona==6:
                preM2=m2*6400000

        return preM2
def garage(garage:bool):
        if garage:
                pre=5000000
        else:
                pre=0
        return pre
def habitacion(habi:int):
        pre=habi*1000000
        return pre
def ascensor(asc:bool):
        if asc:
                pre=1500000
        else:
                pre=0
        return pre
def antiguedad(año:int, precio:int):
        pre=int(precio-(precio*(2021-año)/100))
        return pre


def buscar(inmu:list, presupuesto:int)->list:
        precios=[]
        preciototal=[]
        listaSalida=[]

        for n in range(0,len(inmu)):
                precios.append(zona(inmu[n]['m2'], inmu[n]['zona']))
                precios[n]+=(garage(inmu[n]['gar']))
                precios[n]+=(habitacion(inmu[n]['hab']))
                precios[n]+=(ascensor(inmu[n]['asc']))
        for i in range(0,len(precios)):
                precios[i]=antiguedad(inmu[i]['año'],precios[i])
                if precios[i]<=presupuesto:
                        listaSalida.append(inmu[i])
                        preciototal.append(precios[i])
        for h in range(0,len(preciototal)):
                listaSalida[h]['pre']=preciototal[h]
        return listaSalida
                
        
        


buscar(lista1,350000000)