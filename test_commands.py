# Author : Nikhil Kalra #
# CST8333 Final project#
# December 2,2018 #
from unittest import TestCase
import Commands


class TestCommands(TestCase): #Class used to run test cases by Nikhil Kalra

    def test_insertFile(self): # Method used to test new record function by Nikhil Kalra
        test = Commands.Commands.insertData("nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil"
                                            , "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil")
        self.assertEquals(test, "Pass")

    def test_updateFile(self): # Method used to test update record function by Nikhil Kalra
        test = Commands.Commands.updateData("nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil"
                                            , "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", "nikhil", 2)
        self.assertEquals(test, "Pass")

    def test_deleteFile(self): # Method used to test delete record function by Nikhil Kalra
        test = Commands.Commands.deleteData(1)
        self.assertEquals(test, "Pass")


