import discord
from discord.ext import commands
from Core.classes import Bot_Cog
from Core.errors import Errors
import json

with open("config.json",mode="r",encoding="utf-8") as file:
    data = json.load(file)
    messageId = int(data['Message_id'])
class Event(Bot_Cog):

    @commands.Cog.listener()      #按下表情符號加入身分組
    async def on_raw_reaction_add(self,payload) -> None:  #表情符號偵測
        guild = self.bot.get_guild(payload.guild_id)  #取得當前伺服器
        #新增貼圖獲得身分組
        if payload.message_id == messageId:
            if str(payload.emoji) == data['emoji1']:
                print('Adding to test_role1...')
                role = guild.get_role(int(data['test_role1']))   #取得指定身分組
                try:
                    await payload.member.add_roles(role)
                except Exception as e:
                    print(e)
                await payload.member.send(f'加入 {role} 身分組')
                print('Success')
            elif str(payload.emoji) == data['emoji2']:
                print('Adding to test_role2...')
                role = guild.get_role(int(data['test_role2']))   #取得指定身分組
                try:
                    await payload.member.add_roles(role)
                except Exception as e:
                    print(e)
                await payload.member.send(f'加入 {role} 身分組')
                print('Success')
        
    @commands.Cog.listener()      #按下表情符號加入身分組
    async def on_raw_reaction_remove(self,payload) -> None:  #表情符號偵測
    #移除貼圖移除身分組
        if payload.message_id == messageId:
            guild = self.bot.get_guild(payload.guild_id)  #取得guild
            if str(payload.emoji) == data["emoji1"]:
                print('Removing to test_role1...')
                user =  await guild.fetch_member(payload.user_id)  #取得guild 內 member
                role = guild.get_role(int(data["test_role1"]))  #取得guild 內 身分組
                try:
                    await user.remove_roles(role)
                except Exception as e:
                    print(e)
                await user.send(f'移除 {role} 身分組')
                print('Success')
            elif str(payload.emoji) == data["emoji2"]:
                print('Removing to test_role2...')
                user =  await guild.fetch_member(payload.user_id)  #取得guild 內 member
                role = guild.get_role(int(data["test_role2"]))  #取得guild 內 身分組
                try:
                    await user.remove_roles(role)
                except Exception as e:
                    print(e)
                await user.send(f'移除 {role} 身分組')
                print('Success')
    
    #訊息刪除
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        print("User：", msg.author," Message[",msg.content, "]was been delete on ",msg.channel, "channel.")
    
    @commands.Cog.listener()
    async def on_message_edit(before,after):
        after.delete()
        #print(after.content)
    #async def on_message_delete(slef,msg) -> None:      #只抓一筆資料   #抓取刪除訊息的人
    #    async for entry in msg.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
    #        await msg.channel.send(f'刪除者：{entry.user.name}')
    #        await msg.channel.send(f'訊息發送者：{msg.author}')
    #        await msg.channel.send(f'發送內容：{msg.content}')

async def setup(bot) -> None:
    await bot.add_cog(Event(bot))
