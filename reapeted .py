outputFile = open('UpdatedFile.txt', "w")
inputFile = open('C://Users//shyle//Downloads//Repeated.txt', "r")
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
for line in inputFile:
      if line not in lines_seen_so_far:
            outputFile.write(line)
inputFile.close()
outputFile.close()