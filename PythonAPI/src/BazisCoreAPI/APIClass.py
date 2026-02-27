from BazisCoreAPI import core
from TestLib import Class1


class APIClass:
    def __init__(self):
        self.csClassInstance = Class1()


    def Set_field(self, string):
        self.csClassInstance.SetField(string)


    def Get_field(self):
        return self.csClassInstance.GetField()


    def Get_double_field(self):
        return self.csClassInstance.GetDoubleFiled()


    def Get_SQRT(self, num):
        return self.csClassInstance.GetSqrt(num)


    def Get_double(self, num):
        return self.csClassInstance.GetDoubleSum(num)
