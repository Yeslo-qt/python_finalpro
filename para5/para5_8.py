import sys

for module_name, module_pass in sys.modules.items():
    print(module_name, module_pass)