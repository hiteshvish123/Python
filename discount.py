PURCHASE = int(input("Enter the amount of purchse: "))

if 0 <= PURCHASE <= 5000:
    DIS = 0
if 5001 <= PURCHASE <= 10000:
    DIS = 0.05 * PURCHASE
if 10001 <= PURCHASE <= 25000:
    DIS = 0.1 * PURCHASE
if 25001 <= PURCHASE <= 40000:
    DIS = 0.15 * PURCHASE
if 40001 <= PURCHASE <= 100000:
    DIS = 0.18 * PURCHASE
if PURCHASE > 100000:
    DIS = 0.2 * PURCHASE

print(f"Discount= {round(DIS)}")
print(f"Amount= {PURCHASE-round(DIS)}")
