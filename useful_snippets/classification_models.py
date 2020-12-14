from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,roc_auc_score



def show_performance(model,X_train=X_res,y_train=y_res,X_test=X_test,y_test=y_test,roc=False):
    model.fit(X_train,y_train)
    print('Training accuracy - ',accuracy_score(model.predict(X_train),y_train))
    print('Validation accuracy - ',accuracy_score(model.predict(X_test),y_test))
    
    if roc:
        print('')
        print('Training ROC - ',roc_auc_score(y_train,model.predict_proba(X_train)[:,1]))
        print('Test ROC - ',roc_auc_score(y_test,model.predict_proba(X_test)[:,1]))
        

def run_classification_models(X_train,y_train,X_test,y_test,roc=True):
    models = [LogisticRegression(), RandomForestClassifier(),XGBClassifier()]
    model_names = ['Logistic Regression','Random Forest','XGBclassifier']
    
    for i in range(len(models)):
        print('-------------------------------------------')
        print('For ',model_names[i],' -')
        print('')
        show_performance(models[i],X_train,y_train,X_test,y_test,roc)
        print('-------------------------------------------')
