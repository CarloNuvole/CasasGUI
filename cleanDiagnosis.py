file_path = 'diagnosis.txt'

try:
    file = open(file_path)
    with open(file_path) as f:
        for _ in range(15):
            next(f)
        list = ["0 0\n"]
        for l in f:
            list.insert(len(list), l)
            fc = file.readline()
        with open(file_path, 'w') as f:
            for item in list:
                    f.write("%s" % item)
        file.close()
        f.close()
        print("diagnosis.txt created.")

except FileNotFoundError:
    print("File not found")
