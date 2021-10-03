"""
COVID-19 and VACCINE in Iran & Usa & World
from API disease.sh
Hossein JALILI
vaccines_produced.py
mehr 1400
ver 1.1
"""
import requests
import os

clear=lambda : os.system("cls")

try:
    api_covid = "https://disease.sh/v3/covid-19/vaccine"
except:
    print("can not connect !!!")

json_data=requests.get(api_covid).json()
#print(json_data)

source=str(json_data['source'])
#print("source:\t",source,"\n")

phases=json_data['phases']
data=json_data['data']


def main():
    clear()
    while True:
        try:
            print("------vaccines produced-------")
            print("| 1: Summary of information  |")
            print("| 2: Complete information    |")
            print("| 3: list of sponsors        |")
            print("| 4: list of candidate       |")
            print("| 5: list of mechanism       |")
            print("| 6: list of trialPhase      |")
            print("| 7: more details of per no  |")
            print("| 0: back to main menu       |")
            print("------------------------------")
            ch=int(input("Enter your number\t"))
            if ch==1:
                
                total_vaccine()
                end()
            elif ch==2:
                
                inf_total_vaccine()
                end()
            elif ch==3:
                
                list_of_sponsors()
                end()
            elif ch==4:
                
                list_of_candidate()
                end()
            elif ch==5:
                
                list_of_mechanism()
                end()
            elif ch==6:
                
                list_of_trialPhase()
                end()
            elif ch==7:
                
                details()
                end()
            elif ch==0:
                break
            elif ch not in range(0,8):
                clear()
                print("Enter number in range 0 to 7 !!!")
        except:
            clear()
            print("Enter number !!!")


def end():
    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()

def total_vaccine():
    clear()
    print("-Summary of information on vaccines produced-")
    print("--------------------------------")
    print("phases\t\t\t","candidates")
    for j in range(len(phases)):
        print(phases[j]['phase'],"\t\t",phases[j]['candidates'])
    print("total:",len(phases),"\t\ttotal:",json_data['totalCandidates'])  
    print("--------------------------------\n")

def inf_total_vaccine():
    clear()
    for i in range(len(data)):
        print("-----------------NO:",i+1,"---------------\n")
        print("@ candidate:\t\t",data[i]['candidate'])
        print("@ mechanism:\t\t",data[i]['mechanism'])
        print("@ sponsors:\t\t",data[i]['sponsors'][0])
        print("@ trialPhase:\t\t",data[i]['trialPhase'])
        print("\n@ institutions:\n",data[i]['institutions'][0],"")
    
def list_of_sponsors():
    clear()
    print("----------------- list of sponsors---------------")
    for i in range(len(data)):
        print(i+1," ",data[i]['sponsors'][0])

def list_of_candidate():
    clear()
    print("----------------- list of candidate---------------")
    for i in range(len(data)):
        print(i+1," ",data[i]['candidate'])

def list_of_mechanism():
    clear()
    print("----------------- list of mechanism---------------")
    for i in range(len(data)):
        print(i+1," ",data[i]['mechanism'])

def list_of_trialPhase():
    clear()
    print("----------------- list of trialPhase---------------")
    for i in range(len(data)):
        print(i+1," ",data[i]['trialPhase'])

def details():
    clear()
    try:
        q=int(input("Enter 'NO' code :\t"))
        if q in range(len(data)) :
            print("-----------------NO:",q,"---------------\n")
            print("@ candidate:\t\t",data[q]['candidate'])
            print("@ mechanism:\t\t",data[q]['mechanism'])
            print("@ sponsors:\t\t",data[q]['sponsors'][0])
            print("@ trialPhase:\t\t",data[q]['trialPhase'])
            print("\n@ institutions:\n",data[q]['institutions'][0],"")
            print("\n@ details:\n",data[q]['details'],"\n")
        else :
            print("Enter number in range ")
    except:
        print("Enter number !! ")





