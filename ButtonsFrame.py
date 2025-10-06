from tkinter import Frame, Button
from scripts.scripts import runInstructions

class ButtonsFrame(Frame):
  def __init__(self, root, instructionsSet, createWindow):
    super().__init__(root)

    self.startButton = Button(
      self,
      text="RUN",
      command=lambda: self.runInstructions(instructionsSet.get())
    )
    self.startButton.grid(row=0, column=0)

    self.createButton = Button(
      self,
      text="CREATE",
      command=lambda: createWindow.activate()
    )
    self.createButton.grid(row=0, column=1)
  
  def runInstructions(self, file):
    try:
      runInstructions(file)
    except ValueError as e:
      print(f"Error: {e}")