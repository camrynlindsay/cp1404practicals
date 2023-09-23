"""
Pseudocode
get cents_per_kWh
get daily_use_kWh
get number_of_billing_days
estimated_bill = (cents_per_kWh / 100) * daily_use_kWh * number_of_billing_days
print estimated_bill
"""


# print("Electricity bill estimator")
# cents_per_kWh = float(input("Enter cents per kWh: "))
# daily_use_kWh = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# estimated_bill = (cents_per_kWh / 100) * daily_use_kWh * number_of_billing_days
# print(f"Estimated bill: {estimated_bill}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff_choice == 11:
    tariff_rate = TARIFF_11
else:
    tariff_rate = TARIFF_31
estimated_bill = tariff_rate * daily_use_kWh * number_of_billing_days
print(f"Estimated bill: {estimated_bill:.2f}")
