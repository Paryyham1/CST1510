"""
RECORD CHECK  -  my version
===========================

Name  : parham
Lane  : IT 
Date  :

Run it:   python template.py


"""

#input
over_limits_counts = 0
while True : 
    label = input("label (or 'quit' to stop ):")
    if label == "quit":
        break
    value = float(input("value: "))
    limit = float(input("limit: "))

#proces
difference = value - limit 
percent = value / limit * 100

#statuss
if percent >= 100:
    status = "over limit"
    over_limits_counts +=1
elif percent >=90:
    status = "WARNING"
else:
    status = "ok"

#output
print()
print("=" * 34)
print(f" record check - {label}")
print("=" * 34)
print(f" value : {value:>12.2f}")
print(f" limit : {limit:>12.2f}")
print(f" difference : {difference:>12.2f}")
print(f" percent : {percent:>11.2f}")
print(f" status : {status:>12}")
print("=" * 34)


