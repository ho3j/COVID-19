"""
COVID-19 and VACCINE in Iran & Usa & World
from API disease.sh
Hossein JALILI
mehr 1400
main.py
ver 1.1
"""
import vaccines_produced as vp
import covid_19 as co

def main_():
    vp.clear()
    while True:
        try:
            print("-----------COVID-19-----------")
            print("| 1: Vaccines produced menu  |")
            print("| 2: Covid-19 in worldwide   |")
            print("| 3: Covid-19 in usa         |")
            print("| 4: Covid-19 in iran        |")
            print("| 5: Injected vaccine        |")
            print("| 0: exit                    |")
            print("------------------------------")
            ch=int(input("Enter your number\t"))
            if ch==1:
                vp.main()
                vp.end()
            elif ch==2:
                
                co.c_19_world()
                vp.end()
            elif ch==3:
                
                co.c_19_usa()
                vp.end()
            elif ch==4:
                
                co.c_19_iran()
                vp.end()
            elif ch==5:
                
                co.Injected_vaccine()
                vp.end()

            elif ch==0:
                break
            elif ch not in range(0,8):
                vp.clear()
                print("Enter number in range 0 to 7 !!!")
        except:
            vp.clear()
            print("Enter number !!!")

try:
    main_()
except:
    print("cant not run !!")