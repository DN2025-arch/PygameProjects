

file_path = r"C:\Users\flori\OneDrive\Desktop\Python\CounterFile.txt"

##file = open(file_path, "w")

content = """
This is line 1.
This is line 2.
Python file handling is easy.
You can read this file.
You can write new data
You can append more text
t.End of file
"""
##file.write(content)
##
##file.close()


file = open(file_path, "r")
content = file.readlines()
print(content)
wordcount = len(content)
print(wordcount)

file.close()
