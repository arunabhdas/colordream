#!/usr/bin/env python
import os
import sys
from sys import argv
import pickle

# PyBrain imports
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain import TanhLayer

# Local Imports
from dirpath import DATAPATH
import datamanip

class Brain:
  def __init__(self, hidden_nodes = 30):
    """
    parameters to buildNetwork are inputs, hidden layers, output
    bias = true allows for a bias unit to be added in each neural net layer
    hiddenclass represents the method used by the hidden layer
    """
    self.classifier_neural_net = buildNetwork(8, hidden_nodes, 12, bias=True, hiddenclass=TanhLayer)

    # Initializing dataset for supervised regression training
    self.data_sets = SupervisedDataSet(8, 12)

    # classification_trainer uses backpropagation supervised training method
    self.classification_trainer = BackpropTrainer(self.classifier_neural_net, self.data_sets)

  def add_palette(self, filepath):
    palette = datamanip.get_palette(filepath)
    print palette
    self.data_sets.addSample(
        (
            palette[0][0], palette[0][1], palette[0][2], palette[0][3],
            palette[1][0], palette[1][1], palette[1][2], palette[1][3]
        ),
        (
            palette[2][0], palette[2][1], palette[2][2], palette[2][3],
            palette[3][0], palette[3][1], palette[3][2], palette[3][3],
            palette[4][0], palette[4][1], palette[4][2], palette[4][3],
        )
    )

  def train(self):
    # print("Not Converging...This will not take long, but will be less accurate")
    # for i in range(0, 30):
    #   self.classification_trainer.train()

    print("Converging...This is going to take long!")
    self.classification_trainer.trainUntilConvergence()

  def classify(self, palette):
    return self.classifier_neural_net.activate(
        palette[0][0], palette[0][1], palette[0][2], palette[0][3],
        palette[1][0], palette[1][1], palette[1][2], palette[1][3]
    )
