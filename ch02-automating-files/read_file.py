with open("./text.txt", "r") as read_file:
    text = read_file.read()
    print(text[:10])
print(read_file.closed)
