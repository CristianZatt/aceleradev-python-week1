import unittest
from calculator import *

class calculator(unittest.TestCase):

    def test_50Calls(self):
        calls = 50
        funcPerCall = 2
        funcExecTime = 3

        callReceiveVal = 1
        funcExecVal = 0.2  #20
        funcExecTimeVal = 0.3 #90   = 101

        expected = 101

        result = calc(
            calls = 50,
            funcPerCall = 2,
            funcExecTime = 3,
            callReceiveVal = 1,
            funcExecVal = 0.2,
            funcExecTimeVal = 0.3
        )

        self.assertEquals(expected, result)

unittest.main()