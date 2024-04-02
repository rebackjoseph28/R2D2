import platform
import json

buttons = {}

def button_map(filename):
    with open(filename) as json_file:
        buttons.update(json.load(json_file))

def os_adjust():
    print("OS: " + platform.system())
    if (platform.system() == "Windows"):
        filename = "joysticks/ps4_keys.json"
    elif (platform.system() == "Linux"):
        filename = "joysticks/gamepad.json"
    button_map(filename)
    


os_adjust()
print(buttons["triangle"])