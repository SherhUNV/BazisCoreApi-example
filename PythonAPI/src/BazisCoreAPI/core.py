import sys
import os
from pythonnet import load
from pathlib import Path


dll_folder = Path(__file__).joinpath('libs')
if dll_folder not in sys.path:
    sys.path.append(dll_folder)

load("coreclr")
import clr
clr.AddReference("TestLib")

from TestLib import Class1