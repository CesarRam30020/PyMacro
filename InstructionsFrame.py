from scripts.scripts import getInstructionFiles, deleteInstructionFile
from tkinter import StringVar, Frame, Button, Radiobutton

class InstructionsFrame(Frame):
  def __init__(self, root):
    super().__init__(root)
    self.instructionsSet = StringVar()
    self.instructionsSet.set(None)

    self.getInstructionsSet()

  def getInstructionsSet(self):
    instructionsFiles = getInstructionFiles()

    for i, file in enumerate(instructionsFiles):
      rb = Radiobutton(
        self,
        text = file,
        variable = self.instructionsSet,
        value = file,
        command = lambda f = file: print(f"File: {f}"),
      )
      rb.grid(row=i, column=0, sticky="w")

      delBtn = Button(
        self,
        text = "X",
        command = lambda f = file: deleteInstructionFile(f) and self.reBuild(),
      )
      delBtn.grid(row=i, column=1)

  def reBuild(self):
    for widget in self.winfo_children():
      widget.destroy()
    self.getInstructionsSet()