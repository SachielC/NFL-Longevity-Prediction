# NFL-Longevity-Prediction
## Introduction
The National Football League (NFL) Combine is an annual event in which those 
hopeful of one day playing in the NFL get an opportunity to show off their skills to teams 
ahead of the NFL Draft in hopes of getting selected. As part of the NFL Combine, the size 
of players are measured as well as other physical attributes.1 The Combine 
measurements our model takes into account are a player’s height (inches), weight 
(pounds), age (years), arm length (inches), their 40-yard dash time (seconds), vertical 
jump height (inches), bench press (pounds) and 20-yard shuttle time (seconds).
Using Combine measurement data from every player evaluated between 1987-
2019 and NFL player statistics data from all NFL players between 1987-2019, we 
predicted that over a large sample size, better NFL Combine measurements would overall 
yield more successful NFL careers. We are measuring “success” as years played in the 
league as a starter (the best player on your team at a specific position). We concluded 
that game-statistics and season awards were too dependent on the era in which the game 
was played, and that years played as a starter was most indicative of true success.

1 https://www.profootballnetwork.com/what-is-the-nfl-combine/
## Methodology
We combined our two aforementioned datasets into one large data frame 
(containing both the Combine measurements and NFL statistics, combined via a 
common player name). We then eliminated any unneeded rows deemed irrelevant for our 
purposes. For example, passing, rushing and receiving statistics were removed, as our 
model only takes years started into account for determining success. Our final data frame 
includes NFL players, their aforementioned Combine measurements and their years 
started in the NFL as well as information about the team they were drafted to, the year 
they were drafted as well as extra Combine measurables we contemplated (but ultimately 
decided against) including in our model. We decided to include the team drafted to and 
year drafted in order to make the data easier to work with—they are not factored into our 
model.

We then created a function which takes in a player from the dataset and their 
position, and trains a decision forest with 500 trees on players that share the same 
position. To test the code, we limited it to train from players who were selected to the Pro 
Bowl between 1987-2019. Generally, the top six players at each position are selected to 
participate in the Pro Bowl. By limiting the data to Pro Bowlers, the model will assume 
that any imputed player is of higher skill, which then gives a better range of the data. This 
is an issue because most players that make it to the NFL have very short-lived careers, 
and training on all player data would skew the results greatly towards smaller numbers. 
This would make the model effectively useless as it could guess zero years starting for 
every imputed player and produce high marks of accuracy. Thus, by limiting our data to 
Pro Bowlers, we got a larger and more useful subset of results which we can interpret 
more accurately. 

The model uses ‘Years Started’ as its label, and then guesses how many years the 
imputed player will be a starter. We concluded that results ranging from 1-5 indicate a 
low-end projection for this player, those who score 6-9 have a good outlook on their career 
and any players that score 10 or higher are to be considered elite prospects. This function 
was used to test our decision forest on certain players within the data set to see how well 
the model works against players where we know their years started. By excluding specific 
players from the testing data, we could test them without fear of overfitting, and when 
performing these tests, we saw a reasonable degree of accuracy. This gave us the 
confidence to move forward testing players that are not already within the data.
We then wrote a second, similar function that essentially does the same thing, 
except instead of testing on players within the data set, imputed measurement data yields 
its result. This function was tested on the two most recent Draft classes—2022 and 2023. 
Looking at the 2022 Draft class serves as interesting context for their rookie year 
performances. We tested certain players from the 2023 Draft simply as neat exercise 
given our working on this project coincided with this year’s draft.

## Results
Running the data on select top players from the 2022 Draft class gave us these 
results: the X-axis is our forest’s estimated years starting and the Y-axis is the player’s 
2022 Pro Football Focus (PFF) grade. PFF assigns player grades on a 0-100 scale. These 
grades are assigned by professional football writers and analysts based on player ingame performances.2
We excluded offensive lineman from our results, as our model consistently 
predicted 10+ years starting, regardless of Combine data. This is likely due to the fact Pro 
Bowl linemen almost always start a long time as opposed to other positions due to a 
general longevity of playing that position.
Our data displays reasonable correlation (~59%) with one major outlier being 
Derek Stingley. This, however, makes sense as Stingley suffered several injuries before 
and during the 2022 season, greatly limiting his ability to perform, thus impacting his PFF 
grade.

2 https://www.pff.com/grades

Using our model, we ran combine data on select players from the 2023 Draft as an 
exercise. The model predicts that Devon Witherspoon and Tyree Wilson will start the 
most years, and vehemently disagrees with the number one overall selection of Bryce 
Young. It makes sense that our model would dislike Bryce Young, as he is relatively short 
(5’ 10”) for a QB. However, Young is considered an outlier by most NFL scouts due to his 
raw talent and other athletic abilities. Interestingly, Will Levis, who was widely considered 
to go in the first round, slid down to the second round. This goes against the suggestion 
of our model, which projects him as a 10-year starter in the NFL. 

## Conclusion
Predicting success of NFL prospects is difficult, and our model offers an 
interesting and semi-effective way of assisting in this process. By taking in raw athletic 
Combine data and making a prediction about how many years a player will start, we found 
that the model offers decent accuracy. For our purposes, we were quite impressed—
although we both agreed we would not want our respective favorite NFL teams (Patriots 
and Jets) to rely solely on our methods.
Our model leaves room for adjusting, particularly with what data is used to make 
predictions; It may prove interesting to create a model that takes into account college 
production, which may be more or less indicative of future NFL success. Additionally, 
finding more data dating back before 1987 would presumably assist in the model’s 
accuracy, although it is important to note that different eras of football have catered to 
different skill sets.
