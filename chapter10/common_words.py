def common_words(filename, word):
    text = ""
    try:
        with open(filename) as file_obj:
            for line in file_obj:
                text += line.rstrip()
        # print(text)
    except FileNotFoundError as fe:
        print(f"{fe.filename} is not found")
        exit

    

filename = input("Enter File Name? ")    
while True:
    word = input("Enter word to search for? ")
    if word == "q":
        break
    totalCnt = common_words(filename, word)
    print(f"{word} is contained {totalCnt} times in file {filename}")
