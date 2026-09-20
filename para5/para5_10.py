import inspect
import sys
import matplotlib


for x in dir(matplotlib):
    print(x)

print(inspect.ismodule(matplotlib))

for module_name, module_pass in sys.modules.items():
    print(module_name, module_pass)

XQL = matplotlib

for metod in dir(XQL):
    print(metod)