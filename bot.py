import discord
from discord.ext import commands
from discord.ext.commands import Bot, Greedy
import asyncio
from discord import user
from discord import User
from discord import channel
from discord import Member
import random
from discord import Intents
from dotenv import load_dotenv
import os
import json
load_dotenv()

TOKEN = os.getenv("TOKEN")



intents = Intents.all()



from discord.ext.commands.errors import ArgumentParsingError, MissingRequiredArgument
bot = commands.Bot(command_prefix='g.', intents = intents, case_insensitive=True)
os.chdir(r'')

bot.remove_command('help')


bot.sniped_messages = {}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f'currently moderating {len(bot.guilds)} servers!'))
    print("montigraal is ready to be used")
    
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    emb=discord.Embed(title = "member kicked!", description = f'I have kicked {member.name} from the server! Reason: {reason}, color 0xff0303')
    emb.add_field(name="responsible moderator", value=f'{ctx.author.mention}', inline = False)
    emb.set_thumbnail(url=f'{ctx.member.avatar_url}')
    emb2=discord.Embed(title=f"You have been kicked from {ctx.guild.name}", color=0xff0303)
    emb2.add_field(name="Responsible Moderator:", value=f'{ctx.author.name}', inline=False)
    emb2.add_field(name="Reason:", value=f'{reason}', inline=False)
    await member.send(embed=emb2)
    await member.kick(reason=reason)
    await ctx.send(embed=emb)

@kick.error
async def kick_error(ctx: commands.Context,error: commands.CommandError):
 if isinstance(error, commands.MissingPermissions):
    message = "you are missing the `kick members` permission to run this command"
    await ctx.send(message)

 elif isinstance(error, commands.MissingRequiredArgument):
     message = "ping someone to kick them!"
     await ctx.send(message)

 elif(error, ArgumentParsingError):
     message = "You can't kick your self or anyone that is the same role as you or higher!"
     await ctx.send(message)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    role=discord.utils.get(ctx.guild.roles, name="Staff")
    if role in member.roles:
        embed=discord.Embed(description="You can't ban this member as they are staff", color=0xFF0000)
        await ctx.send(embed=embed)
    else:
        await member.ban(reason = reason)
        embed=discord.Embed(description=f"{member.mention} has been banned. Reason: **{reason}**", color=ctx.author.color)
        await ctx.send(embed=embed)
        embed=discord.Embed(title=f"You have been been from {ctx.guild}.", description=f"Reason: {reason}", timestamp=ctx.message.created_at)
        embed.set_footer(text=f"ID: {member.id}", icon_url=member.avatar_url)
        userToDM = bot.get_user(member.id)
        await userToDM.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
    guild = ctx.guild
    user = await bot.fetch_user(id)
    await guild.unban(user)
    emb=discord.Embed(title="unban", description=f'I have unbanned {user.name} from {guild.name}', color = 0xfffff)
    await ctx.send(embed=emb)

@unban.error
async def unban_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        message = "You do not have the `ban_members` permission to run this command!"
        await ctx.send(message)

    elif isinstance(error, commands.MissingRequiredArgument):
        message = "Please put a discord ID to unban!"
        await ctx.send(message)

    elif isinstance(error, ArgumentParsingError):
        message = "This user seems to not be banned or is already unbanned!"
        await ctx.send(message)


@bot.command()
async def dm(ctx, users: Greedy[User], *, message):
    for user in users:
        await user.send(message)
        await ctx.message.delete()


@dm.error
async def dm_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        message = "Put a message you want me to dm to this user!"

@bot.command(aliases = ['clear'])
@commands.has_permissions(administrator=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)

    emb=discord.Embed(title=f"{amount} messages have been cleared!", color=0xff0303)
    emb.add_field(name=f'executed by {ctx.author.name}', value=f'channel purged: {ctx.channel.name}')
    msg=await ctx.send(embed=emb, delete_after=1)

@purge.error
async def purge_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        message = "You do not have the `delete messaged` permission to run this commnd!"
        await ctx.send(message)

    elif isinstance(error, commands.MissingRequiredArgument):
        message2 = "please enter a number to purge"
        await ctx.send(message2)


