

file_path = r"C:\Users\flori\OneDrive\Desktop\Python\ExampleFile1.txt"


opened_file = open(file_path, "a")

opened_file.write("this is a really cool file.\n")

opened_file.close()


opened_file = open(file_path, "r+")

##content = opened_file.read()
##print(content)
print("---")
content = opened_file.readlines()
print(content)

opened_file.write("this shouldn't work")

for i in content:
    print(i)

opened_file.close()
