'''import csv
f = open("data.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["S.No", "Name", "Department"])
writer.writerow([1, "Alice", "Computer Science"])
writer.writerow([2, "Bob", "Mathematics"])
writer.writerow([3, "Charlie", "Physics"])
f.close()'''



import csv
f = open("data.csv", "r")
reader = csv.reader(f)
for i in reader:
    print(i)
f.close()#csvreader is used to read data from a CSV file row by row.