password = ["iSmElLy0u69696","yourmom420", "pOrNhuuuub", "password", "peeeeeeepeeeeeeepoooooopoooooo"]
email = ["@gmail.com", "@yahoo.com", "@outlook"]
@bot.command(aliases = ['hack'])
async def hecc(ctx, member: discord.Member):
    hack = await ctx.send(f"starting the hack process on {member.name}..")
    await asyncio.sleep(2.25)
    await hack.edit(content=f'**[25%]** Finding {member.name}\'s ip')
    await asyncio.sleep(2.5)
    await hack.edit(content="**[45%]** IP found!")
    await asyncio.sleep(2.25)
    await hack.edit(content="Sending ip to hacker")
    await ctx.author.send(f"{member.name}\'s ip address: 127.0.0.1")
    await hack.edit(content='**[52%]** Finding Email and Password.')
    await asyncio.sleep(2.01)
    await hack.edit(content='**[52%]** Finding Email and Password..')
    await asyncio.sleep(2.5)
    await hack.edit(content='**[60%]** Email and Password found! Sending to hacker..')
    await asyncio.sleep(2.5)
    await ctx.author.send(f"{member.name}'s *totally* real email and password.")
    await ctx.author.send(f"{member.name}{random.choice(email)}")
    await ctx.author.send(random.choice(password))
    await asyncio.sleep(2.1)
    await hack.edit(content=f'**[66%]** Reporting {member.name} to the discord TOS')
    await asyncio.sleep(2.1)
    await hack.edit(content=f'**[75%]** Reporting {member.name} to the fbi')
    await asyncio.sleep(2.1)
    await hack.edit(content='Completing hack.')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack..')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack...')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack.')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack..')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack...')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack.')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack..')
    await asyncio.sleep(.1)
    await hack.edit(content='Completing hack...')
    await asyncio.sleep(.1)
    await hack.edit(content=f"**[100%]**the *totally* real hack completed on {member.name}!")  

@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@bot.command()
async def snipe(ctx):
    try:

        contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
    except:
        await ctx.channel.send("No message was deleted!")
        return
         
    embed = discord.Embed(description=contents, color = discord.Colour.random(), timestamp=time)
    embed.set_author(name=f'{author.name}', icon_url=author.avatar_url)
    embed.set_footer(text="caught in 4k")

    await ctx.channel.send(embed=embed)

@bot.event
async def on_message(message):
    if "deez nuts" in message.content:
        message = message.channel
        await message.send("https://cdn.discordapp.com/emojis/855104399676407848.gif?v=1")
    await bot.process_commands(message)

@bot.command(aliases = ['av'])
async def avatar(ctx, *, member : discord.Member=None):
    
    if member == None:
        member = ctx.author

    emb=discord.Embed(title = f"{member.name}'s avatar", color = discord.Colour.random())
    emb.set_image(url=member.avatar_url)
    await ctx.send(embed=emb)

