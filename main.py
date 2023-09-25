def read_file(filename):
    with open(filename, 'r') as file:
        f = file.read()
        print(f)
    return f
    file.close()


def occurrence_words(filecontent):
    words = filecontent.split(" ")
    occ = {item: words.count(item) for item in words}
    print(occ)


if __name__ == '__main__':
    w = read_file('input.txt')
    occurrence_words(w)
