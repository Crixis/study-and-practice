examenes_medicos = [[32777584,("EM_AUD",15000),("EM_VIS",15000),("EM_FIS",20000), ("EL_PCOVID", 50000), ("EL_GENERAL", 35000)], 
[1048069255,("EM_AUD",15000),("EM_VIS",15000),("EM_FIS",20000),("EL_PCOVID", 50000), ("EL_GENERAL", 35000)], 
[8534598,("EM_AUD",15000),("EM_VIS",15000),("EM_FIS",20000)], 
[32444589,("EM_AUD",15000),("EM_VIS",15000),("EM_FIS",20000),("EL_PCOVID", 50000), ("EL_GENERAL", 35000)]]

def covid(ex):
    totalcovid=0
    for n in range(0, len(ex)):
        for i in range(1, len(ex[n])):
            if "EL_PCOVID" in ex[n][i]:
                totalcovid+=1
    return totalcovid

def informe(examenes_medicos:list)->list: 
    listasalida=[]
    total=[]
    suma=0
    for h in range(0, len(examenes_medicos)):
        listasalida.append([examenes_medicos[h][0],0])

    listasalida.append(covid(examenes_medicos))

    for n in range(0, len(examenes_medicos)):
        for j in range(1, len(examenes_medicos[n])):
            suma+=examenes_medicos[n][j][1]
        total.append(suma)
        suma=0
    
    for h in range(0, len(listasalida)-1):
        listasalida[h][1]=total[h]

    return listasalida
    
print(informe(examenes_medicos))