@bot.command()
@commands.is_owner()
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete(reason="Channel has been nuked!")
        await new_channel.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
        await ctx.send("Nuked the Channel sucessfully!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@bot.command()
async def help(ctx):
    emb=discord.Embed(title = "Help commands", color = discord.Colour.random())
    emb.add_field(name = "List of command types", value = "fun, moderation", inline = False)
    await ctx.send(embed=emb)

    
    if "fun" in message.content:
        e=discord.Embed(title = "fun commands", description = "g.hecc, g.snipe, g.dm", color = discord.Colour.random())
        await message.send(embed=e)

@bot.command(aliases = ['guildcount'])
async def guilds(ctx):
    emb=discord.Embed(title = "Guild Number:", description = f'I am currently in {len(bot.guilds)} servers', color = discord.Colour.random())
    await ctx.send(embed=emb)

@bot.command(aliases = ['gl'])
async def guildlist(ctx):
    emb=discord.Embed(title = "List of guilds i am in", description = f'{[guild.name for guild in bot.guilds]}', color = discord.Colour.random())
    await ctx.send(embed=emb)

@bot.command(aliases = ['inv'])
async def botinvite(ctx):
    link = ''
    await ctx.send(f"invite me to your server! <{link}>")


@bot.command(aliases = ['whois', 'ui'])
async def userinfo(ctx, member : discord.Member = None):
    
    member = ctx.member or ctx.author
    roles = [role for role in member.roles][1:]

    emb=discord.Embed(title = f'{member.name} user info', color = discord.Colour.random(), timestamp = ctx.message.created_at)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f'Requested by {ctx.author.name}')
    emb.add_field(name="nickname", value=member.display_name, inline=False)
    emb.add_field(name="Discord name", value=member.name, inline=False)
    emb.add_field(name="ID", value=member.id, inline=False)
    emb.add_field(name="account creation date", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
    emb.add_field(name="server join date", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
    emb.add_field(name = f'roles ({len(roles)})', value= " ".join([role.mention for role in roles]) or "No Roles", inline = False)
    emb.add_field(name="top role", value=member.top_role.mention, inline = False)
    emb.add_field(name='Is bot?', value=member.bot, inline=False)
    await ctx.send(embed=emb)

@bot.command()
@commands.is_owner()
async def stop (ctx):
    await ctx.send("stopping bot..")
    await asyncio.sleep(2)
    await ctx.bot.close()
    print("bot is down")


@bot.command(aliases = ['tempmute'])
@commands.has_permissions(manage_messages=True, manage_roles=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    guild = ctx.guild
    muterole = discord.utils.get(guild.roles, name="Muted")
    
    if not muterole:
        muterole = await guild.create_role(name="Muted")
        for channel in guild.channels:
           await channel.set_permissions(muterole, speak=False, send_messages=False)


    await member.add_roles(muterole, reason=reason)
    emb=discord.Embed(description = f":white_check_mark: I have muted {member.name}! Reason: {reason}", color = discord.Colour.random())
    await ctx.send(embed=emb)
    emb2=discord.Embed(title = f'you were muted in {guild}!', color=discord.Colour.random())
    emb2.add_field(name="Reason", value = reason, inline = False)
    emb2.add_field(name="responsible moderator", value=ctx.author.mention, inline = False)
    await member.send(embed=emb2)

@bot.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild
    muterole = discord.utils.get(guild.roles, name = "Muted")
    c = ctx
    await member.remove_roles(muterole)
    emb=discord.Embed(description=f'I have unmuted {member.name}', color = discord.Colour.random())
    await c.send(embed=emb)
    await member.send(f'You have been unmuted in {guild}')



@bot.command(aliases = ['fm'])
@commands.has_permissions(manage_roles = True)
async def filemute(ctx, member : discord.Member, *, reason=None):
    guild = ctx.guild
    fmrole = discord.utils.get(guild.roles, name = 'Filemuted')
    if fmrole in member.roles:
        await ctx.send("This person is already filemuted!")

    if not fmrole:
        fmrole = await guild.create_role(name='Filemuted')
        for channel in guild.channels:
            await channel.set_permissions(fmrole, attach_files = False)

    
    
    await member.add_roles(fmrole, reason=reason)
    emb=discord.Embed(description = f':white_check_mark: I have filemuted {member}! Reason: {reason}', color = discord.Colour.random())
    await ctx.send(embed=emb)
    emb2=discord.Embed(description = f"You have been filemuted in {guild}!", color = discord.Colour.random())
    emb2.add_field(name='Reason:', value=reason, inline = False)
    emb2.add_field(name="responible mod:", value = ctx.author.name, inline = False)
    await member.send(embed=emb2)

@bot.command(aliases = ['unfm'])
@commands.has_permissions(manage_roles = True)
async def unfilemute(ctx, member : discord.Member):
    guild = ctx.guild
    fmrole = discord.utils.get(guild.roles, name = 'Filemuted')
    if fmrole not in member.roles:
        await ctx.send(f"{member.name} is not filemuted!")
    else:
        await member.remove_roles(fmrole)
        emb=discord.Embed(description = f'I have unfilemuted {member.name}!', color = discord.Colour.random())
        await ctx.send(embed=emb)
        await member.send(f"You have been unfilemuted from {guild}!")

@bot.command()
async def suggest(ctx, *, message):
    channel = bot.get_channel(channel_id)
    semb=discord.Embed(title="Suggestion", description=message, color=discord.Colour.random())
    semb.set_footer(text="i approve: ✅, i disapprove: ❌")
    message = await channel.send(embed=semb)
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    await ctx.send("suggestion added!")

@bot.command(aliases=['renick'])
async def nick(ctx, member : discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f"I changed {member.mention}'s name!")

@bot.command(aliases=['giverole'])
@commands.has_permissions(administrator = True)
async def addrole(ctx, user : discord.Member, *, role : discord.Role):
    if role.position > ctx.author.top_role.position:
        return await ctx.send("This role is above your role!")
    if role in user.roles:
        await ctx.send(f"{role} is already in {user.name}'s roles!")
    else:
        await user.add_roles(role)
        await ctx.send(f"I have added {role} to {user.name}")

@bot.command()
@commands.has_permissions(administrator = True)
async def removerole(ctx, user : discord.Member, *, role : discord.Role):
    if role.position > ctx.author.top_role.position:
        return await ctx.send("this role is above your role!")
    if role not in user.roles:
        await ctx.send(f"This role is not in {user.name}'s roles!")
    else:
        await user.remove_roles(role)
        await ctx.send(f"I have removed {role} from {user.name}!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

 
@bot.command()
@commands.has_permissions(manage_channels = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Slowmode delay set to {seconds} seconds.")


@bot.command()
async def moderation(ctx):
    em=discord.Embed(title="Current list of moderation commands:", description="g.kick, g.ban, g.unban, g.purge, g.mute, g.unmute, g.filemute, g.unfilemute, g.nick, ,g.addrole, g.removerole, g.slowmode", color = discord.Colour.random())
    em.set_footer(text="More commands will be added in the future!")
    await ctx.send(embed=em)


@bot.command()
async def fun(ctx):
    e=discord.Embed(title="List of current fun commands:", description="g.hecc, g.snipe, g.dm", color = discord.Colour.random())
    e.set_footer(text="More commands will be added in the future!")
    await ctx.send(embed=e)


@bot.command(aliases = ['repeat'])
async def say(ctx,*, message):
    await ctx.message.delete()
    e=discord.Embed(title = "Message", description = message, color = discord.Colour.random())
    await ctx.send(embed=e)


@bot.command(aliases = ['gp'])
async def ghostping(ctx, *, message):
    channel = bot.get_channel()
    await ctx.message.delete()
    e=discord.Embed(title = "ghostping/message", description = message)
    await channel.send(embed=e)

@bot.command()
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx, channel : discord.TextChannel=None):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    e=discord.Embed(description=f"✅ {channel.name} has been locked!")
    await ctx.send(embed=e)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    e=discord.Embed(description=f"✅ {channel.name} has been unlocked!")
    await ctx.send(embed=e)

@bot.event
async def on_message(message):
    if "what da dog doin" in message.content:
        message = message.channel
        e=discord.Embed(description = "I know what da dog doin but im not telling you 😉", color=0xff0303)
        await message.send(embed=e)
    await bot.process_commands(message)


@bot.event
async def on_message(message):
    if "w0t" in message.content:
        await message.delete()
    await bot.process_commands(message)


@bot.event
async def on_message(message):
    if "tired" in message.content:
        e = discord.Embed(color = discord.Colour.random())
        e.set_image(url="https://cdn.discordapp.com/attachments/755023686989250600/945375399532199976/60v1s1.jpg")
        await message.reply(embed=e)
    await bot.process_commands(message)


@bot.command()
async def saul(ctx, user: discord.User = None):

    author = ctx.message.author

    if user == None:
        await ctx.send("mention a user to get sauled")
        return

    if user == author:
        await ctx.send("you can't saul yourself")
        return


    e=discord.Embed(title = "sauled", description = f"{user.name} has been sauled by {author.name}", color = discord.Colour.red())
    e.set_image(url = "https://cdn.discordapp.com/attachments/895150178540081172/991875288415862814/3d-saul-saul-goodman.gif")
    await ctx.send(embed=e)


bot.run(TOKEN)
