import PySimpleGUI as sg
import configparser

data_file = "data.ini"
num_chapters = 10

config = configparser.ConfigParser()
config.read(data_file)

has_FR_default = config.getboolean("OWNED", "FR")
has_FL_default = config.getboolean("OWNED", "FL")
has_CP_default = config.getboolean("OWNED", "CP")
has_FS_default = config.getboolean("OWNED", "FS")

track_keys = []
x = 0
for chapter in range(1, num_chapters):
    for checkbox in range(1, 4):
        track_keys.append(config.getboolean("TRACK", "c" + str(chapter) + "_" + str(checkbox)))
        x = x + 1
print(f"num keys: {x}")

sg.theme("DarkPurple3")
layout = [[sg.Checkbox("FR", default=has_FR_default, key="has_FR"), sg.Text("Familia Romana")],
          [sg.Checkbox("FL", default=has_FL_default, key="has_FL"), sg.Text("Fabellae Latinae")],
          [sg.Checkbox("CP", default=has_CP_default, key="has_CP"), sg.Text("Colloquia Personarum")],
          [sg.Checkbox("FS", default=has_FS_default, key="has_FS"), sg.Text("Fabulae Syrae")],
          [sg.HorizontalSeparator()]]

# FIXME something here makes previous checkboxes return None
#for i in range(1, num_chapters * 3):
#    print(str(int(i / 3) + 1) + "_1")
#    print(str(int(i / 3) + 1) + "_2")
#    print(str(int(i / 3) + 1) + "_3")
#    layout.append([sg.Checkbox("", default=track_keys[int(i / 3) + 1], key=(str(i) + "_1")),
#                   sg.Checkbox("", default=track_keys[int(i / 3) + 1], key=(str(i) + "_2")),
#                   sg.Checkbox("", default=track_keys[int(i / 3) + 1], key=(str(i) + "_3")), sg.Text(i)])
#    i += 3

layout.append([sg.Button("Exit")])

window = sg.Window("LLSPI Tracker", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
print(values)
config["OWNED"]["FR"] = str(values["has_FR"])
config["OWNED"]["FL"] = str(values["has_FL"])
config["OWNED"]["CP"] = str(values["has_CP"])
config["OWNED"]["FS"] = str(values["has_FS"])

with open(data_file, "w") as configfile:
    print("Writing to ini")
    config.write(configfile)

window.close()
