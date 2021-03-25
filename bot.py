import discord
from discord.ext import commands
import time
import asyncio

bot = commands.Bot(command_prefix = '::', help_command = None) # ��ɾ� ���ξ� ����
token = ('ODIzOTQ2MTY4MjE5NTk4ODU5.YFoNqg.w_GOfkEBPfoiVwVEASHfKIx6U3Y') # Discord bot ��ū��(�س������)
users = {}

@bot.event # Bot �¶��� ���� �̺�Ʈ
async def on_ready() :
    print(f'���� ����: {bot.user.name}!')
    game = discord.Game("ī���� ���� ����") # ~~�ϴ��߿� ǥ��
    await bot.change_presence(status = discord.Status.online, activity = game)


@bot.command()
async def �ȳ�(ctx) :
    await ctx.send("�ȳ��ϼ���!")

@bot.command()
async def ���ν���(ctx):
    name = ctx.author.name
    if name in users.keys():
        await ctx.send("�̹� �������Դϴ�.")
    else:
        start_time = time.time()
        users[name] = start_time
        await ctx.send("{} �� ���� �����մϴ�.".format(name))

@bot.command()  
async def ��������(ctx):
    name = ctx.author.name
    if (name in users.keys()) == False:
        await ctx.send("���� ���� �ƴմϴ�.")
    else:
        finish_time = time.time()
        users[name] = finish_time - users[name]
        sec = users[name]
        hours = sec // 3600
        sec = sec - hours*3600
        minutes = sec // 60
        sec = sec - minutes*60
        await ctx.send("%s �� ���� �����մϴ�.\n���� �ð�: %.0f�ð� %.0f�� %.2f��" % (name, hours, minutes, sec))
        del users[name]

bot.run(token)