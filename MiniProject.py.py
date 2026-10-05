"""
RECORD CHECK  -  my version
===========================

Name  : Parham 
Lane  : IT 
Date  : 02-10-2026
"""
# input
label = input("name / hostname / IP: ")
first = float(input("first number: "))
second = float(input("second number:"))

# process 
difference = first - second
percent = (first / second) * 100

# output
print()
print("=" * 34)
print(f" record check ) - {label}")
print("=" * 34)
print(f" first : {first:>10.2f}")
print(f" second : {second:>10.2f}")
print(f" difference {difference:>+10.2f}")
print(f" percent : {percent:>10.2f}")
print(f" summary :{label} is at {percent:.2f}% of the second value")
print("=" * 34)