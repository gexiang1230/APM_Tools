import decimal
name = "allen"
f"He said his name is {name}."
'He said his name is allen.'
width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"{{result: {value:{width}.{precision}}}}")  # nested fields
