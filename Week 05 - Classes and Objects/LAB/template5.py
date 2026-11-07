"""
RECORD CHECK  -  my version
===========================

Name  : Parham hajinia
Lane  : IT 
Date  :

Run it:   python template.py

"""

class Record:
    """A labelled reading with a value and a limit."""

    def __init__(self, label, value, limit):
        """Store the label, value and limit on this record."""
        self.label = label      # name of the record
        self.value = value      # the current reading
        self.limit = limit      # the maximum allowed

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value against limit."""
        percent = self.value / self.limit * 100   # how much of the limit is used
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
#CLASS


def w_file(path):
    """Write the sample data into a txt file."""
    datas = "reze-01,70,100\nreze-02,92,100\nreze-03,150,120\nreze-04,60,80\nreze-05,200,200\n"
    with open(path, "w") as file:
        file.write(datas)


def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    loaded = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()          # remove the newline and spaces
            if line == "":
                continue                 # skip blank lines
            parts = line.split(",")      # split into label, value, limit
            loaded.append(Record(parts[0], float(parts[1]), float(parts[2])))
    return loaded


w_file("records.txt")                    # create the data file first
records = load_records("records.txt")    # then load it into Record objects

#RECORDS


over_limit_count = 0    # running total of OVER LIMIT records

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Label  : {record.label}")
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")
    if record.status() == "OVER LIMIT":
        over_limit_count += 1            # count it for the final total

    print("=" * 34)

print()
print(f"Records over limit: {over_limit_count}")   # printed once, after the loop

#OUTPUT