# with open('notes.txt', 'r') as file:
    



    # for line in file: 
    #     print(line.strip())
with open('details.txt','w') as file:
    file.write("my name is mohan\n")
    file.write("my age is 20\n")
    print("done")


    # with open('notes.txt', 'a') as file:
    #     file.write("\nudhay\n")

try:
    with open('notes.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
