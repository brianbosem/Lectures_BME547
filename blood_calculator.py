print("This is the blood_calculator.py module")
print("Its name is {}".format(__name__))

def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("\nMake a choice")
        print("1 = HDL Analysis")
        print("2 = LDL Analysis")
        print("3 = Total Cholesterol Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        elif choice == 3:
            TOT_Driver()
    print(choice)
    return choice

##### HDL #####
def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)

def hdl_input():
    hdl_value = int(input("Enter HDL value: "))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 < HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low" 

def hdl_output(HDL_value, HDL_character):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_character))

##### LDL #####
def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)

def ldl_input():
    ldl_value = int(input("Enter LDL value: "))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 159:
        return "Borderline High"
    elif 160 < LDL_value < 189:
        return "High"
    else:
        return "Very High" 

def ldl_output(LDL_value, LDL_character):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_character))

##### Total #####
def TOT_Driver():
    TOT_value = tot_input()
    TOT_character = tot_analysis(TOT_value)
    tot_output(TOT_value, TOT_character)

def tot_input():
    tot_value = int(input("Enter Total Cholesterol value: "))
    return tot_value

def tot_analysis(tot_value):
    if tot_value < 200:
        return "Normal"
    elif 200 <= tot_value < 239:
        return "Borderline High"
    else:
        return "High" 

def tot_output(TOT_value, TOT_character):
    print("The total cholesterol value of {} is considered {}".format(TOT_value, TOT_character))


##### Run Interface ######
if __name__ == "__main__":
    interface()

