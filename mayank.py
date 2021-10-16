import discord
from discord.ext import commands
import json
import asyncio
Token = "ODczMTU4MDA4Mzc1NDkyNjI4.YTwjsw.IucPGXNJ_ig_37W9xXEyU8Al6l0"

client = commands.Bot(command_prefix='.m',self_bot=True)

@client.event
async def on_ready():
	print(f"Name - {client.user.name}\nID - {client.user.id}\nBot is working...")
	await client.change_presence(status = discord.Status.dnd)
	ch = client.get_channel(876519671086604368)
	await ch.send("<@834974192356294716>\n🤖 *Bot restarted!!*")
	

#				[ Channel Codes ]		  	#
@client.event
async def on_guild_channel_update(before: discord.abc.GuildChannel,after: discord.abc.GuildChannel):
	with open("key.json") as fp:
		Data = json.load(fp)
	chl = list(Data["Channels"].values())
	logs = list(Data["Logs"].values())
	teaml = list(Data["Teams"].values())
	tags = list(Data["Tags"].values())
	n = chl 
	server = after.guild.name
	chid = after.id
	
	if after.id not in n: return

	bot = before.guild.me
	before_send = before.permissions_for(bot).send_messages
	after_send = after.permissions_for(bot).send_messages

	if before_send != after_send and after_send:
		if chid in n[0:6]:
			Team = teaml[0]
			ch = client.get_channel(logs[0])
			tg = tags[0]
		
		if chid in n[6:12]:
			Team = teaml[1]
			ch = client.get_channel(logs[1])
			tg = tags[1]
		
		if chid in n[12:18]:
			Team = teaml[2]
			ch = client.get_channel(logs[2])
			tg = tags[2]
		
		if chid in n[18:24]:
			Team = teaml[3]
			ch = client.get_channel(logs[3])
			tg = tags[3]
		
		if chid in n[24:30]:
			Team = teaml[4]
			ch = client.get_channel(logs[4])
			tg = tags[4]
			
		if chid in n[30:36]:
			Team = teaml[5]
			ch = client.get_channel(logs[5])
			tg = tags[5]
			
		if chid in n[36:42]:
			Team = teaml[6]
			ch = client.get_channel(logs[6])
			tg = tags[6]					
					
		if chid in n[42:48]:
			Team = teaml[7]
			ch = client.get_channel(logs[7])
			tg = tags[7]

		if chid in n[48:54]:
			Team = teaml[8]
			ch = client.get_channel(logs[8])
			tg = tags[8]						

		if chid in n[54:60]:
			Team = teaml[9]
			ch = client.get_channel(logs[9])
			tg = tags[9]
						
		if chid==n[60]:
		  Team = "Testing Message!!!"
		  ch = client.get_channel(logs[10])
		  tg = tags[10]
			
		await after.send(Team)
		await ch.send(f"{tg} {client.user.mention}\n```py\n📢 Customs Info```Server Name - {server}\n*Your team has been successfully registered in <#{chid}>*\nPlease check the channel and your Slot no Carefully")

#	 		[	IDP Codes	]				  #
@client.event
async def on_message(message):
	async for message in message.channel.history(limit=1):
		with open("key.json") as fp:
			Data = json.load(fp)
		idpl = list(Data["IdpChannels"].values())
		logs = list(Data["Logs"].values())
		tags = list(Data['Tags'].values())
		n = idpl
		
		if message.channel.id in idpl:	
			server = message.guild.name
			msg = message.content
			chid = message.channel.id
			if chid in n[0:6]:
			  ch = client.get_channel(logs[0])
			  tg = tags[0]
			
			if chid in n[6:12]:
			  ch = client.get_channel(logs[1])
			  tg = tags[1]
			
			if chid in n[12:18]:
			  ch = client.get_channel(logs[2])
			  tg = tags[2]
			
			if chid in n[18:24]:
			  ch = client.get_channel(logs[3])
			  tg = tags[3]
			
			if chid in n[24:30]:
			  ch = client.get_channel(logs[4])
			  tg = tags[4]

			if chid in n[30:36]:
				ch = client.get_channel(logs[5])
				tg = tags[5]
			
			if chid in n[36:42]:
				ch = client.get_channel(logs[6])
				tg = tags[6]
			
			if chid in n[42:48]:
				ch = client.get_channel(logs[7])
				tg = tags[7]
			
			if chid in n[48:54]:
				ch = client.get_channel(logs[8])
				tg = tags[8]
			
			if chid in n[54:60]:
				ch = client.get_channel(logs[9])
				tg = tags[9]
			
			if chid==n[60]:
			  ch = client.get_channel(logs[10])
			  tg = tags[10]
		  
			if message.attachments:
				urls = [attachment.url for attachment in message.attachments]
				urlmsg = "\n".join(urls)
				await ch.send(f"{tg}\nFrom Server - {server}\nFrom Channel - <#{chid}>\n\n{msg}\n\n{urlmsg}")
			else :
				await ch.send(f"{tg} {client.user.mention}\nFrom Server - {server}\nFrom Channel - <#{chid}>\n\n{msg}")
		await client.process_commands(message)

