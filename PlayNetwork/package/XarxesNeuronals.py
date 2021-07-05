from package.KeyBoardInput import KeyBoardInput
import pickle

class XarxesNetwork(object):

    def __init__(self, net):
        self.xarxa = net

    def getXarxaActual(self):
        """Get xarxa."""
        return self.xarxa

    @staticmethod
    def loadNet(file):
        with open(file, 'rb') as input:
            net = pickle.load(input)
            return net





