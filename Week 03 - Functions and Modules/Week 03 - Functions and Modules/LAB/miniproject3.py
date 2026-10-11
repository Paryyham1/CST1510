"""
RECORD CHECK  -  my version
===========================

Name  : parham 
Lane  : IT
Date  : 10-10-2026

Run it:   python template.py


"""

#FUNCTIONS
def status_of(percent):
    """return "OVER LIMIT", "WARNING" or "OK" for a given percentage"""
    if percent >= 100:       #100% or more means the limit is passed
        return "OVER LIMIT"
    elif percent >= 90: #90 to just under 100% means we are close
        return "WARNING"
    else:                    #else is safe
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value"""
    difference = value - limit   
    percent = (value / limit) * 100
    return difference, percent     #send both back to the main loop


def print_report(label, value, limit, difference, percent, status):
    """print the full bordered report to print one record"""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    print(f" value: {value:>12.2f}")
    print(f" limit : {limit:>12.2f}")
    print(f" difference: {difference:>12.2f}")
    print(f" percent: {percent:12.2f}")
    print(f" status: {status:>12}")    #text so just >12 no need .2f
    print("=" * 34)

#input
over_limit_counts = 0
while True:
    label = input("label('quit' to stop):")
    label == "quit"
    break
value = float(input("value: "))
limit = float(input("limit:"))

#process
difference, percent = check(value, limit)
status = status_of(percent)
if status == "OVER LIMIT":
    over_limit_counts += 1

#output
print_report(label, value, limit, difference, percent, status)
print()
print(f"records over limit: {over_limit_counts}")
    
    
