from os import listdir

# Local imports
from brain import Brain
from dirpath import DATAPATH

class ColorDream():
    def __init__(self):
        self.brain = Brain()

    def train(self):
        for filename in listdir(DATAPATH):
            if filename[-4:] == '.txt':
                self.brain.add_palette(DATAPATH + "/" + filename)

        self.brain.train()

    def test(self, palette):
        return self.brain.classify(palette)
