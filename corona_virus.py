from covid import Covid
import time
covid = Covid()
loop = 0
while loop < 1:
    print('*' * 10)
    print("welcome to kareena vimrus chemker")
    print('*' * 10)
    print("")
    print("Select the options from below")
    print("""
    press 1 for Global-Active cases
    press 2 for Global-Confirmed cases
    press 3 for Global-Recovered cases
    press 4 for Global-Death cases
    press 5 for Entering country name
    """)
    print("")
    ui = input("please select a Number : ")
    if ui == "1":
        print("Total Active cases is :", covid.get_total_active_cases())
        time.sleep(2)
    if ui == "2":
        print("Total confirmed cases is :", covid.get_total_confirmed_cases())
        time.sleep(2)
    if ui == "3":
        print("Total Recovered cases is :", covid.get_total_confirmed_cases())
        time.sleep(2)
    if ui == "4":
        print("Total Deaths is :", covid.get_total_deaths())
        time.sleep(2)
    if ui == "5":
        ux = input("Enter the country name : ")
        print("")
        zak = (covid.get_status_by_country_name(ux))
        for i in zak:
            print(i, ":", zak[i])
        time.sleep(10)
    man = int(ui)
    if man >= 6:
        print("Please select a valid Number")
    else:
        print("Install brain.com")
loop += 1
