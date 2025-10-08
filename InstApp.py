from tkinter import Tk
from InstructionsFrame import InstructionsFrame
from ButtonsFrame import ButtonsFrame
from CreateWindow import CreateWindow
from scripts.scripts import runInstructions

class InstApp:
  def __init__(self):
    self.root = Tk()
    self.root.title("Instructions Runner")
    self.child_window = None

    instructionsFrame = InstructionsFrame(self.root)
    instructionsFrame.grid(row=0, column=0)

    buttonsFrame = ButtonsFrame(
      self.root,
      # instructionsSet = instructionsFrame.instructionsSet,
      # on_create = self.handle_on_create,
      buttons=[
        {
          "text": "RUN",
          "command": lambda: self.runInstructions(
            instructionsFrame.instructionsSet.get()
          )
        },
        {
          "text": "CREATE",
          "command": self.handle_on_create
        }
      ]
    )
    buttonsFrame.grid(row=1, column=0)

    self.root.mainloop()

  def handle_on_create(self):
    self.child_window = CreateWindow("Create New Ins File")
  
  def runInstructions(self, file):
    try:
      runInstructions(file)
    except ValueError as e:
      print(f"Error: {e}")