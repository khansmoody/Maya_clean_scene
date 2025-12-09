import maya.cmds as cmds
import datetime

class SceneCleanerUI:


    def __init__(self):
        self.window = "SceneCleanerUI"
        self.log_field = "logField"
        self.build()


    # -------------------------------------------
    # LOGGING SYSTEM

    def log(self, message, level = "INFO"):

        # 1. Time Prefix
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}][{level}] {message}"
        
        # Try: Add word at scrollField(log page)
        # Else: If there's no UI, print with console
        try:
            cmds.scrollField(self.log_field, e = True, insertText = formatted + "\n")
            cmds.scrollField(self.log_field, e = True, scrollBottom = True)
        except Exception:
            print(formatted)



    # -------------------------------------------
    # CALLBACK FUNCTIONS

    def on_info(*_):
        self.log("Hello clicked!")

    def on_warn(*_):
        self.log("This is a warning!", level = "WARN")

    def on_error(*_):
        self.log("Something went wrong!", level = "ERROR")



    # -------------------------------------------------------
    # BUILD UI

    def create_ui(self):
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window)

        # Generating Window/Layout
        cmds.window(self.window, title = "Scene Cleaner 2.0", widthHeight = (350, 260))
        cmds.columnLayout(adjustableColumn = True)

        # Buttons
        cmds.button(label = "Log Info", command = self.on_info)
        cmds.button(label = "Log Warning", command = self.on_warn)
        cmds.button(label = "Log Error", command = self.on_error)

        cmds.separator(height = 10, style = "in")

        # Log Field
        cmds.scrollField(self.log_field, editable = False, wordWrap = True, height = 150)

        cmds.showWindow(self.window)


    create_ui()