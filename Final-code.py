import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

#Importing Datasets 

df = pd.read_csv('combine.csv', sep = ',')
df2 = pd.read_csv('nfl_draft_1970-2021.csv', sep = ',')

#Merging Tables, getting rid of some unnecessary columns to make data 
more legible

df_merged = df.merge(df2,left_on = 'nameFull', right_on = 'player')
df_new = df_merged.drop(columns=['nameFirst', 'nameLast', 'playerId', 
'nflId', 'combineId', 'collegeId', 'rush_att', 'rush_yards', 
'rush_tds', 'receptions', 'rec_yards','rec_tds', 'games', 'pass_tds', 
'carAV', 'drAV', 'college_x', 'position_x'])
df_new = df_new.drop(columns=['pass_comp', 'pass_att', 'pass_yards', 
'pass_int', 'interceptions', 'dob', 'playerProfileUrl', 'age', 
'sacks', 'tackles'])
df_new = 
df_new.drop(columns=['college_y','to','player','pick','round','combin
eWonderlic'])
df_new = df_new.fillna(0)
df_new.to_csv('data.csv')

def guess_in_dataset(player, position):'
#Troubleshooting / initial testing function
 data = pd.read_csv('data.csv')
 play = data[(data['nameFull'] == player) & (data['combinePosition'] 
== position)]
 player_data = play.loc[:,['heightInches', 'combineWeight', 
'ageAtDraft', 'combineArm', 'combine40yd', 'combineVert', 
'combineBench', 'combineShuttle', 'combine60ydShuttle']]
 datas = data[(data['starter'] > 0)] 
 features1 = ['heightInches', 'combineWeight', 'ageAtDraft', 
'combineArm', 'combine40yd', 'combineVert', 'combineBench', 
'combineShuttle', 'combine60ydShuttle']
 label = 'starter'
 X = datas[features1]
 y = datas[label]
 X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=.2)
 Forest = RandomForestClassifier(n_estimators=300)
 Forest.fit(X_train, y_train)
 print(Forest.score(X_test,y_test))
 print(play.loc[:,'starter'])
 return(Forest.predict(player_data))

def guess_new(lst, position):
#Trains a dataset based off a player's position and inputs their 
measurables to guess years started 
 data = pd.read_csv('data.csv')
 player_data = pd.DataFrame(lst).T
 player_data.columns = ['heightInches', 'combineWeight', 
'ageAtDraft', 
 'combineArm', 'combine40yd', 'combineVert', 
'combineBench', 'combineShuttle']
 print(player_data.head)
 probowlersonly = data[(data['pro_bowl'] >= 1) & 
(data['combinePosition'] == position)]
 datas = probowlersonly
 features1 = ['heightInches', 'combineWeight', 'ageAtDraft', 
'combineArm', 
 'combine40yd', 'combineVert', 'combineBench', 
'combineShuttle']
 label = 'starter'
 X = datas[features1]
 y = datas[label]
 X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=.1)
 Forest2 = RandomForestClassifier(n_estimators=500)
 Forest2.fit(X_train, y_train)
 return(Forest2.predict(player_data))

#Data is :HT, WT, AGE, ARM, 40, VERTICAL, BENCH, SHUTTLE
#Two Datasets which have playerdata from 2022 and 2023

