import pytest
import os
import sys

real_path = os.path.realpath(__file__)
current_directory = os.path.dirname(real_path)
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory+"/source")

#import aliens
# I can't test aliens because for iniatialize him
# we need to open a pygame screen
