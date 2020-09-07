
def find_roc_terms(cls,X,y):
    probs = cls.predict_proba(X)[:,1]
    fpr,tpr,_ = roc_curve(y,probs)
    auc = roc_auc_score(y,probs)
    
    return fpr,tpr,auc



def plot_roc_test(cls,X_train,y_train,X_test,y_test):
    fpr,tpr,auc = find_roc_terms(cls,X_train,y_train)
    fpr_test,tpr_test,auc_test = find_roc_terms(cls,X_test,y_test)
    
    fig,(ax1,ax2) = plt.subplots(1,2,figsize = (12,6))
    ax1.plot(fpr,tpr,label="auc="+str(auc)[0:4],c = 'r')
    ax1.plot([0,1],[0,1],alpha = 0.1,c = 'b')
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.set_title('Train Roc')
    ax1.legend()
    
    ax2.plot(fpr_test,tpr_test,label="auc="+str(auc_test)[0:4],c = 'r')
    ax2.plot([0,1],[0,1],alpha = 0.1,c = 'b')
    ax2.set_xlabel('False Positive Rate')
    ax2.set_ylabel('True Positive Rate')
    ax2.set_title('Test Roc')
    ax2.legend()
