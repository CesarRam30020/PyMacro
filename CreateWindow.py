from tkinter import Toplevel, Label, Entry, StringVar, Button, Text
from scripts.scripts import saveInstructions

class CreateWindow(Toplevel):
  def __init__(self, title = "Titulo"):
    super().__init__()
    self.title(title)

    self.row = 0
    self.fileNameStr = StringVar()
    self.textInsStr = StringVar()
    self.summaryStr = StringVar()
    self.clickWindow = None

    self.fileNameLbl = Label(self, text="Nombre del archivo: ")
    self.fileNameLbl.grid(row=self.getRow(), column=0)
    self.fileNameTxt = Entry(self, textvariable=self.fileNameStr)
    self.fileNameTxt.grid(row=self.getRow(-1), column=1)

    self.textInsLbl = Label(self, text="Texto a escribir: ")
    self.textInsLbl.grid(row=self.getRow(), column=0)
    self.textInsTxt = Entry(self)
    self.textInsTxt.grid(row=self.getRow(-1), column=1)
    self.textInsBtn = Button(self, text="+", command=self.addWriteInstruction)
    self.textInsBtn.grid(row=self.getRow(-1), column=2)

    self.awaitLbl = Label(self, text="Tiempo a esperar despues de la acción: ")
    self.awaitLbl.grid(row=self.getRow(), column=0)
    self.awaitTxt = Entry(self)
    self.awaitTxt.grid(row=self.getRow(-1), column=1)

    self.clickBtn = Button(self, text="click", command=self.clickEvent)
    self.clickBtn.grid(row=self.getRow(), column=0)
    self.saveBtn = Button(self, text="Guardar", command=self.saveInsFile)
    self.saveBtn.grid(row=self.getRow(-1), column=1)

    self.summaryTxt = Text(
      self,
      height=5,
      width=5,
      state="disabled"
    )
    self.summaryTxt.grid(row=self.getRow(), column=0, columnspan=3, sticky="nsew")

  def getRow(self, gap = 0):
    self.row += 1 + gap
    return self.row

  def addWriteInstruction(self):
    if self.textInsTxt.get() == "":
      return

    text = self.summaryTxt.get("1.0", "end-1c")
    text += f"\nwrite={self.textInsTxt.get()}"
    self.__writeTextSummary(text)

    if self.awaitTxt.get() != "":
      text = self.summaryTxt.get("1.0", "end-1c")
      text += f"\nawait={self.awaitTxt.get()}"
      self.__writeTextSummary(text)
    
    self.textInsTxt.delete(0, "end")
    self.awaitTxt.delete(0, "end")
  
  def __writeTextSummary(self, text):
    self.summaryTxt.config(state="normal")
    self.summaryTxt.delete("1.0", "end-1c")
    self.summaryTxt.insert("end-1c", text)
    self.summaryTxt.config(state="disabled")
  
  def clickEvent(self):
    self.clickWindow = Toplevel()
    self.clickWindow.wm_attributes("-alpha", 0.7)
    self.clickWindow.wm_attributes("-fullscreen", True)
    self.clickWindow.bind("<Button>", self.handleClick)
  
  def handleClick(self, event):
    text = self.summaryTxt.get("1.0", "end-1c")
    text += f"\nclick={event.x}, {event.y}"
    self.__writeTextSummary(text)

    if self.awaitTxt.get() != "":
      text = self.summaryTxt.get("1.0", "end-1c")
      text += f"\nawait={self.awaitTxt.get()}"
      self.__writeTextSummary(text)
    
    self.awaitTxt.delete(0, "end")
    self.clickWindow.destroy()

  def saveInsFile(self):
    if self.fileNameTxt.get() == "":
      return

    saveInstructions(
      self.fileNameTxt.get(),
      self.summaryTxt.get("1.0", "end-1c")
    )