import configparser
data_file = "data.ini"

file = open(data_file, "a")

for chapter in range(1, 36):
    for checkbox in range(1, 4):
        file.write("\nc" + str(chapter) + "_" + str(checkbox) + " = False")

file.close()
