#! /usr/bin/env python
#-*- coding: utf-8 -*-

from distance import *

import numpy as np
import pandas as pd

class DistanceBuilder(object):

  """
  Build distance file for cluster
  """  

  def __init__(self):
    self.vectors = []

  def load_points(self, filename):
    '''
    Load all points from file(x dimension vectors)

    Args:
        filename : file's name that contains all points. Format is a vector one line, each dimension value split by blank space
    '''
    #fp=pd.read_table(filename)
    with open(filename,'rb') as fp:
      data= pd.read_table(filename,header=None)
      fp=data[0].str.split()
      for line in fp:
        self.vectors.append(list(map(float, line[:-1])))
        #self.vectors.append(np.array(map(float, line.split('\t')[:-1]), dtype = np.float32))
    self.vectors = np.array(self.vectors, dtype = np.float32)


  def build_distance_file_for_cluster(self, distance_obj, filename):
    '''
    Save distance and index into file

    Args:
        distance_obj : distance.Distance object for compute the distance of two point
        filename     : file to save the result for cluster
    '''
    fo = open(filename, 'w')
    for i in range(len(self.vectors) - 1):
      for j in range(i, len(self.vectors)):

        fo.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(distance_obj.distance(self.vectors[i], self.vectors[j])) + '\n')
    fo.close()
#end DistanceBuilder
