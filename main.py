# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = 77
    print(a)

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7,
           21.8, 21.3, 20.9, 20.1]
C = np.array(cvalues)
print(C, type(C))

print(C.size)
plt.plot(C)
plt.show()

students = ["Max", "Monika", "Fritz", "Paul", "Rudi"]
cpy = students.copy()
cpy.append("Michael")

students.sort(reverse=True, key=len)
print(str(len(students)) + ": " + str(students))

students.reverse()
print(str(len(students)) + ": " + str(students))

dummy = students.pop()
students.remove(students[2])

print(str(len(students)) + ": " + str(students))
print(dummy)
print(str(len(cpy)) + ": " + str(cpy))

print("test")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
