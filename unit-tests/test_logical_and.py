# Python code to test Intrepydd's logical_and function by calling func_logical_and.func()
# Author: Sriraj (sriraj@gatech.edu)

import numpy as np;

# Copy of Intrepydd code from func_logical_and.pydd, adapted to Python
def python_logical_and(A, B):
    C = np.logical_and(A, B)
    return C

# Called by pytest tool, which automatically calls all test_* functions in test_*.py files in this directory
def test_logical_and():
    import subprocess
    subprocess.run(["../intrepydd/pyddc", "func_logical_and.pydd"])  # Compile func_logical_and.pydd
    import func_logical_and
    # Check that Intrepydd & Python implementations of logical_and behave the same
    # Not all test cases will have an equivalent python_* function to compare with
    A = True
    B = np.array([[3.4, 0, 7.8],[9.0, -1.2, 3.4]])
    C = np.array([[3, 1, 7],[9, 0, 3]])
    assert (func_logical_and.func1(A, B.astype('float64')) == python_logical_and(A, B)).all()
    assert (func_logical_and.func1(A, B) == python_logical_and(A, B)).all()
    assert (func_logical_and.func2(C, A) == python_logical_and(C, A)).all()
    assert (func_logical_and.func3(C, B) == python_logical_and(C, B)).all()