#			COMMANDS 		#

# Ping Check
@client.command()
async def Ping(ctx):
	n = round(client.latency*1000)
	await ctx.reply(f"**📡 `{n}` ms**")	

# Data check
@client.command()
async def Data(ctx):
    with open("key.json","r") as fp:
    	Mydata = json.load(fp)
    teams = ""
    logs = ""
    tags = ""
    for i in Mydata['Teams']:
    	teams += f"```py\n{i} : {Mydata['Teams'][i]}\n```"
    for i in Mydata['Logs']:
    	logs += f"```py\n{i} : {Mydata['Logs'][i]}\n```"
    for i in Mydata['Tags']:
    	tags += f"```py\n{i} : {Mydata['Tags'][i]}\n```"
    
    await ctx.send(f"**Teams :**\n{teams}")
    await asyncio.sleep(1)
    await ctx.send(f"**Logs :**\n{logs}")
    await ctx.send(f"**Tags :**\n{tags}")
    
# Update Team	
@client.command(aliases=['UT','ut'])
async def UpdateTeam(ctx,key,*,value):
	with open("key.json","r") as fp:
	   NewData=json.load(fp)
	   keys = list(NewData['Teams'].keys())
	   if key not in keys :
	   	await ctx.reply("```\n❓ Invalid Key```")
	   	return
	   NewData['Teams'][key] = value
	   with open('key.json', 'w') as fp:
	   	json.dump(NewData, fp, indent=4)
	   await ctx.reply(f"☑️*Team details has been successfully updated*")
	   await asyncio.sleep(1)
	   await ctx.send(f"```py\n{key} : {NewData['Teams'][key]}```")

# Update channels
@client.command(aliases=['UCH','uch'])
async def UpdateChannel(ctx,key, value):
  id = int(value)
  with open("key.json","r") as fp:
    NewData=json.load(fp)
    keys = list(NewData['Channels'].keys())
    chnls = list(NewData['Channels'].values())
    if key not in keys :
    	await ctx.reply("```\n❓ Invalid Key```")
    	return
    if id in chnls and id != 0 :
    	await ctx.reply("```\n❓ This Channel ID already present in the data```")
    	for i in keys :
    		if NewData['Channels'][i] == id :
    			await ctx.send(f"```py\n{i} = {id}```") 		
    	return	   
    NewData['Channels'][key] = id
    with open('key.json', 'w') as fp:
        json.dump(NewData, fp, indent=4)
    await asyncio.sleep(1)   
    await ctx.send(f"{client.user.mention},\n☑️*Channel Id has been successfully updated*\n```py\nChannels :\n    {key} : {NewData['Channels'][key]}```")

# Update Idp channels
@client.command(aliases=['UIDPCH','uidpch'])
async def UpdateIdpChannel(ctx,key, value):
  id = int(value)
  with open("key.json","r") as fp:
    NewData=json.load(fp)
    keys = list(NewData['IdpChannels'].keys())
    chnls = list(NewData['IdpChannels'].values())
    if key not in keys :
    	await ctx.reply("```\n❓ Invalid Key```")
    	return
    if id in chnls and id != 0 :
    	await ctx.reply("```\n❓ This Channel ID already present in the data```")
    	for q in keys :
    		if NewData['IdpChannels'][q] == id :
    			await ctx.send(f"```py\n{q} = {id}```") 		    	
    	return	   
    NewData['IdpChannels'][key] = id
    with open('key.json', 'w') as fp:
        json.dump(NewData, fp, indent=4)
    await asyncio.sleep(1)
    await ctx.send(f"{client.user.mention},\n☑️*IDP Channel Id has been successfully updated*\n```py\nChannels :\n    {key} : {NewData['IdpChannels'][key]}```")

