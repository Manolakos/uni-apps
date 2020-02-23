with open("words.txt", "r") as infile:
    words = infile.read().split()
    list = sorted(words, key=len, reverse=True)
    for i in range(5):
        new = ""
        for letter in (list[i] [::-1]):
            if not letter.lower() in "aeiouy":
                new = new + letter

        print(new)

