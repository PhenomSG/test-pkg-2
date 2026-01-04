import sys
import os
import importlib

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Dynamically import the module using the correct name
sg_package = importlib.import_module("sg_package")  # Use 'sg_package' without the hyphen

# Now you can use sg_package
from sg_package import example

# Use functions from example
example.add_one(5)

