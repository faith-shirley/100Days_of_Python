age = int(input("Enter your age."))
if age <= 15:
    ticket_price = 500
elif age <= 30:
    ticket_price = 1000
else:
    ticket_price = 2000
print(f"Ticket price: UGX{ticket_price}")