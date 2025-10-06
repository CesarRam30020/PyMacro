from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()

setup(
  name="PyMacro",
  version="1.0.0",
  author="César Ramírez",
  author_email="cesar.ram.30020@gmail.com",
  description="Aplicación para crear y ejecutar macros de teclado y mouse para automatizar tareas repetitivas.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/CesarRam30020/PyMacro",
  packages=find_packages(include=["scripts", "scripts.*"]),
  include_package_data=True,
  package_data={
    "": ["*.ins"],  # incluye archivos .ins en cualquier subcarpeta
  },
  install_requires=[
    "pyautogui>=0.9.54",
    "pynput>=1.7.6",
    # agrega dependencias si usas tkinter, customtkinter, etc.
  ],
  python_requires=">=3.9",
  entry_points={
    "console_scripts": [
      # permite ejecutar 'pymacro' desde la terminal
      "pymacro=scripts.main:main",
    ],
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Utilities",
    "Intended Audience :: End Users/Desktop",
    "Development Status :: 4 - Beta",
  ],
  keywords="automation macros keyboard mouse tkinter gui",
)
