from math import*
from colorama import Back,Fore,Style,deinit,init


carte=[]
carte = input("Entrez Le numéro de votre carte : ")

if len(carte)==16 :
    print(Fore.GREEN+Style.NORMAL + "Vous avez entrez le bon nombre de chiffre pour votre carte !")
    
    E00=[]
    E01=[]
    E02=[]
    E03=[]
    E04=[]
    E05=[]
    E06=[]
    E07=[]

    E00=int(carte[14])*2
    E01=int(carte[12])*2
    E02=int(carte[10])*2
    E03=int(carte[8])*2
    E04=int(carte[6])*2
    E05=int(carte[4])*2
    E06=int(carte[2])*2
    E07=int(carte[0])*2

    if (len(str(E00)))==2:
        result_E00=str(E00)
        result1_E00=int(result_E00[1])+int(result_E00[0])  
    else : 
        result1_E00=int(E00)
    
    if (len(str(E01)))==2:
        result_E01=str(E01)
        result1_E01=int(result_E01[1])+int(result_E01[0])  
    else : 
        result1_E01=int(E01)
    
    if (len(str(E02)))==2:
        result_E02=str(E02)
        result1_E02=int(result_E02[1])+int(result_E02[0])  
    else : 
        result1_E02=int(E02)
    
    if (len(str(E03)))==2:
        result_E03=str(E03)
        result1_E03=int(result_E03[1])+int(result_E03[0])  
    else : 
        result1_E03=int(E03)

    if (len(str(E04)))==2:
        result_E04=str(E04)
        result1_E04=int(result_E04[1])+int(result_E04[0])  
    else : 
        result1_E04=int(E04)

    if (len(str(E05)))==2:
        result_E05=str(E05)
        result1_E05=int(result_E05[1])+int(result_E05[0])  
    else : 
        result1_E05=int(E05)

    if (len(str(E06)))==2:
        result_E06=str(E06)
        result1_E06=int(result_E06[1])+int(result_E06[0])  
    else : 
        result1_E06=int(E06)

    if (len(str(E07)))==2:
        result_E07=str(E07)
        result1_E07=int(result_E07[1])+int(result_E07[0])  
    else : 
        result1_E07=int(E07) 

    result1_final=int(result1_E07+result1_E06+result1_E05+result1_E04+result1_E03+result1_E02+result1_E01+result1_E00)

    result2_final=int(carte[1])+int(carte[3])+int(carte[5])+int(carte[7])+int(carte[9])+int(carte[11])+int(carte[13])+int(carte[15])
    
    FIN=result1_final+result2_final

    if FIN%10==0 :

        print(Fore.GREEN+Style.NORMAL + "Votre carte est bel et bien valide ")
    else :
        print(Fore.RED+Style.NORMAL + "Votre carte n'est pas valide")

if len(carte)<16:
    print(Fore.RED+Style.NORMAL + "Veuillez entrez une carte avec au moins 16 chiffres !")
if len(carte)>16:
    print(Fore.RED+Style.NORMAL +"Veuillez entrer une carte avec au plus 16 chiffres !" )