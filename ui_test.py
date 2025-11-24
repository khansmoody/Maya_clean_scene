import maya.cmds as cmds

# Method for printing log out
def log(msg):
    # 1. Add word at scrollField(log page)
    # 2. Just print()
    try:
        prev = cmds.scrollField("logField", q=True, text=True)
        cmds.scrollField("logField", e=True, text=prev + msg + "\n")
    except:
        print(msg)

# Method activates right after click
def on_button_click(*args):
    log("Hello clicked!")

# Method generates UI
def create_ui():
    if cmds.window("TestUI", exists=True):
        cmds.deleteUI("TestUI")

    # Generating Window
    window = cmds.window("TestUI", title="Test UI", widthHeight=(300,200))

    # Layout
    cmds.columnLayout(adjustableColumn=True)

    # Button
    cmds.button(label="Test Button", command=on_button_click)

    # Log page
    cmds.scrollField("logField", editable=False, wordWrap=True, height=120)

    cmds.showWindow(window)
    
create_ui()