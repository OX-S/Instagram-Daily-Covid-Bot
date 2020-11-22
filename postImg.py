from instabot import Bot

username = '      '
password = '       '

bot = Bot()
bot.login(username = username,
	password = password)
bot.upload_photo('post.png',
	caption = 'Todays COVID-19 Update')
