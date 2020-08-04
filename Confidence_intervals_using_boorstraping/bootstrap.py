import numpy as np
import pandas as pd
from tqdm import tqdm

class Bootstrap_ci:


	def boot(self,X_data,y_data,R,test_data,model):
		predictions = []
		for i in tqdm(range(R)):
			predictions.append(self.alpha(X_data,y_data,self.get_indices(X_data,200),test_data,model))
		   
		return np.percentile(predictions,2.5,axis = 0),np.percentile(predictions,97.5,axis = 0)

	def alpha(self,X_data,y_data,index,test_data,model):
		X = X_data.loc[index]
		y = y_data.loc[index]
		
		lr = model
		lr.fit(pd.DataFrame(X),y)
		
		return lr.predict(pd.DataFrame(test_data))


	def get_indices(self,data,num_samples):
		return  np.random.choice(data.index, num_samples, replace=True)


	
