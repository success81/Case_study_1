import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'archive/USvideos.csv')
plt.style.use('ggplot')
fig, ax = plt.subplots(2,2)

# Column of interest
ClnData = data[['title', 'tags', 'views', 'likes', 'dislikes']]

# establish sad list
rem_chars = ["!",'\"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","}","~","–","|"]
rep_chars = ['' for i in range(len(rem_chars)-1)]
rep_chars.append(' ')

# Cleaned Title
ClnData['title'] = ClnData['title'].str.lower()
ClnData['title'] = ClnData['title'].str.replace(pat='[^a-z| ]', repl='', regex=True)
ClnData['title'] = ClnData['title'].str.replace(pat='|', repl=' ', regex=True)
# Cleaned the tags
ClnData['tags'] = ClnData['tags'].str.lower()
ClnData['tags'] = ClnData['tags'].str.replace(pat='[^a-z| ]', repl='', regex=True)
ClnData['tags'] = ClnData['tags'].str.replace(pat='|', repl=' ')

ClnData['title length'] = ClnData['title'].str.split().str.len()
ClnData['tag length'] = ClnData['tags'].str.split().str.len()

def title_alliterates(title):
  if " " not in list(title):
    return False
  compare_let = list(title)[0]
  word_list = title.split(" ")
  word_list.pop(0)
  for word in word_list:
    try:
      if list(word)[0] == compare_let:
        return True
    except IndexError:
        return False
  return False

alliterates = []
for title in ClnData['title']:
  if title_alliterates(title):
    alliterates.append('True')
  else:
    alliterates.append('False')

ClnData['alliterates'] = pd.array(alliterates)

print(ClnData.groupby('alliterates')['views'].mean())


ax[0,0].set_title("Active Interation: Title Length")
ax[0,1].set_title("Active Interation: Tag Length")
ax[1,0].set_title("Passive Interation: Title Length")
ax[1,1].set_title("Passive Interation: Tag Length")
ax[0,0].set_xlabel("Title Length(word)")
ax[0,1].set_xlabel("Tag Length(word)")
ax[1,0].set_xlabel("Title Length(word)")
ax[1,1].set_xlabel("Tag Length(word)")
ax[0,0].set_ylabel("Likes")
ax[0,1].set_ylabel("Likes")
ax[1,0].set_ylabel("Views")
ax[1,1].set_ylabel("Views")
ax[0,0].bar(ClnData['title length'],ClnData['likes'])
ax[0,1].bar(ClnData['tag length'],ClnData['likes'])
ax[1,0].bar(ClnData['title length'],ClnData['views'])
ax[1,1].bar(ClnData['tag length'],ClnData['views'])

ax = ax.flatten()
fig.tight_layout()
plt.show()


'''
tag vs title

arr tag - arra title

count vs count
title vs tag
number of tags vs veiw count
if word == a tag in the title
'str'

bar graph?
word count vs veiw count
United States
'''
