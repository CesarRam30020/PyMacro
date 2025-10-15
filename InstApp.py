from tkinter import Tk
from InstructionsFrame import InstructionsFrame
from ButtonsFrame import ButtonsFrame
from CreateWindow import CreateWindow
from scripts.scripts import runInstructions

class InstApp:
  def __init__(self):
    self.root = Tk()
    self.root.title("PyMacro")
    self.child_window = None

    self.instructionsFrame = InstructionsFrame(self.root)
    self.instructionsFrame.grid(row=0, column=0)

    buttonsFrame = ButtonsFrame(
      self.root,
      buttons=[
        {
          "text": "Correr",
          "command": lambda: self.runInstructions(
            self.instructionsFrame.instructionsSet.get()
          )
        },
        {
          "text": "Crear",
          "command": self.handle_on_create
        }
      ]
    )
    buttonsFrame.grid(row=1, column=0)

    self.root.mainloop()

  def handle_on_create(self):
    self.child_window = CreateWindow("Crear Nuevo .Ins")
    self.child_window.protocol("WM_DELETE_WINDOW", self.onWindowClosed)
  
  def onWindowClosed(self):
    self.child_window.destroy()
    self.instructionsFrame.reBuild()

  def runInstructions(self, file):
    try:
      runInstructions(file)
    except ValueError as e:
      print(f"Error: {e}")