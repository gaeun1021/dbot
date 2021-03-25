import discord
from discord.ext import commands
import time
import asyncio

bot = commands.Bot(command_prefix = '::', help_command = None) # 명령어 접두어 설정
token = ('ODIzOTQ2MTY4MjE5NTk4ODU5.YFoNqg.w_GOfkEBPfoiVwVEASHfKIx6U3Y') # Discord bot 토큰값(※노출금지)
users = {}

@bot.event # Bot 온라인 접속 이벤트
async def on_ready() :
    print(f'부팅 성공: {bot.user.name}!')
    game = discord.Game("카페인 과다 수혈") # ~~하는중에 표시
    await bot.change_presence(status = discord.Status.online, activity = game)


@bot.command()
async def 안녕(ctx) :
    await ctx.send("안녕하세요!")

@bot.command()
async def 공부시작(ctx):
    name = ctx.author.name
    if name in users.keys():
        await ctx.send("이미 공부중입니다.")
    else:
        start_time = time.time()
        users[name] = start_time
        await ctx.send("{} 님 공부 시작합니다.".format(name))

@bot.command()  
async def 공부종료(ctx):
    name = ctx.author.name
    if (name in users.keys()) == False:
        await ctx.send("공부 중이 아닙니다.")
    else:
        finish_time = time.time()
        users[name] = finish_time - users[name]
        sec = users[name]
        hours = sec // 3600
        sec = sec - hours*3600
        minutes = sec // 60
        sec = sec - minutes*60
        await ctx.send("%s 님 공부 종료합니다.\n공부 시간: %.0f시간 %.0f분 %.2f초" % (name, hours, minutes, sec))
        del users[name]

bot.run(token)