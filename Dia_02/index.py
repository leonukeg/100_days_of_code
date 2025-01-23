print("Welcome to the tip calculatos")
bill = float(input("total de dinero"))
tip = int(input("cual es el el porcentaje asignado para la propina? 10 12 15 "))
people = int(input("cuantas personas reciben propina?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"cada persona debe recibir: ${final_amount}")
