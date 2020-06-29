import discord
import time
from discord.ext import commands


class Tools(commands.Cog):

    def __int__(self,client):
        self.client=client

    @commands.command(name='Clear',
                      description='Clears the chat, usage: -clear (num), only available with the manage messages permission.',
                      brief='Clears the chat.',
                      aliases=['clear', 'clean', 'purge', 'wipe'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @commands.command(name='Avatar',
                      description='See anyones full resolution discord photo just @ them.',
                      brief='See profile pictures at max res.',
                      aliases=['pp', 'profilepicture', 'profile_picture', 'avatar'])
    async def avatar(self, ctx, member: discord.Member):
        await ctx.send('{}'.format(member.avatar_url))

    @commands.command(name='Stats',
                      description='Get a stats page for anyone you @.',
                      brief='User Stats.',
                      aliases=['stats', 'stat', 'userstats', 'user_stats', 'info'])
    async def user_stats(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(Color=member.top_role.color)

        embed.set_author(name="User info:")

        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name="ID:", value=member.id)

        embed.add_field(name="User name:", value=member.display_name)

        embed.add_field(name="Account created:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p"))

        embed.add_field(name="Joined server at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p"))

        embed.add_field(name=f"Server Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Tools(client))
