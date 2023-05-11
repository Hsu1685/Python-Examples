import glob
import os
# print(os.getcwd())    # Show current working folder
os.chdir("CSV_Editor")

with open("BATopr.csv", "a", encoding="utf-8") as w:   # Open file(Automatically clsoe):: write(If don't exist make a new one)
    for i in range(65536):
        w.write("," + str(i) +",,,," + "\n")
        w.flush()