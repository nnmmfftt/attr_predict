import cluster
import distance
import plot
import sys
import pandas as pd
import numpy
import sys
import distance_build_origin

filename_all = sys.argv[1]
filename_add = sys.argv[2]
#convert attr to str from file
def get_new_policy_to_str(filename):
    new_attr = ''
    with open(filename, 'r') as f:  
        lines = f.readlines() 
        last_line = lines[-1]  
    return last_line

#to get attr from origin txt/csv
def get_ex_attr_list(filename):
    vec =[]
    with open(filename,'rb') as fp:
      data= pd.read_table(filename,header=None)
      fp=data[0].str.split()
      for line in fp:
        vec.append(list(map(float, line[:-1])))
    vec = np.array(self.vectors, dtype = np.float32)
    return vec

#compute count of new attr -1,means sum of exist attr
def get_attr_num(filename):
    last_line = get_new_policy_to_str(filename)
    return int(last_line[0])


def get_num_of_attr(filename):
    pass

#convert new attr to 2D vector(float)
def get_new_attr_to_vec(filename):
    vec = []
    str_attr = ''
    str_attr = get_new_policy_to_str(filename)
    vec=list(map(float,str_attr))
    return vec
    


def min_distance_compute(filename,vec):
    vec_dis = get_ex_attr_list(filename)
    last_num = get_attr_num(filename)
 #  for i in range(key_1,key_1 + len(vec_dis) - 1):
    min_j,min_dis = 0,0x7FFFFFFF
    for j in range(0, last_num+1):
        if distance_obj.distance(vec, vec_dis[j]) < min_dis :
            min_dis= distance_obj.distance(vec, vec_dis[j])
            min_j = j
    return min_dis,min_j



def get_res(filename,j):
  if j < 1:
    return False
  for cur_line_number, line in enumerate(open(filename, 'rU')):
    if cur_line_number == j-1:
      return line[-1]
  return False

def write_new_policy_to_file(filename,str_new_attr,res):
    rc = 0
    fp = open(filename,'a+')
    rc = fp.write(str_new_attr+' '+str(res))
    if rc < 1 :return False 
    else: return True


def write_dis_to_file(filename):
    fo = open(filename, 'w')
    for j in range(0, last_num+1):
        fo.write(str(last_num + 1) + ' ' + str(j + 1) + ' ' + str(distance_obj.distance(vec_newattr, vec_dis[j])) + '\n')



#def add_policy_for_file(filename,str_policy_list):
#    with open(filename, "a+") as f: 
#        f.write(str_policy_list)







if __name__ == '__main__' ():
    vec = get_new_attr_to_vec(filename_new)
    min_dis,min_j = min_distance_compute(filename_all,vec)
    print(get_res(filename_all,min_j))
    write_new_policy_to_file(filename_all,vec )
    write_dis_to_file(filename_all)
    print("Update done")