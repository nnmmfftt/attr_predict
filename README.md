# DensityPeakClusering

A cluster framework for 'Clustering by fast search and find of density peaks' in science 2014.
### Density_peak_for_attr
Forked the DensityPeakCluster from [jasonwbw](https://github.com/jasonwbw/DensityPeakCluster)


ADD : Sub/Objs' attr context clustering.

# Decision tree for attr predict
Use same dataset from density_peak_for_attr.

                 precision  recall   f1-score    support

        deny       0.97      0.89      0.93        66
        permit     0.63      0.86      0.73        14

avg / total       0.91      0.89      0.89        80

## How to Use
### Density peak for attr
  0. python distance_builder_data_doc.py(Patient data set has privacy information, please send me email if you need if for research)
  1. python step1_choose_center.py
  2. python step2_cluster.py
### Decision tree for attr
  0. use decision_tree_predict_attr.py
 
## Dependencies
NumPy Matplotlib Scikit-Learn
## Reference
Clustering by fast search and find of density peaks
## License
The MIT License (MIT)