draft2023 = {
 'bryce_young' : [[70, 204, 21, 30.5, 0, 0, 0, 0], 'QB'],
 'cj_stroud' : [[75, 214, 21, 32.5, 0, 0, 0, 0], 'QB'],
 'will_anderson' : [[75, 253, 21, 33.825, 4.6, 0, 0, 0], 'DE'],
 'anthony_richardson' : [[76, 244, 20.2, 32.75, 4.43, 40.5, 0, 0], 
'QB'],
 'devon_witherspoon' : [[72, 181, 22.4, 31.25, 4.45, 0, 0, 0], 
'CB'],
 'paris_johnson_jr' : [[78, 313, 21, 36.25, 0, 0, 29, 0], 'OT'],
 'tyree_wilson' : [[78, 271, 22, 35.5, 0, 0, 23, 0], 'DE'],
 'will_levis' : [[76, 229, 23, 32, 0, 34, 0, 0], 'QB'],
 'JSN' : [[73, 196, 21, 30.5, 4.53, 35, 0, 3.93 ], "WR"]
}
draft2022 = {
 'travon_walker' : [[77, 272, 21, 35.5, 4.51, 35.5, 0, 4.32], 
'DE'],
 'aidan_hutchinson' : [[79, 260, 22, 32.125, 4.74, 36, 0, 4.15], 
'DE'],
 'derek_stingley_jr' : [[72, 190, 20, 30.75, 4.37, 0, 0, 0], 
'CB'],
 'sauce_gardner' : [[75, 190, 20, 33.5, 4.41, 0, 0, 0], 'CB'],
 'kayvon_thibodeaux' : [[76, 254, 21, 33.125, 4.58, 0, 27, 0], 
'DE'],
 'ikem_ekwonu' : [[76, 310, 21, 34, 4.93, 29, 0, 4.73], 'OT'],
 'evan_neal' : [[79.5, 337, 21, 34, 0, 0, 0, 0], 'OT'],
 'drake_london' : [[76, 219, 20, 33, 4.5, 0, 0, 0], 'WR'],
 'garret_wilson' : [[72, 183, 21, 32, 4.38, 36, 0, 4.36], 'WR'],
 'chris_olave' : [[72, 187, 21, 31, 4.39, 32, 0, 0], 'WR'],
 'jordan_davis' : [[78, 341, 22, 34, 4.78, 32, 0, 0], 'DT'],
 'kenny_pickett' : [[75, 217, 23, 31, 4.73, 33.5, 0, 4.29], 'QB'],
 'quay_walker' : [[76, 241, 21, 32.5, 4.52, 32, 0, 0], 'LB'],
 'george_karlaftis' : [[76, 266, 21, 32.5, 0, 38, 21, 4.36], 'DE']
}

#Testing each player in the above two dictionaries

for player in draft2023:
 print(player)
 print(guess_new(draft2023[player][0], draft2023[player][1]))
print('\n\n\n')
for player in draft2022:
 print(player)
 print(guess_new(draft2022[player][0], draft2022[player][1]))


"""RESULTS / VISUALIZATION SECTION,
Taken from several tests from the forest"""


#Graphs players based on X: the guess made by the algorithm and Y: 
PFF grades
pff_grades = np.array([60.3, 80.7, 49.1, 87.9, 71.9, 83.2, 82.7, 
82.5, 71.4, 75.5, 51.9, 52])
prediction = np.array([5, 12, 12, 7, 11, 8, 10, 6, 6, 7, 4, 5])
names = ['Travon Walker', 'Aidan Hutchinson', 'Derek Stingley', 
'Sauce Gardner', 'Kayvon Thibodeaux', 
 'Drake London', 'Garret Wilson', 'Chris Olave', 'Jordan 
Davis', 'Kenny Pickett',
 'Quay Walker', 'George Karlaftis']
plt.plot(prediction, pff_grades, 'o')
for i, txt in enumerate(names):
 if txt != 'Quay Walker':
 plt.annotate(txt, (prediction[i], pff_grades[i]))
 else: 
 plt.annotate(txt, (prediction[i], pff_grades[i]+2), 
arrowprops = dict(facecolor = 'black', headwidth = 1))
plt.xlabel('Estimated Years Starting')
plt.ylabel('PFF Grade 2022')
plt.show()

#Second plot without outlier and with regression line

pff_grades = np.array([60.3, 80.7, 87.9, 71.9, 83.2, 82.7, 82.5, 
71.4, 75.5, 51.9, 52])
prediction = np.array([5, 12, 7, 11, 8, 10, 6, 6, 7, 4, 5])
names = ['Travon Walker', 'Aidan Hutchinson', 'Sauce Gardner', 
'Kayvon Thibodeaux', 
 'Drake London', 'Garret Wilson', 'Chris Olave', 'Jordan 
Davis', 'Kenny Pickett',
 'Quay Walker', 'George Karlaftis']
linear_model = LinearRegression()
x = prediction.reshape(-1, 1)
y = pff_grades.reshape(-1, 1)
linear_model.fit(x, y)
y_hat = linear_model.predict(x)
plt.plot(prediction,y_hat)
plt.plot(prediction, pff_grades, 'o')
corr_coef = np.corrcoef(prediction, pff_grades)[0, 1]
plt.text(5, 90, f'Correlation: {corr_coef}')
for i, txt in enumerate(names):
 if txt != 'Quay Walker':
 plt.annotate(txt, (prediction[i], pff_grades[i]))
 else: 
 plt.annotate(txt, (prediction[i], pff_grades[i]+2), 
arrowprops = dict(facecolor = 'black', headwidth = 1))
plt.xlabel('Estimated Years Starting')
plt.ylabel('PFF Grade 2022'
