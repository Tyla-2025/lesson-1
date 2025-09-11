file_read = open('C://Users//shyle//Desktop//python.tari//module1//Codingal.txt','r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open('C://Users//shyle//Desktop//python.tari//module1//Codingal.txt', 'w')
file_write.write(" File in write mode ....")
file_write.write("Hi!I am penguin. I am 1 yr. old ")
file_write.close()

file_append = open('C://Users//shyle//Desktop//python.tari//module1//Codingal.txt', 'a')
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()