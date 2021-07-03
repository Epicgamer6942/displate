import discord
from discord import message
from discord import guild
from discord.ext import commands
import random
import os

from discord.member import Member

class mod(commands.Cog):
    def __init__(self, client):
        self.client=client
#error handler
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(f'{ctx.author.mention} you dont have the required permissions try again.',delete_after=10)
            await ctx.message.delete()
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} you have not input all the required arguement.\nTry again.',delete_after=10)
            await ctx.message.delete()

#kick
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def kick(self, ctx, member:discord.Member,* ,reason=None):
        await member.kick(reason=reason)
        channel=self.get_channel(734312251917467742)
        await channel.send(f'{member} has been kicked for {reason}')
#ban
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member,* ,reason=None):
        await member.ban(reason=reason)
        channel=self.get_channel(734312251917467742)
        await channel.send (f'{member} has been banned for {reason}')
#muted
    @commands.command()
    async def muted(self,ctx, member: discord.Member, *, reason=None):
        guild=self.guild
        mrole=discord.utils.get(guild.roles,name="Muted")
        if not mrole:
            mrole=await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mrole,speak=False, send_messages=False,read_message_history=True,read_messages=False)
        await member.add_roles(mrole,reason=reason)
        await ctx.send(f'Muted {member.mention} for {reason}')
        await member.send(f'You were muted in the server {guild.name} for {reason} pls avoid doing this in the future.\nThank you')
#unmuted
    @commands.command()
    async def unmuted(self,ctx, member: discord.Member, *, reason=None):
        guild=self.guild
        mrole=discord.utils.get(guild.roles,name="Muted")
        await member.remove_roles(mrole,reason=reason)
        await ctx.send(f'Unmuted {member.mention} for {reason}')
        await member.send(f'You were unmuted in the server {guild.name} for {reason} pls avoid doing this in the future.\nThank you')





def setup(client):
    client.add_cog(mod(client))
