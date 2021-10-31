from discord.ext import commands
import discord
from selenium import webdriver
import os
import time
from key_gen import assigner
from keep_alive import keep_alive
from discord.utils import get
driver = webdriver.Firefox()
fn = assigner.Create()

def error():
  with open("error.png", 'rb') as fp:
    print(fp)
    return "error.png"

def get_page(page):
  if not page.startswith("https://"):
    url = f"https://infinityiron.xyz/{page}"
  elif page.startswith("https://") or page.startswith("http://"):
    url = page
  try:
    driver.get(page)
    #time.sleep(5)
    driver.get_screenshot_as_file(f"{fn}.png")
    with open(f"{fn}.png", 'rb') as fp:
      return {"fp" : f"{fn}.png", "f" : fp, "fn" : fn}
  except Exception as E:
    return {"fp" : E}

def get_pageb(page):
  try:
    driver.get(f'https://beta.infinityiron.xyz/{page}')
    driver.get_screenshot_as_file(f"{fn}.png")
    with open(f"{fn}.png", 'rb') as fp:
      return {"fp" : f"{fn}.png", "f" : fp, "fn" : fn}
  except Exception as E:
    return {"fp" : E}

def get_(page):
  try:
    driver.get(f'https://{page}')
    driver.get_screenshot_as_file(f"{fn}.png")
    with open(f"{fn}.png", 'rb') as fp:
      return {"fp" : f"{fn}.png", "f" : fp, "fn" : fn}
  except Exception as E:
    print(E)
    return

bot = commands.Bot(command_prefix="$!")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 866024988901638185 and payload.emoji.name == "<:cantrash:850571950408335391>":
      channel = bot.get_channel(614467771866021944)

      message = await channel.fetch_message(payload.message_id)

      reaction = get(message.reactions, emoji=payload.emoji.name)

      if reaction and reaction.count > 1:
        
        await message.delete()


@bot.command()
async def _get(ctx, page: str):
  await ctx.trigger_typing()
  await ctx.send(file=discord.File(get_page(page)['fp'], 'new_filename.png'))
  os.remove(f'{fn}.png')

@bot.listen('on_message')
async def chec(message):
  ctx = await bot.get_context(message)
  if message.content.startswith("http://") or message.content.startswith("https://"):
    try:
      await ctx.trigger_typing()
      a = await ctx.reply(f"preview of `{message.content}`",file=discord.File(get_page(message.content)['fp'], "DisFrame.png"))
      await a.add_reaction("<:cantrash:850571950408335391>")
      os.remove(f"{fn}.png")
    except Exception as E:
      os.remove(f"{fn}.png")
      return print(E)


keep_alive()
bot.run(os.environ['token'])