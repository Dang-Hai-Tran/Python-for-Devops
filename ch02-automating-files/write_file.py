text = "To write to a file, use the write mode, represented as the argument\n w. The tool direnv is used to automatically set up some\n development environments. You can define environment variables\n and application runtimes in a file named .envrc; direnv\n uses it to set these things up when you enter the directory\n with the file."
with open("./newtext.txt", "w") as write_file:
    result = write_file.write(text)
    print(result == len(text))
