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
    
    if message.content.startswith(f'<@!{client.user.id}> ') or message.content.startswith(f'<@{client.user.id}> '):
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
     所以這幾行通常會放在整個`on_message`的程式串最上方

3. `<@!{client.user.id}>`跟`<@{client.user.id}>`差在哪？這個if條件又有什麼作用？
   - `<@!{client.user.id}>`是當機器人在伺服器有暱稱時所帶有的格式，`<@{client.user.id}>`這個則是機器人原名稱帶有的格式（如在私訊中或是機器人在伺服器中沒有暱稱時）
   - 這段程式碼意味著「當機器人被標註時，傳送一條訊息至該頻道」
   - `message.channel.send`指的是「傳送訊息到觸發機器人執行工作的訊息的頻道」，這段文字看起來很饒舌，簡而言之就是「你從哪裡叫他，他就從哪裡回你」
4. 最後一行的await是在等什麼？
   - 這行程式碼會檢查此訊息是否為前綴指令，通常會放在最後一行，以保證前面的條件式不會被這行的檢查覆蓋
   - 如果沒有這行程式碼，那麼所有前綴指令將全部無法運作
