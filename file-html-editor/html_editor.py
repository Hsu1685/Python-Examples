import glob
import os
# print(os.getcwd())    # Show current working folder
os.chdir("html_editor")

with open("TestReport.htm", "r", encoding="utf-8") as r:    # Open file(Automatically clsoe): read(encoding="utf-8" Corresponding to Chinese and other language)
    line_list = []
    line = 0
    for find_lines in r.readlines():            # Repeated execution lines = read_file.readlines()
        p1 = find_lines.find("<P><LEFT>")       # Find "<p> <left>" location
        p2 = find_lines.find("%</LEFT>")        # Find "% </ left>" location
        line = line + 1                         # Calculate the current number of lines
        if (p1 != -1) & (p2 != -1):             # Find the number of rows of strings
            slice_string = find_lines[p1+9:p2]  # Captive character fragment
            if int(slice_string.strip()) < 100: # Remove the string space, check if it is less than 100%
                line_list.append(line)          # Save the current number of lines

# print(line_list)    # Show all the number of lines identified

with open("TestReport.htm", "r", encoding="utf-8") as r:    # Open file(Automatically clsoe): read(encoding="utf-8" Corresponding to Chinese and other language)
    read_lines = r.readlines()
    for x1 in line_list:
        read_lines[x1 - 2] = read_lines[x1 - 2].replace('<TD>', '<TD BGCOLOR="#FF8686">')
    # print(read_lines)    # Show read_lines content

with open("TestReport_modify.htm", "w", encoding="utf-8") as w:   # Open file(Automatically clsoe):: write(If don't exist make a new one)
    for data in read_lines:
        w.write(data)
        w.flush()
