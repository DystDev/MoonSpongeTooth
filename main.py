import discord
import os
import random
from replit import db
from discord.ext import commands



actions = ["punch", "right_fist", "kiss", "people_hugging", "lips", "tongue", "anger_right", "eyes", "fencer: :heavy_plus_sign", "surfer: :heavy_plus_sign", "ring", "golf: :heavy_plus_sign", "bicyclist: :arrow_forward", "juggler", "dart: :heavy_plus_sign", "bowling: :heavy_plus_sign", "video_game: :heavy_plus_sign", "heart", "sparkling_heart", "sponge", "worship_symbol", "toothbrush", "shower", "gun", "scissors", "broken_heart", "football: :heavy_plus_sign", "soccer: :heavy_plus_sign", "basketball: :heavy_plus_sign", "rugby: :heavy_plus_sign", "ping_pong: :heavy_plus_sign", "boxing_glove: :heavy_plus_sign", "horse_racing: :heavy_plus_sign", "slot_machine: :heavy_plus_sign"]

iru = ["nerd", "cowboy", "imp", "japanese_ogre", "disguised_face", "clown", "ghost", "space_invader", "alien", "scream_cat", "heart_eyes_cat", "pouting_cat", "baby", "older_man", "man_with_chinese_cap", "spy", "cook", "farmer", "student", "health_worker", "person_bald", "child", "singer", "office_worker", "factory_worker", "technologist", "mechanic", "scientist", "artist", "firefighter", "pilot", "judge", "prince", "bride_with_veil", "santa", "angel", "man_walking", "woman_with_probing_cane", "person_in_motorized_wheelchair", "dancers", "dog", "cat", "mouse", "rabbit", "fox", "panda_face", "koala", "horse", "unicorn", "worm", "bug", "butterfly", "bee", "octopus", "snake", "blowfish", "zebra", "full_moon_with_face", "full_moon_with_face", "full_moon_with_face", "dragon", "sheep", "rooster", "squid", "monkey_face", "cockroach", "speak_no_evil", "man_in_manual_wheelchair", "man_frowning", "mage", "superhero", "man_in_tuxedo", "tooth", "bagel", "fries", "red_car"]



if "responding" not in db.keys():
  db["responding"] = True

client = discord.Client()


bot = commands.Bot(command_prefix="!", description='moonspongetooth - !help')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="!help"))
  print("Logged in as {0.user}".format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  
  if msg.startswith("!power"):
    value = msg.split("!power ",1)[1]
    if value.lower() == "on":
      db["responding"] = True
      embedVar = discord.Embed(title="Power", color=0x00ff00)
      embedVar.add_field(name="Responding: ", value="On", inline=False)
      await message.channel.send(embed=embedVar)
    elif value.lower() == "off":
      db["responding"] = False
      embedVar = discord.Embed(title="Power", color=0xFF0000)
      embedVar.add_field(name="Responding: ", value="Off", inline=False)
      await message.channel.send(embed=embedVar)
      
    else:
      return
    



  if db["responding"] != True:
    return
  iruOptions = iru
    
  if msg.startswith("!mst"):
    await message.channel.send(":full_moon_with_face: :sponge: :tooth:")
    await message.delete()
  if msg.startswith("!story"):
    await message.channel.send(":" + random.choice(iruOptions) + ": :" + random.choice(actions) + ": :" + random.choice(iruOptions) + ":")
    await message.delete()

  if msg.startswith("!help"):
    embedVar = discord.Embed(title="Help", color=0x00ff00)
    embedVar.add_field(name="Responding: ", value="Use !story for a short randomised 3/4 emoji story \n use !add then an emoji (without the colons - has to be a discord emoji - customs not supported yet) to add it to the generator e.g. !add weary \n use !view to view all manually added emojis and their index i.e not all stories with these will make sense \n use !del then the index of an item to delete e.g. !del 1 to delete first item. you can also use !del all to delete all custom emojis \n use !power on / !power off to turn bot on or off", inline=True)
    await message.channel.send(embed=embedVar)
  

  if msg.startswith("!add"):
    newEmoji = msg.split("!add ", 1)[1]
    add_emoji(newEmoji)
    embedVar = discord.Embed(title="Added", color=0x00ff00)
    embedVar.add_field(name="New Emoji Added: ", value=":" + newEmoji + ":", inline=True)
    await message.channel.send(embed=embedVar)

  if msg.startswith("!del"):
    emoji = []
    if 'emoji' in db.keys():
      index = msg.split("!del ", 1)[1]
      if index == "all":
        for x in range(0, len(db["emoji"]) + 1):
          del_emoji(0)
        
        embedVar = discord.Embed(title="Delted All", color=0x890000)
        embedVar.add_field(name="Completed: ", value='All Emojis Deleted', inline=True)
        await message.channel.send(embed=embedVar)
      else:
        index = int(index)
        del_emoji(index - 1)
        emoji = db["emoji"]
        embedVar = discord.Embed(title="Delted", color=0xFF0000)
        embedVar.add_field(name="Emoji Deleted - New List: ", value=emoji, inline=True)
        await message.channel.send(embed=embedVar)

  if msg.startswith("!view") or msg.startswith("!list"):
    emoji = []
    if "emoji" in db.keys():
      emoji = db["emoji"]
    embedVar = discord.Embed(title="List", color=0xEEEEEE)
    embedVar.add_field(name="List of custom emojis: ", value=emoji, inline=True)
    await message.channel.send(embed=embedVar)



def add_emoji(emoji_text):
  if "emoji" in db.keys():
    emoji = db["emoji"]
    emoji.append(emoji_text)
    db["emoji"] = emoji
  else:
    db["emoji"] = [emoji_text]



def del_emoji(index):
  emoji = db["emoji"]
  if len(emoji) > index:
    del emoji[index]
    db["emoji"] = emoji




client.run(os.getenv('TOKEN'))