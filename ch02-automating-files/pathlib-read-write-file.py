from importlib.resources import path
import pathlib

path = pathlib.Path("/Users/danghai/Dev/Learn-dev/python-for-devops/ch02-automating-files/text.txt")
text = path.read_text()
print(text)
