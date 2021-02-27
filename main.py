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
      await message.channel.send("MST is now On. Happy storytelling!")
    elif value.lower() == "off":
      db["responding"] = False
      await message.channel.send("MST is now off.")
    else:
      return
    



  if db["responding"] != True:
    return
  iruOptions = iru
    
  
  if msg.startswith("!story"):
    await message.channel.send(":" + random.choice(iruOptions) + ": :" + random.choice(actions) + ": :" + random.choice(iruOptions) + ":")
    await message.delete()

  if msg.startswith("!help"):
    await message.channel.send("Use !story for a short randomised 3/4 emoji story \n use !add then an emoji (without the colons - has to be a discord emoji - customs not supported yet) to add it to the generator e.g. !add weary \n use !view to view all manually added emojis and their index i.e not all stories with these will make sense \n use !del then the index of an item to delete e.g. !del 1 to delete first item \n use !power on / !power off to turn bot on or off")

  if msg.startswith("!add"):
    newEmoji = msg.split("!add ", 1)[1]
    add_emoji(newEmoji)
    await message.channel.send("New emoji added: :" + newEmoji + ":")

  if msg.startswith("!del"):
    emoji = []
    if 'emoji' in db.keys():
      index = int(msg.split("!del", 1)[1])
      del_emoji(index - 1)
      emoji = db["emoji"]
      await message.channel.send("New user emojis: ")
      await message.channel.send(emoji)

  if msg.startswith("!view"):
    emoji = []
    if "emoji" in db.keys():
      emoji = db["emoji"]
    await message.channel.send(emoji)



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