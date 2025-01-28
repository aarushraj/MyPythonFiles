std_marks = {
    "Alice": {"Physics": 85, "Chemistry": 78, "Mathematics": 92},
    "Bob": {"Physics": 74, "Chemistry": 88, "Mathematics": 81},
    "Charlie": {"Physics": 90, "Chemistry": 67, "Mathematics": 85},
    "Diana": {"Physics": 79, "Chemistry": 82, "Mathematics": 88},
    "Eve": {"Physics": 92, "Chemistry": 80, "Mathematics": 94},
}


myList = std_marks.items()
print(myList)
print(type(myList))
std_avg = {}
"""
for key in std_marks:
    marksheet = std_marks[key]
    avg = (sum)(list(marksheet.values()))/3
    std_avg.update({key:avg})

print("Student average: ")
print(std_avg)

cls_high = {}
high = std_avg["Alice"]
for name in std_avg:
    if std_avg[name]>high:
        high = std_avg[name]
        cls_high.update({name:high})
print("Class Highest: ", cls_high)
"""

