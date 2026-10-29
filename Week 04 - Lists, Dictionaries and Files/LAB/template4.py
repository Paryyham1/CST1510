"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  : IT  
Date  :

Run it:   python template.py


"""
def load_records(path):
    """read label,value,limit lines from a file and return a list of dicts."""
    records = []                          # always start with an empty list
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:                                                                                 # comprehension to clean fields
                a_list = [l.strip() for l in line.split(",")]
                label, value, limit = a_list                                                        # ValueError if not 3 fields
                records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


with open("gb_rec.txt","w") as f:
    while True:
        label = input("Enter hostname/label: ")
        value = input("Enter value: ")
        limit = input("Enter limit: ")

        f.write(f"{label},{value},{limit}\n")

        again = input("Add another?(y/n): ")
        if again != "y":
            break

try:
    records = load_records("gb_rec.txt")
except FileNotFoundError:
    print("Error: the file was not found")
    records = []
except ValueError:
    print("Error: a line is not label,value,limit with numbers")          
    records = []

print("\nRecords Entered:")
for record in records:
    print(record)
