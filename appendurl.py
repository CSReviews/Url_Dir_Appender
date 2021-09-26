url = input("input URL \nex. www.example.com/\n>")
inputFile = input("Input txt file of directories\nex. dirs.txt \n>")

urlList = []
with open(inputFile , 'r') as file:
    urlList = [line.strip() for line in file]
#print(urlList)

my_new_list = [url + x  for x in urlList]
print(my_new_list)

f = open("urlList.txt", "w+")

for element in my_new_list:
    f.write(element + "\n")
f.close()