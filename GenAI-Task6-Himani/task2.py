prices=[120, 350, 'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        if price <0:
            print(f"Negative price '{price}' skipped.")
            continue
        total += price
    except TypeError:
        print(f"Invalid price '{price}' skipped.")
        continue
    

print(f"Total price: {total}")