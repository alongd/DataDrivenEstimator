#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import unittest
import cnn_framework
from cnn_framework.predictor import Predictor
from cnn_framework.input import read_input_file
from cnn_framework.layers import MoleculeConv
from keras.layers.core import Dense


class TestInput(unittest.TestCase):

    def test_read_input_file(self):

        predictor_test = Predictor()

        path = os.path.join(os.path.dirname(cnn_framework.__file__),
                            'test_data',
                            'minimal_predictor',
                            'predictor_input.py')
        read_input_file(path, predictor_test)

        predictor_model = predictor_test.model
        self.assertEqual(len(predictor_model.layers), 4)
        self.assertTrue(isinstance(predictor_model.layers[1], MoleculeConv))
        self.assertTrue(isinstance(predictor_model.layers[2], Dense))

        self.assertEqual(predictor_model.layers[1].inner_dim, 38)
        self.assertEqual(predictor_model.layers[1].units, 512)
