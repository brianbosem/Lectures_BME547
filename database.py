print("This is the database.py module")
print("Its name is {}".format(__name__))

# import blood_calculator
# from blood_calculator import hdl_analysis
import blood_calculator as bc

# answer = blood_calculator.hdl_analysis(55)
# answer = hdl_analysis(55)
answer = bc.hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

# answer2 = blood_calculator.ldl_analysis(200)
# answer2 = ldl_analysis(200)
answer2 = bc.ldl_analysis(55)
print("The analysis of 200 LDL is {}".format(answer2))