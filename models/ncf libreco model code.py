#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
from libreco.data import random_split, DatasetPure
from libreco.algorithms import NCF  # pure data, 
from libreco.evaluation import evaluate


# In[15]:


train_data = pd.read_csv('ml-dataset/train_rating.csv')
test_data = pd.read_csv('ml-dataset/test_rating.csv')


# In[16]:


train_data.drop(columns=['ratingId', 'title'],axis=1, inplace=True)
test_data.drop(columns=['ratingId', 'title'], axis=1, inplace=True)


# In[17]:


column_name = train_data.columns[-1]
column_data = train_data.pop(column_name)

train_data.insert(1, column_name, column_data)


# In[18]:


column_name = test_data.columns[-1]
column_data = test_data.pop(column_name)

test_data.insert(1, column_name, column_data)


# In[19]:


train_data


# In[20]:


test_data


# In[21]:


train_data.columns = ["user", "item", "label", "time"]
test_data.columns = ["user", "item", "label", "time"]


# In[22]:


eval_data, test_data = random_split(test_data, multi_ratios=[0.2, 0.8])


# In[23]:


train_data, data_info= DatasetPure.build_trainset(train_data)
eval_data = DatasetPure.build_evalset(eval_data)
test_data = DatasetPure.build_testset(test_data)


# In[24]:


import tensorflow.compat.v1 as tf

# Clear default graph
tf.reset_default_graph()

# Define variable scope with reuse=tf.AUTO_REUSE
with tf.variable_scope("embedding", reuse=tf.AUTO_REUSE):
    # Initialize NCF model
    ncf = NCF(
        task="rating",
        data_info=data_info,
        loss_type="cross_entropy",
        embed_size=16,
        n_epochs=10,
        lr=1e-3,
        batch_size=8192,
        num_neg=1,
        use_bn=False
    )

# Fit the model
ncf.fit(
    train_data,
    neg_sampling=False,
    verbose=2,
    eval_data=eval_data,
    metrics=["loss"],
)


# In[25]:


# do final evaluation on test data
evaluate(
    model=ncf,
    data=test_data,
    neg_sampling=False,
    metrics=["loss"],
)


# In[34]:


# predict preference of user 5755 to item 110
ncf.predict(user=162523, item=4150)


# In[35]:


# recommend 10items for user 5755
ncf.recommend_user(user=162523, n_rec=10)


# In[37]:


movie = pd.read_csv('ml-dataset/train_rating.csv')


# In[39]:


movie = movie[['movieId','title']]


# In[40]:


movie.drop_duplicates(inplace=True)


# In[44]:


id_movie_map = {}
for id, title in zip(movie['movieId'],movie['title']):
    id_movie_map[id] = title


# In[51]:


# recommend 10items for user 5755
recomm = ncf.recommend_user(user=162523, n_rec=10)[162523]


# In[52]:


recomm


# In[53]:


for i in recomm:
    print(id_movie_map[i])


# In[ ]:




