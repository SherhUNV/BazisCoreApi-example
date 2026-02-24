import sys
import os
from pythonnet import load

load("coreclr")
import clr

# Add the directory containing your DLL to the system path
dll_Dir = r"D:\source\repos\BazisCoreApi-example\TestLib\bin\Debug\net8.0"
sys.path.append(dll_Dir)

# Add a reference to the assembly (use the name of the DLL without the extension)
clr.AddReference("TestLib")

# Import the specific namespace and class
from TestLib import Class1

# Create an instance of the class and use its methods
instance = Class1()
result = instance.SetField("Hello_World!!1")
print(f"The result is: {instance.GetField()}")
print(f"The result is: {instance.GetDoubleFiled()}")
print(f"The result is: {instance.GetSqrt(25)}")
print(f"The result is: {instance.GetDoubleSum(10)}")
