# AP Reburn Analysis.py

Attachment 14257, text, 2 KB, added 2023-04-27 by Ryan Ferguson.

# This code will look at the directory "path" and identify how many AP SN's have more than one burn-in file entry.
# These files should be pulled directly from Dexter and put into one single folder "path" to do analysis
# Current version of code limits files analyzed to only those produced after Jan 1 2021

import os

# Get the list of all files and directories
file = open("AP SNs.txt", "a")
path = "C:/Users/rferguson/Python/Green_AP_Investigation/Data"

dir_list = os.listdir(path)
dir_list.sort()

print("Files and directories in '", path, "'\n")
file.write("Files and directories in '" + path + "'\n")
file.write("Autopilot SN, Burn-In \n\n")

# for item in dir_list:  # Create a txt file with all files used in this script
#    item = item.rstrip(".csv").lstrip("acal")
#    file.write(item + "\n")

def fileparse(item):  # Parse file names into a tuple ordered (sn, datecode)
    item = item.rstrip(".csv").lstrip("acal")
    item = item.split("-")
    sn = int(item[0])
    datecode = str(item[1])
    return(sn, datecode)

total = 0
sncount = {}
for item in dir_list: # Count the number of times each SN is in the dir list
    total = total + 1
    sn = fileparse(item)[0]
    date = fileparse(item)[1]
    year = int(date[0:2])
    if year < 21:  #Filter results to only those produced after Jan 1, 2021.
        continue
    if sn in sncount:
        sncount[sn] = sncount[sn] + 1
    else:
        sncount[sn] = 1

reburncount = 0
for sn in sncount:  # Identify re-burns
    count = sncount[sn]
    if count > 1:
        file.write(str(sn) + " " + str(count) + "\n")
        print(sn,count)
        reburncount = reburncount + 1

# Output statistics
file.write("\n\n---------- STATISTICS ----------\n")
file.write("Total number of files analyzed: " + str(total) + " Files\n")
analyzedSns = str(len(sncount))
file.write("Total number of SN's produced since Jan 1 2021: " + analyzedSns + " SN's \n")
file.write("Total number of reburned autopilots: " + str(reburncount) + " Autopilots\n")
percent = reburncount / int(analyzedSns) * 100
percent = int(percent)
file.write("Percentage of autopilots reburned: " + str(percent) + " %")
