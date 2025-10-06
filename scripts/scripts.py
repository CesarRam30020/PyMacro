from os import listdir
from pyautogui import moveTo, move, click, write, press

BASE_PATH = "instructions/"

def getInstructionFiles():
  return [_ for _ in listdir(BASE_PATH) if _[-4:] == ".ins"]

def deleteInstructionFile(file):
  try:
    import os
    os.remove(f"{BASE_PATH}{file}")
    return True
  except Exception as e:
    print(f"Error deleting file: {e}")
    return False

def runInstructions(file: str):
  if file == "None":
    raise ValueError("No instruction file provided")

  
  with open(f"{BASE_PATH}{file}", "r") as file:
    instructions = file.readlines()

    for instruction in instructions:
      match instruction.split(":"):
        case ["move", params]:
          move(*map(int, params.split(",")))

        case ["moveTo", params]:
          moveTo(*map(int, params.split(",")))

        case ["click", params]:
          click(*map(int, params.split(",")))

        case ["write", params]:
          write(params.strip())

        case ["press", params]:
          press(params.strip())

        case _:
          print("Unknown instruction")

  return True