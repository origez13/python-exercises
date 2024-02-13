temp_of_choice = input("choose the starting temprature (F or  C) ")
temp_value = int(input("choose the value: "))

#from f to c
if temp_of_choice == "F":
    conversion_value = (temp_value - 32) * (5 / 9)
    print(f"{temp_value} from f to c will be {conversion_value}")

#from c to f
elif temp_of_choice == "C":
    conversion_value = (temp_value) * (9 / 5) + 32
    print(f"{temp_value} from c to f will be {conversion_value}")
else:
    print("invaild choice")
