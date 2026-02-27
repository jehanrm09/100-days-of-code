f1 = open("python1.txt", "r")
f2 = open("python2.txt", "r")
fileOne = f1.readlines()
fileTwo = f2.readlines()
f1.close()
f2.close()

for index,line in enumerate(fileOne):
    if line!= fileTwo[index]:
        for ind,char in enumerate(line):
            if char!=fileTwo[index][ind]:
                print("line number",index+1,"colum",ind+1)
                break
        break