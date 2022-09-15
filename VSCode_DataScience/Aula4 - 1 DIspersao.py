import plotly.express as px 
import numpy as np  
    
np.random.seed(42)  
    
df = px.data.iris() 
  
fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                 color="species") 
fig.show()

#fig = px.scatter(df, x="sepal_width", y="sepal_length", 
#                 color="species", size='petal_length',  
#                 hover_data=['petal_width']) 
#fig.show()