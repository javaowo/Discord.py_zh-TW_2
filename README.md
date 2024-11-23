# Discord.py第二章 機器人基本功能啟用
> 也是Ly1.0開源
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
這裡是指利用`on_message`來讓機器人讀取訊息，根據你給機器人的關鍵詞來決定他要做什麼事情。  
當然，執行的條件是他要能看到那個頻道的訊息（不論私訊或是伺服器頻道）
```python
@client.event 
async def on_message(message):

    if message.author == client.user:
        return
```
其中，`message.author`是指訊息的傳送者；`client.user`是指機器人本身  
這段程式碼意味著「當傳送訊息的人是機器人本身時，不執行以下的程式碼」  
所以這幾行通常會放在整個`on_message`的程式串最上方
