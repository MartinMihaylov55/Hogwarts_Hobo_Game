from analysis import Hobo
from analysis import RailTrack
from analysis import Train
from analysis import Tunnel
# Interpreter complains if from analysis import * used
import unittest

class Test(unittest.TestCase):

    def testhobo(self):
        hoboInstance = Hobo.Hobo("parameter")

    def testrailtrack(self):
        railtrackInstance = RailTrack.RailTrack("parameter")

    def traintest(self):
        trainInstance = Train.Train("Parameter", "track")

    def tunnelTest(self):
        tunnelInstance = Tunnel.Tunnel("parameter")
