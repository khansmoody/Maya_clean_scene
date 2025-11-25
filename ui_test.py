import maya.cmds as cmds
import datetime

# Method for printing log out
def log(msg, level = "info"):

    # 1. Time Prefix
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    formatted = "[{}][{}] {}".format(timestamp, level, msg)
    
    # Try: Add word at scrollField(log page)
    # Else: Just print()
    try:
        prev = cmds.scrollField("logField", q = True, text = True)
        cmds.scrollField("logField", e = True, text = prev + msg + "\n")
    except:
        print(msg)



# Method activates right after click
def on_button_click(*args):
    log("Hello clicked!")

def on_button_warning(*args):
    log("This is a warning!", level = "WARN")

def on_button_error(*args):
    log("Something went wrong!", level = "ERROR")


# Method generates UI
def create_ui():
    if cmds.window("TestUI", exists = True):
        cmds.deleteUI("TestUI")

    # Generating Window/Layout
    window = cmds.window("TestUI", title = "Test UI", widthHeight = (350,250))
    cmds.columnLayout(adjustableColumn=True)

    # Button
    cmds.button(label = "Log Info", command = on_button_click)
    cmds.button(label = "Log Warning", command = on_button_warning)
    cmds.button(label = "Log Error", command = on_button_error)

    cmds.separator(height = 10, style = "in")

    # Log page
    cmds.scrollField("logField", editable = False, wordWrap = True, height = 150)

    cmds.showWindow(window)
    
create_ui()