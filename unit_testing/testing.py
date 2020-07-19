with open("/home/prasad/PycharmProjects/PythonDev/unit_testing/testdata.txt", "r") as read_file:
    # conf = json.load(read_file)
    conf = read_file.readlines()
    print(type(conf))

    for i in conf:
        print(type(i))