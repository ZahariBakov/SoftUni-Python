import re

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

count_of_barcodes = int(input())

for i in range(count_of_barcodes):
    product_group = ""
    current_barcode = input()
    matches = re.match(pattern, current_barcode)

    if matches:
        for char in matches.group():
            if char.isdigit():
                product_group += char

        if not product_group:
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
