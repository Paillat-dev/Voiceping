import discord
from config import bot, token
from utils import add_channel_roles, remove_channel_roles

@bot.event
async def on_ready():
    print("Bot is ready")
    #set the bot status to "Ping @voice_vhannel_name"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="@voice_channel_name"))

@bot.event
#when someone joins a voice channel
async def on_voice_state_update(member, before, after):
    '''Different cases:
    1. Member joins a voice channel:
        - Add the channel roles to the member
    2. Member leaves a voice channel:
        - Remove the channel roles from the member
    3. Member switches voice channels:
        - Remove the channel roles from the member for the old channel
        - Add the channel roles to the member for the new channel
    4. Member mutes/, or any change that dosen't change the voice channel id
        - Do nothing
    '''
    if before.channel is None:
        # Case 1
        await add_channel_roles(after.channel, member)
    elif after.channel is None:
        # Case 2
        await remove_channel_roles(before.channel, member)
    elif before.channel.id != after.channel.id:
        # Case 3
        await remove_channel_roles(before.channel, member)
        await add_channel_roles(after.channel, member)
    else:
        # Case 4
        pass


bot.run(token)