#!/usr/bin/env python

##count = 0

nodeName = ""

    ##print(file)
    ##print(file1)
    ##print(file2)

file = "/Users/sai2e/Downloads/4155_Data/9-30.txt"
    ##print(i)
with open(file, encoding = 'UTF-8') as f:
    line = f.readline()
    print("First line: " + line)

s = "profmgr["
s1 = "cfgm["
s2 = "stm["
s3 = "<AtkiG20-C5-A7280-1 10.47.0.22>"
s4 = "authmgr["
s5 = "fpapps["


        
if s in line:
    nodeName = line[31:line.find(" profmgr[")]
elif s1 in line:
    nodeName = line[31:line.find(" cfgm[")]
elif s2 in line:
    nodeName = line[31:line.find(" stm[")]
elif s3 in line:
    nodeName = line[31:line.find(" <AtkiG20-C5-A7280-1 10.47.0.22>")]
elif s4 in line:
    nodeName = line[31:line.find(" authmgr[")]
elif s5 in line:
    nodeName = line[31:line.find(" fpapps[")]


file1 = "/Users/sai2e/Downloads/9-30_sorted/" + str(nodeName) + ".txt"
print("File1: " + file1)
print("Node name: " + nodeName)


with open(file, encoding = 'UTF-8') as f:
	with open(file,encoding = 'UTF-8') as f3:
		with open(file1, "w", encoding = 'UTF-8') as f1:
	
			file2 = "/Users/sai2e/Downloads/9-30_data/Copy_" + str(1) + ".txt"
			with open(file2, "w",encoding = 'UTF-8') as f2:
				print("Worked")
				for line in f:
					if "2019-09-30" in line:
						if s in line:
							if line[31:line.find(s)] == nodeName + " ":
								f1.write(line)
								##print("Worked00000000000000000")
						elif s1 in line:
							if line[31:line.find(s1)] == nodeName + " ":
								f1.write(line)
								##print("Worked1111111111111111111111111")
						elif s2 in line:  
							if line[31:line.find(s2)] == nodeName + " ":
								f1.write(line)
								##print("Worked2222222222222222222222222222")
						elif s3 in line:
							if line[31:line.find(s3)] == nodeName + " ":
								f1.write(line)
								##print("Worked33333333333333333333333333333")
						elif s4 in line:
							if line[31:line.find(s4)] == nodeName + " ":
								f1.write(line)
								##print("Worked444444444444444444444444444")
						elif s5 in line:
							if line[31:line.find(s5)] == nodeName + " ":
								f1.write(line)
								##print("Worked5555555555555555555555555555555555555")

				for line in f3:
					if "2019-09-30" in line:
						if s in line:
							if line[31:line.find(s)] != nodeName + " ":
								f2.write(line)
						elif s1 in line:
							if line[31:line.find(s1)] != nodeName + " ":
								f2.write(line) 
						elif s2 in line:
							if line[31:line.find(s2)] != nodeName + " ":
								f2.write(line)
						elif s3 in line:
							if line[31:line.find(s3)] != nodeName + " ":
								f2.write(line)
						elif s4 in line:
							if line[31:line.find(s4)] != nodeName + " ":
								f2.write(line)
						elif s5 in line:
							if line[31:line.find(s5)] != nodeName + " ":
								f2.write(line)