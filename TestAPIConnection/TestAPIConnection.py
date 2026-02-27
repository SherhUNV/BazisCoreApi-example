from BazisCoreAPI import core
from BazisCoreAPI import APIClass


instance = APIClass()
instance.Set_field('Hello_World!!1')


print(f"The result is: {instance.Get_field()}")
print(f"The result is: {instance.Get_double_field()}")
print(f"The result is: {instance.Get_SQRT(25)}")
print(f"The result is: {instance.Get_double(10)}")
