def converter(amount,rate):
    amount = amount*rate
    return amount

usd_to_eur_rate=0.86
usd_to_inr_rate=90.90
usd_to_gbp_rate=0.74

# amount in USD dollar
my_amount=100

euros = converter(my_amount, usd_to_eur_rate)
rupees=converter(my_amount, usd_to_inr_rate)
pounds=converter(my_amount, usd_to_gbp_rate)

print(f"--- Currency Report for ${my_amount} ---")
print(f"In Euros: €{euros}")
print(f"In India: ₹{rupees}")
print(f"In British Pounds: £{pounds}")

# testing with different amount
print(f"Testing for small amount($5) in Euros: €{converter(5,usd_to_eur_rate)}")