with open("words.txt", "r") as infile:
    text = infile.read().split()
    for words in range(len(text)):
        new = ""
        if len(text[words]) > 3:
            for j in range(len(text[words])):
                if j == 0:
                    first = text[words][j]
                elif text[words][j] != ".":
                    new = new + text[words][j]

            new = new + first + "ay"
            print(new)
