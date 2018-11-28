#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cluster
import distance
import plot
# import plot_utils
import step1_choose_center
import step2_cluster
import sys


filename_all = sys.argv[1]
filename_add = sys.argv[2]

def append_policy(filename_all,filename_add):

    with open(filename_add, 'r') as f:  
        lines = f.readlines() 
        last_line = lines[-1]   

    with open(filename_all, "a+") as fs: 
        fs.write(last_line)

if __name__ == '__main__':

    append_policy(filename_all,filename_add)
    # distance builder
    builder = DistanceBuilder()
    builder.load_points(r'../data/data_doc/data_doc2.txt')
    builder.build_distance_file_for_cluster(SqrtDistance(), r'../data/data_doc/data_doc.dat')
    #choose cluster center & plot
    plot('../data/data_doc/data_doc.dat')
    #cluster
    plot2('../data/data_doc/data_doc.dat', 20, 0.1,False)
