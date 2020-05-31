from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

for tag  in  y_kmeans.labels_ :
    if tag==1:
      tags1=element+" "+element[tag]
    if tag==2:
      tags2=element+" "+element[tag]
    if tag==3:
      tags3=element+" "+element[tag]

wordcloud = WordCloud(width = 1000, height = 1000, 
            background_color ='white', 
            min_font_size = 14).generate(tag1) 

plt.figure(figsize = (10, 10), facecolor = None) 
plt.imshow(wordcloud) 
