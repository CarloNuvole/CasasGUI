import os

for elem in range(0,401):

    # 000 -> 009
    if (elem < 10):
        c = "00" + str(elem)

    #010 -> 099
    elif (elem >= 10 and elem < 100):
        c = "0" + str(elem)

    else:
        c = str(elem)

    file_path = "dataset/" + c + ".txt"

    try:
        file = open(file_path)

        with open(file_path) as f:
            l = sum(1 for _ in f)

        if l <= 1:
            print("Patient #" + c + " data are missing. File will be removed")
            file.close()
            os.remove(file_path)
        else:
            list = []
            fc = file.readline()

            while fc:
                if fc[0] != " ":
                    list.insert(len(list), fc[:-1])
                fc = file.readline()

            with open(file_path, 'w') as f:
                for item in list:
                    if item[-1] != " " and item.count(" ") < 3:
                        f.write("%s \n" % item)
                    else:
                        f.write("%s\n" % item)
            file.close()
            f.close()
    except FileNotFoundError:
        print("Patient #" + c + " data not found")

print("Database cleaned.")
