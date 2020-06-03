import sys
import os
from cx_Freeze import setup, Executable

#Set Path for TCL_Library and TK_LIBRARY
os.environ['TCL_LIBRARY'] = "C:\\Users\\Neeraj Chekutty\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Neeraj Chekutty\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6"

#Run the setup method from the cx_Freeze module
setup(  name = "Space_Invaders",
        version = "0.1",
        description = "Space Invaders",
        options = {"build_exe": build_exe_options},
        executables = [Executable("invaders_space.py", base=base)])

