#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
import matplotlib.pyplot as plt

def plot_scatter_diagram(which_fig, x, y, x_label = 'x', y_label = 'y', title = 'title', style_list = []):
	'''
	Plot scatter diagram

	Args:
		which_fig  : which sub plot
		x          : x array
		y          : y array
		x_label    : label of x pixel
		y_label    : label of y pixel
		title      : title of the plot
	'''
	styles = ['k', 'g', 'r', 'c', 'm', 'y', 'b', '#9400D3','#C0FF3E']
	assert len(x) == len(y)
	print(style_list)
	if len(style_list) != 0:
		assert len(x) == len(style_list) and len(styles) >= len(set(style_list))
	plt.figure(which_fig)
	plt.clf()
	if len(style_list) == 0:
		print(1)
		plt.scatter(x, y, color=styles[0])
	else:
		clses = set(style_list)
		xs, ys = {}, {}
		for i in range(len(x)):
			try:
				xs[style_list[i]].append(x[i])
				ys[style_list[i]].append(y[i])
			except KeyError:
				xs[style_list[i]] = [x[i]]
				ys[style_list[i]] = [y[i]]
		added = 1
		for idx, cls in enumerate(clses):
			if cls == -1:
				style = styles[0]
				added = 0
			else:
				style = styles[idx + added]
			plt.scatter(xs[cls], ys[cls], color=style)
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.show()

