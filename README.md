# Discord.py第二章 機器人基本功能啟用
> 也是Ls1.0版本開源
## 前言
自己在摸資料的時候摸到一個酷東西  
```python
import discord; discord.Client(intents=discord.Intents.default()).run("你的機器人TOKEN")
```
嗯對，一行指令便能啟動機器人  
看來我還是太小看python的簡化力量了（  

這篇有以下兩個主題，可善用`ctrl+F`搜尋你想要的內容  
- Discord機器人偵測訊息
- 前綴指令使用
  
可能有人會覺得只有兩個很少，但這兩個已經可以延伸出超多東西了  
> 這篇只會教基本的，請放心

## Discord機器人偵測訊息
底下會一一解釋這些程式碼在幹嘛
```python
@client.event 
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('你好'):
        await message.channel.send('Hello!')

    await client.process_commands(message)
```

1. `om_message`是什麼？
   - 這裡是指利用`on_message`來讓機器人讀取訊息，根據你給機器人的關鍵詞來決定他要做什麼事情。  
     當然，執行的條件是他要能看到那個頻道的訊息（不論私訊或是伺服器頻道）
   - 後面()裡面的`message`是給「機器人收到的訊息」定義一個參數名稱，以進行使用

2. 第一個if條件是什麼意思？
   - `message.author`是指訊息的傳送者
   - `client.user`是指機器人本身  
   - 這段程式碼意味著「當傳送訊息的人是機器人本身時，不執行以下的程式碼」  
     所以這幾行通常會放在整個`on_message`的程式串最上方，讓機器人不會進入死循環

3. 第二個if條件是什麼意思？
   - `message.content.startswith`指的是「當訊息的開頭為...」
   - `message.channel.send`指的是「傳送訊息到觸發機器人執行工作的訊息的頻道」  
     這段文字看起來很饒舌，簡而言之就是「你從哪裡叫他，他就從哪裡回你」的概念
   - 所以這段程式碼的意思是：「當訊息的開頭為『你好』時，傳送一條訊息」
  
5. 最後一行的await是在等什麼？
   - `process_commands`會檢查此訊息是否為前綴指令，通常會放在最後一行，以保證前面的條件式不會被這行的檢查覆蓋
   - 如果沒有這行程式碼，那麼所有前綴指令將**全部**無法運作

## 前綴指令使用
1. 這東西跟斜線指令不一樣，看你`command_prefix`裡面寫什麼訊息開頭就要寫什麼
2. 每個機器人都內建一個「!help」查詢可用指令，記得，那個「!」是根據你`command_prefix`裡面打的東西決定什麼開頭接help
   > 假設你的前綴開頭是`command_prefix='&'`，那你就要輸入「&help」來做查詢

下面來解釋一下這幾行程式碼在幹嘛
```python
@client.command(name= 'test' , help = '測試指令') 
async def test(ctx):
    await ctx.send('Hello!')
```
1. 前綴指令名稱：test，透過「!test」來呼叫程式
2. name跟help可以不用寫，那個只是在你使用「!help」會顯示的東西，如果不打指令名稱會預設為「async def」後面的那個
3. `ctx.send`邏輯跟上面的`message.channel.send`一樣
  
把它全部結合起來你就會得到這樣一個東西：
```python
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'My ID is {client.user.id}')

@client.event 
async def on_message(message):

    if message.author == client.user: 
        return
    
    if message.content.startswith('你好'): 
        await message.channel.send('Hello!') 

    await client.process_commands(message) 

@client.command(name= 'test' , help = '測試指令') 
async def test(ctx):
    await ctx.send('Hello!')

client.run("YOUR_BOT_TOKEN")
```
  
## 後話
熱知識：  
1. python裡面「'」跟「"」是可以通用的  
2. 很多提到的參數名稱是都可以隨便改的，只是現在說的名稱比較通用+好閱讀  

其實泠珊是從泠伊1.5版本之後才獨立出來的，所以她們兩隻的版本數有點亂（  
這邊還是先通稱為泠珊1.0版本  
等我整理好再來改吧030
