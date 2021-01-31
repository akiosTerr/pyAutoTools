def create_file(file_name):
    f = open(file_name+".txt", "w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()
    print("file %s created" % file_name)


def append_file(word, filename):
    file_object = open(filename+".txt", "a+")
    for i in range(4):
        file_object.write("Appended %s %d\r\n" % (word, i + 1))


