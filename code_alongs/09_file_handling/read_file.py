from pathlib import Path

# __file__ -> absolute path to this script
# .parent -> parent directory of this script
# / "data" -> add this directory to the path
# "r" = read "w" = write
DATA_PATH = Path(__file__).parent / "data"  # dunder file , .parent (folder) sen tillbaka till "data" inom parentfolder

print(DATA_PATH)

print("hej")




print("Reading a file")

# open up quotes.txt and print it

# with open("data/quotes.txt", "r") as file:
#     print(file.read())

#file_path_absolute = "/Users/oskarsvalin/Documents/github/python_oskar_aiu26/code_alongs/09_file_handling/data/quotes.txt"

with open(DATA_PATH / "quotes.txt", "r") as file:
    print(file.read())