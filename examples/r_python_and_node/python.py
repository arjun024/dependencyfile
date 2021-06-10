import rpy2.robjects as robjects
from Naked.toolshed.shell import execute_js

print("Hello from python")

print("python: Calling R")
r = robjects.r
r.source('function.R')

print("python: Calling JavaScript")
execute_js('javascript.js')
