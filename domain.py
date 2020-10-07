import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)import nltk
from django.contrib import admin
from django.urls import path
from twitterapp import views
from django.conf.urls import url  
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home', views.homeview),
    url(r'^username', views.usernamereq),
    url(r'^tweets', views.tweets), 
    url(r'^friendtweets', views.friendstweet),       
]
