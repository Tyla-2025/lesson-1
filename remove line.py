file1 = open('C://Users//shyle//Desktop//python.tari//module1//Codingal.txt','r')
file2 = open('C://Users//shyle//Desktop//python.tari//module1//CodingalUpdated.txt','w')
for line in file1.readlines():
       if not (line.startswith('Coding')):
        print(line)

        file2.write(line)
file2.close()
file1.close()