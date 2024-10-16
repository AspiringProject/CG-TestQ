def librarycode(title, year):
    parta = title[0: 3]
    partb = year[2: 4]
    libraryCode = parta.upper() + partb
    return libraryCode

title = input("Enter the title of the book: ")
year = input("Enter the year the book was published: ")
code = librarycode(title, year)
file = open("library.txt", "a")
file.write(code + "\n")
file.close()
print("Library code: ", code)
print("Library code has been saved to library.txt")