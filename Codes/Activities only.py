import scipy.io
import os
import numpy as np
import pandas as pd
import statsmodels
from statsmodels.tsa.api import VAR
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import scikitplot as skplt 
from sklearn import metrics
from sklearn.metrics import f1_score 
import statistics 


'''reading files'''
path = "//"

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.mat' in file:
            files.append((os.path.join(r,file)))

###############################################
            
featVect = []
y1_train = []
order_ = 3

def processFile(matfile,order):
        
        file = scipy.io.loadmat(matfile)
        new = (file['data1'])[:,[10,11,12,13,14,15,26,27,28,29,30,31]] #file is a dictionary. The actual data is the value of the 'data1' key , Indexing refers to Left/Right hand Acceleration and angular velocity
                
        ''' to have each file trained '''
        featVect.append(new)

        # ''' to use VAR '''
        # tempVect = []
        # model = VAR(new,None)
        # results = model.fit(order) #5 order
        # #return list(results.coefs.ravel())
        # tempVect.extend(list(results.params.ravel())) #coeffs
        # tempVect.extend(list(results.sigma_u.ravel())) #noise covariance
        # featVect.append(tempVect)

#
def get_data():    
    for file in files:
        if 'run' in file:
            #print('m run')
            processFile(file,order_)
            y1_train.append('run')
               
        elif 'wal' in file:
           #print('m walk')                
           processFile(file,order_)
           y1_train.append('wlk')
           
        elif 'bye' in file:
            #print('m bye')                
            processFile(file,order_)
            y1_train.append('bye')       
       
        elif 'cla' in file:
           #print('m clapping')                
           processFile(file,order_)
           y1_train.append('clap')    
                     
 
get_data()

# =============================================================================


n_featVect= np.array(featVect)
xy=n_featVect.shape[1]

# ACF

lag = range(1,15)
feature= np.empty(shape= [len(n_featVect), n_featVect.shape[1]*len(lag)])
for i, sample in enumerate(n_featVect): #i in range(number of matrices) , sample is matrix itself
    for j, lags in enumerate(lag):
        for k in range (sample.shape[1]): #Sample's features coulumns
            feature[i,j*xy+k] = pd.DataFrame(sample)[k].autocorr(lag=lags)
X_test= np.array(featVect).reshape(-1, 1)    
# =============================================================================

# Generates TP, TN, FP, FN from the data to calculates specitivty

def spevsv_measure(conf):
    FP = conf.sum(axis=0) - np.diag(confusion_matrix)  
    FN = conf.sum(axis=1) - np.diag(confusion_matrix)
    TP = np.diag(conf)
    TN = conf.values.sum() - (FP + FN + TP)
    specitivty = TN / (TN+FP)
    return specitivty

#Create a Gaussian Classifier
clf = RandomForestClassifier(n_estimators=500,n_jobs=-1) #n_jobs = -1 lets you use all the cores to speed things up
x=feature
y=np.array(y1_train)
accuracy_mean=[]
percesion_mean =[]
f_score_mean=[]
specitivity_mean=[]
recall_mean=[]
Y_T=np.array([])
Y_P=np.array([])

for i in range(10):

    #Train the model using the training sets y_pred=clf.predict(X_test)
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=.30) # 70% training and 30% test
    
    clf.fit(X_train,Y_train)
    
    Y_pred=clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    #print('acc=', np.mean(Y_pred == Y_test) * 100)
    
    accuracy_mean.append(metrics.accuracy_score(Y_test, Y_pred))
    percesion_mean.append(metrics.precision_score(Y_test, Y_pred,average='weighted'))
    recall_mean.append(metrics.recall_score(Y_test, Y_pred,average='weighted'))
    conf=metrics.confusion_matrix(Y_test, Y_pred)
    # specitivity_mean.append(spevsv_measure(conf))
    f_score_mean.append(f1_score(Y_test, Y_pred,average='weighted'))
    Y_T=np.append(Y_T,Y_test, 0)
    Y_P=np.append(Y_P,Y_pred, 0)


#########################################################
  
#confusion matrix as numbers
skplt.metrics.plot_confusion_matrix(Y_T, Y_P, normalize=False)
#confusion matrix as heat fusion
skplt.metrics.plot_confusion_matrix(Y_T, Y_P, normalize=True)
print("accuracy mean: ", statistics.mean(accuracy_mean) )
print("percecsion mean: ", statistics.mean(percesion_mean) )
print("recall mean: ", statistics.mean(recall_mean) )
# print("specitivity mean: ", statistics.mean(specitivity_mean) )
print("f_score mean: ", statistics.mean(f_score_mean) )



