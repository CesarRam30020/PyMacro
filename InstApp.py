from tkinter import Tk
# from pyautogui import moveTo, move, click, write, press
from InstructionsFrame import InstructionsFrame
from ButtonsFrame import ButtonsFrame

class InstApp:
  def __init__(self):
    # Constants
    self.root = Tk()
    self.root.title("Instructions Runner")
    self.createWindow = None

    instructionsFrame = InstructionsFrame(self.root)
    instructionsFrame.grid(row=0, column=0)

    buttonsFrame = ButtonsFrame(
      self.root,
      instructionsSet = instructionsFrame.instructionsSet,
      createWindow = self.createWindow
    )
    buttonsFrame.grid(row=1, column=0)

    self.root.mainloop()