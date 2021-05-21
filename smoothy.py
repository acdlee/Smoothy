'''
Application Name: Smoothy
Author: Christopher Lee
Date: 05/21/2021 - ...

Smoothy is a program similar to the discord bot Groovy
where a user can play Twitch streams. 

Created using the documentation at:
		https://discordpy.readthedocs.io/en/stable/index.html


Explore this file next time:
	https://github.com/Rapptz/discord.py/blob/v1.7.2/examples/basic_voice.py
'''

import discord
import logging 

logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


channel = None
@client.event
#Handle message events; message has class Message
async def on_message(message):
	author = message.author		#author has class Member; i.e. the user
	#no action if the client sends a message
	if author == client.user:	
		return

	#join the channel command
	if message.content.lower() == '$join':
		#check if the user is in a voice channel
		if not author.voice:	#voice has class VoiceState
			#request they join a voice channel
			await message.channel.send('You have to join a voice channel!')
			return

		#check if we're already in a channel
		if channel:
			message.channel.send('Sorry, someone is already enjoying their Smoothy.')
			return 
					
		channel = author.voice.channel
		await author.voice.channel.connect()	#joins the author's voice channel

	#force the bot to leave the channel
	if message.content.lower() == '$leave':
		#check if the bot is even in a channel
		if not channel:
			"I'm currently not in a channel!"
			return

		#leave the channel and reset the variable channel to None
		await channel.disconnect()
		channel = None
		



client.run('token')
