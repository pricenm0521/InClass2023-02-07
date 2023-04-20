# main.py
#    package name.module name
from demoPackage.demo import *
demo() # call the function in demo.py ie entry point
from demoPackage.demo01 import *
demo01({"key1":"value1", "key2":"value2"})
demo01(None)
demo01({})