# Check Channels 
@client.command()
async def Channels(ctx):
  with open("key.json","r") as fp:
    Mydata = json.load(fp)
  y = ""
  for i in Mydata['Channels']:
  	y += f"{i} : <#{Mydata['Channels'][i]}>\n"
  await asyncio.sleep(1)
  await ctx.reply(f"```\nChannels :```\n{y}")

# Check Idp channels
@client.command()
async def IdpChannels(ctx):
  with open("key.json","r") as fp:
    Mydata = json.load(fp)
  y = ""
  for i in Mydata['IdpChannels']:
  	y += f"{i} : <#{Mydata['IdpChannels'][i]}>\n"
  await asyncio.sleep(1)
  await ctx.reply(f"```\nIdp Channels :```\n{y}")

# Team Details
@client.command()
async def Team(ctx,key):
	num = int(key)
	lt = [1,2,3,4,5,6,7,8,9,10]
	if num not in lt:
		await ctx.reply("```\n❓ Invalid Key```")
		return
	with open('key.json','r') as fp:
		data = json.load(fp)
	x = list(data["Tags"].values())
	y = list(data["Logs"].values())
	z = list(data["Teams"].values())
	p = 0
	q = 0
	if num == 1:
		p = 0
		q = 6
	elif num == 2:
		p = 6
		q = 12
	elif num == 3:
		p = 12
		q = 18
	elif num == 4:
		p = 18
		q = 24
	elif num == 5:
		p = 24
		q = 30
	elif num == 6:
		p = 30
		q = 36
	elif num == 7:
		p = 36
		q = 42
	elif num == 8:
		p = 42
		q = 48
	elif num == 9:
		p = 48
		q = 54
	elif num == 10:
		p = 54
		q = 60
						
	r = list(data['Channels'].values())
	g = list(data['IdpChannels'].values())
	n = p
	c = ""
	d = ""
	e = 0
	while e < 6:
		c += f"<#{r[n]}>\n"
		d += f"<#{g[n]}>\n"
		n += 1
		e += 1				
	await ctx.send(f"Team : {x[num-1]}\nLog channel : <#{y[num-1]}>\n```\n Team details :```{z[num-1]}")
	await asyncio.sleep(1)
	await ctx.send(f"```\nRegistration Channels : ```{c}\n```\nIdp Channels : ```{d}")

# Update Log channels	
@client.command(aliases=['ULCH','ulch'])
async def UpdateLogCh(ctx,key,value):
	value = int(value)
	with open("key.json","r") as fp:
	   NewData=json.load(fp)
	   keys = list(NewData['Logs'].keys())
	   if key not in keys :
	   	await ctx.reply("```\n❓ Invalid Key```")
	   	return
	   NewData['Logs'][key] = value
	   with open('key.json', 'w') as fp:
	   	json.dump(NewData, fp, indent=4)
	   await ctx.reply(f"☑️*Team Log Channel has been successfully updated*")
	   await asyncio.sleep(1)
	   await ctx.send(f"```py\n{key} : {NewData['Logs'][key]}```")
	   
# Update Tags 
@client.command(aliases=['UTAG','utag'])
async def UpdateTag(ctx,key,*,value):
	with open("key.json","r") as fp:
	   NewData=json.load(fp)
	   keys = list(NewData['Tags'].keys())
	   if key not in keys :
	   	await ctx.reply("```\n❓ Invalid Key```")
	   	return
	   NewData['Tags'][key] = value
	   with open('key.json', 'w') as fp:
	   	json.dump(NewData, fp, indent=4)
	   await ctx.reply(f"☑️*Team tag has been successfully updated*")
	   await asyncio.sleep(1)
	   await ctx.send(f"```py\n{key} : {NewData['Tags'][key]}```")	   

# Errors
@client.event
async def on_command_error(ctx, error): 
	if isinstance(error,commands.CommandNotFound):
		await ctx.reply("```\n❓ Command Not Found!!```")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.reply("```\n❓ Missing Required Argument```")
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.reply("```\n❓ Invalid Syntax```")
	else :
		ch = client.get_channel(883965820122832896)
		await ch.send(f"<@834974192356294716>\n{error}")	 					 					 		
				
client.run(Token, bot=False)
