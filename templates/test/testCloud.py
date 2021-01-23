import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

conn = sqlite3.connect('/Users/yuxuan/coding/douban/movie.db')
cur = conn.cursor()
sql = 'select introduction from movie250'
text = ''
data = cur.execute(sql)
for item in data:
    text = text + item[0]
    # print(item[0])
cur.close()
conn.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open('/Users/yuxuan/coding/douban/templates/test/tree.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path=r'/System/Library/Fonts/Hiragino Sans GB.ttc'
)
wc.generate_from_text(string)

# plot the figure
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # do not show the axis
plt.savefig('./word.jpg',dpi=500)
# plt.show()
