from __future__ import division
from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
from datetime import date, timedelta

yesterday = date.today() - timedelta(days = 2)
beforeyesterday = date.today() - timedelta(days = 3)
bbyesterday = date.today() - timedelta(days = 4)


url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df = pd.read_csv(url, error_bad_lines=False)
index = df.index
length = len(index)

for x in range(2,length):
	if str(df.loc[x][0]) == str(yesterday):
		if str(df.loc[x][1]) == "New Jersey":
			cases = df.loc[x][3]
			deaths = df.loc[x][4]
	elif str(df.loc[x][0]) == str(beforeyesterday):
		if str(df.loc[x][1]) == "New Jersey":
			oldcases = df.loc[x][3]
			olddeaths = df.loc[x][4]
	elif str(df.loc[x][0]) == str(bbyesterday):
		if str(df.loc[x][1]) == "New Jersey":
			beforeoldcases = df.loc[x][3]
			beforeolddeaths = df.loc[x][4]


url2 = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
dfUS = pd.read_csv(url2, error_bad_lines=False)
indexUS = dfUS.index
lengthUS = len(indexUS)

for y in range(2,lengthUS):
	if str(dfUS.loc[y][0]) == str(yesterday):
		UScases = dfUS.loc[y][1]


newcases = cases - oldcases
newdeaths = deaths - olddeaths
percent = cases/oldcases
if percent < 1:
	incdec = "increase"
	percent = round(1-percent,2)
else:
	percent = round(percent-1,2)
	incdec = "decrease"


img = Image.new('RGB', (1080,1350), color = "white")
draw = ImageDraw.Draw(img)

fnt = ImageFont.truetype('/Library/Fonts/Arial Rounded Bold.ttf', 120)
fnt2 = ImageFont.truetype('/Library/Fonts/Arial Rounded Bold.ttf', 60)
fnt3 = ImageFont.truetype('/Library/Fonts/Arial Rounded Bold.ttf', 30)
text = "Yesterday there were " + str(newcases) + "\n\nnew cases of COVID-19 \n\nreported in New Jersey, \n\nthat is a " + str(percent) + "% " + incdec + " in \n\ncases. This brings us to a total \n\nof " + str(cases) + " COVID-19 cases in \n\nNew Jersey and " + str(UScases) + " cases \n\nnationwide"

draw.text((10,10), "Today's COVID-19 \nUpdate:", font=fnt, fill=(226,62,89))
draw.text((40,350), text, font=fnt2, fill=(98,98,98))
draw.text((500,1300), "Source: NY Times COVID-19 Data", font=fnt3, fill=(0,0,0))

img.save('post.png')



