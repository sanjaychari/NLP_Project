import os
import pandas as pd
import csv

dirs = os.listdir("Twitter_Data")
li = []
li.append(["Serial Number","Content","User_Id","Username","Label"])
label = 1
serial_no = 1
for i in dirs:
	if(not(i==".DS_Store")):
		path = "Twitter_Data/"+i+"/tweets.csv"
		df = pd.read_csv(path)
		for index,row in df.iterrows():
			if(row[4]=="Tweet"):
				if(row[3].find("https://")==-1):
					li.append([serial_no,row[3],row[8],row[10],label])
					serial_no += 1
				else:
					li.append([serial_no,row[3][:row[3].find("https://")],row[8],row[10],label])
					serial_no += 1
		label += 1

with open("dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(li)

