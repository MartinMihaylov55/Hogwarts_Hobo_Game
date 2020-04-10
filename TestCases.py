from analysis import Hobo
from analysis import Analyze
from analysis import RailTrack
from analysis import Train
from analysis import Tunnel
# Interpreter complains if from analysis import * used
import unittest

class Test(unittest.TestCase):

    def testhobo(self):
        hoboInstance = Hobo

    def testanalyze(self):
        analyzeInstance = Analyze

    def testrailtrack(self):
        railtrackInstance = RailTrack

    def traintest(self):
        trainInstance = Train

    def tunnelTest(self):
        tunnelInstance = Tunnel
