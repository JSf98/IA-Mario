import os

class FileWritter(object):

    def __init__(self, path):
        self.file = open(path, "w", encoding='utf8')

    def writeString(self, string):
        self.file.write(string)

    def writeLine(self, string):
        self.file.write(string + os.linesep)

    def close(self):
        self.file.close()