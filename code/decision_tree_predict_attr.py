from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def dec_testset():
    with open("../data/data_doc/data_doc.txt",'rb') as fp:
          data= pd.read_table("data_doc1.txt",header=None)
          fp=data[0].str.split()
          for line in fp:
            X.append(list(map(float, line[:-1])))
            Y.append(line[-1])
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    X = np.array(X, dtype = np.float32)
    Y = np.array(Y, dtype = np.float32)
    train_X,test_X, train_y, test_y = train_test_split(X,Y,test_size=0.2)
    model = tree.DecisionTreeClassifier(criterion='gini')       # gini impurity
    model = tree.DecisionTreeClassifier(criterion='entropy')    # information gain
    model.fit(train_X, train_y)
    expected = test_y
    predicted = model.predict(test_X)
    label = list(set(Y))
    return model
def pred(model,predict_dat):
    model.predict(predict_dat)
    return True

    
if __name__ == '__main__':
    model = dec_testset()
    pred(model,predict_dat)

