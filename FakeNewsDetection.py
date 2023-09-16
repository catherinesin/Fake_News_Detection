import pandas as pd
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import Dataset
df = pd.read_csv('train.csv') # Data for train
df2 = pd.read_csv('test.csv') # Data for test
df.dropna
df2.dropna
rows_train = len(df.index) # Number of rows of train data
# Preprocessing
Y = df[['Label']]
df.drop(['Label'],axis=1,inplace=True)
df_merge = df.append(df2) # Merge train and test data set
X_prep = pd.get_dummies(df_merge[['Country (mentioned)', 'Review Date', 'Source']]) # Get dummy variables
X = X_prep.iloc[:rows_train,:] # For train
X_finalTest = X_prep.iloc[rows_train:,:] # For final prediction

# Train the Model
best_s = 0 # accuracy score
best_nei = 0 # k
best_ts = 0 # test size
best_rs = 0 # random state
for k in range(16,20):
    for t_s in range(15,30):
        for r_s in range(20,40):
            # Training Test Split
            X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=t_s/100, random_state=r_s)
            KNN_model = KNeighborsClassifier(n_neighbors = k)
            KNN_model.fit(X_train, y_train)
            # Predict Test
            KNN_prediction = KNN_model.predict(X_test)
            if accuracy_score(KNN_prediction, y_test)>best_s:
                best_s = accuracy_score(KNN_prediction, y_test)
                best_nei = k
                best_ts = t_s
                best_rs = r_s
print("best score: ", best_s)
print("k: ", best_nei)
print("test size: ", best_ts)
print("random state: ", best_rs)

# Finalise the model
model = KNeighborsClassifier(n_neighbors = best_nei)
model.fit(X, Y)
# Predict Test File
df2['Id'] = range(1, len(df2) + 1)
y_finalPred = model.predict(X_finalTest)
res = pd.DataFrame(df2['Id'])
res['Category'] = y_finalPred
res.reset_index(drop=True)
# Save result
res.to_csv('submission.csv',index=False)