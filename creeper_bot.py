# This bot requires the 'message_content' intent.

import discord
from discord import app_commands



#----- Bot

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)



#----- Slash Commands

@tree.command(name = "finish", description = "nut") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message(":camera_with_flash:")
    
@tree.command(name = "creeper", description = "sssssss") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message(".\nCreeper, oh man\nSo we back in the mine, got our pick axe swinging from side to side,\nSide, side to side\nThis task a grueling one, hope to find some diamonds tonight, night, night\nDiamonds tonight\nHeads up, you hear a sound, turn around and look up, total shock fills your body,\nOh no it\'s you again,\nI could never forget those eyes, eyes, eyes,\nEyes, eyes, eyes\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again\nJust when you think you\'re safe, overhear some hissing from right behind,\nRight, right behind\nThat\'s a nice life you have, shame it\'s gotta end at this time, time, time,\nTime, time, time, time\nBlows up, then your health bar drops, you could use a 1-up, get inside don\'t be tardy,\nSo now you\'re stuck in there, half a heart is left but don\'t die, die, die\nDie, die, die, die\n\'Cause baby tonight, the creeper\'s trying to steal all your stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'")
    #await interaction.response.send_message(".\n\'Cause baby tonight, the creeper\'s trying to steal all your stuff again,\nCreepers, you\'re mine\nDig up diamonds, and craft those diamonds and make some armor,\nGet it baby, go and forge that like you so, MLG pro,\nThe sword\'s made of diamonds, so come at me bro\nTraining in your room under the torch light,\nHone that form to get you ready for the big fight,\nEvery single day and the whole night,\nCreeper\'s out prowlin\' - alright\nLook at me, look at you,\nTake my revenge that\'s what I\'m gonna do,\nI\'m a warrior baby, what else is new,\nAnd my blade\'s gonna tear through you\nBring it\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\nYeah baby tonight, grab your sword, armor and gold, take your revenge,\nSo fight, fight like it\'s the last, last night of your life, life, show them your bite,\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'\n\'Cause baby tonight, the creepers tried to steal all our stuff again")



#----- Bot Start

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')



#----- Live Response

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("creeper"):
        await message.channel.send(".\nCreeper, oh man\nSo we back in the mine, got our pick axe swinging from side to side,\nSide, side to side\nThis task a grueling one, hope to find some diamonds tonight, night, night\nDiamonds tonight\nHeads up, you hear a sound, turn around and look up, total shock fills your body,\nOh no it\'s you again,\nI could never forget those eyes, eyes, eyes,\nEyes, eyes, eyes\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again\nJust when you think you\'re safe, overhear some hissing from right behind,\nRight, right behind\nThat\'s a nice life you have, shame it\'s gotta end at this time, time, time,\nTime, time, time, time\nBlows up, then your health bar drops, you could use a 1-up, get inside don\'t be tardy,\nSo now you\'re stuck in there, half a heart is left but don\'t die, die, die\nDie, die, die, die\n\'Cause baby tonight, the creeper\'s trying to steal all your stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'")
        await message.channel.send(".\n\'Cause baby tonight, the creeper\'s trying to steal all your stuff again,\nCreepers, you\'re mine\nDig up diamonds, and craft those diamonds and make some armor,\nGet it baby, go and forge that like you so, MLG pro,\nThe sword\'s made of diamonds, so come at me bro\nTraining in your room under the torch light,\nHone that form to get you ready for the big fight,\nEvery single day and the whole night,\nCreeper\'s out prowlin\' - alright\nLook at me, look at you,\nTake my revenge that\'s what I\'m gonna do,\nI\'m a warrior baby, what else is new,\nAnd my blade\'s gonna tear through you\nBring it\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\nYeah baby tonight, grab your sword, armor and gold, take your revenge,\nSo fight, fight like it\'s the last, last night of your life, life, show them your bite,\n\'Cause baby tonight, the creeper\'s trying to steal all our stuff again,\n\'Cause baby tonight, you grab your pick, shovel and bolt again,\nAnd run, run until it\'s done, done, until the sun comes up in the morn\'\n\'Cause baby tonight, the creepers tried to steal all our stuff again")



#----- Token
client.run('MTEzNTY3MDM3MzA0ODkxODEwNg.GRzjHU.goYL-hpimCJrJFpTVcy8_NshWR6ctRF8COLbSc')