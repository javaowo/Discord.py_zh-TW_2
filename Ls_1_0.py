# 調用Discord函式庫
import discord

# 從Discord.py引入處理指令的模組
from discord.ext import commands

"""
1. 命名處理機器人的物件「client」  
2. 命名機器人的前綴指令符號「!」，可根據需求更改為自己想要的前綴符號（不限）  
3. 賦予機器人接收訊息的權限「intents」，其中「Intents.all」代表機器人能夠接收所有可用的訊息  
"""
client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

"""
1. 使用一個事件處理器
2. 當機器人完全啟動並連接到Discord的時候，打印已登入的機器人名稱和ID
"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'My ID is {client.user.id}')

"""
1. 使用一個事件處理器
2. 避免機器人回覆自己的訊息
3. 當機器人收到一個開頭為「你好」的訊息時，執行程式碼
4. 檢查訊息是否為前綴指令的訊息
"""
@client.event 
async def on_message(message):

    if message.author == client.user: # 避免機器人自己回覆自己
        return
    
    if message.content.startswith('你好'): # 當機器人被提及時
        await message.channel.send('Hello!') # 回覆訊息 

    await client.process_commands(message) # 處理指令

"""
1. 使用一個指令處理器
2. 當機器人收到一個開頭為「!」前綴符號的訊息時，尋找匹配指令名稱並執行
"""
@client.command(name= 'test' , help = '測試指令') 
async def test(ctx):
    await ctx.send('Hello!')

# 起動機器人，記得先把「YOUR_BOT_TOKEN」替換成你的機器人的Token 
client.run("YOUR_BOT_TOKEN")
