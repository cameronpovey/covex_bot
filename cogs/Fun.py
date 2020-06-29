import discord
import random
import os
import time
import giphy_client
import praw
from discord.ext import commands
from giphy_client.rest import ApiException
from discord import File


class Fun(commands.Cog):

    def __int__(self,client):
        self.client=client

    @commands.command(name='Meme',
                      description="Sends a meme straight from the 'hot' page of the meme subreddit.",
                      brief="Sends a random meme.",
                      aliases=['meme','m', 'Memes', 'memes', 'MEMES', 'givemememes', 'GIVEMEMEMES'])
    #finds random memes in hot
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id='ID',
                             client_secret='TOKEN',
                             user_agent='AGENT',
                             username='USERNAME')
        subreddit = reddit.subreddit('memes')
        memes = subreddit.hot(limit=300)
        listmeme = list(memes)
        meme = random.choice(listmeme)
        embed = discord.Embed(title=meme.title,
                              url=meme.url, colour=0x1973b3)
        embed.set_image(url=meme.url)
        await ctx.send(embed=embed)
        
    #finds random memes in new
    @commands.command(name='newmeme',
                      description="Sends a fresh meme from the 'new' page, these memes may not be great.",
                      brief="Sends a random meme.",
                      aliases=['NewMeme', 'nm', 'NM', 'newm', 'nmeme', 'nmemes'])
    async def newmeme(self, ctx):
        reddit = praw.Reddit(client_id='ID',
                             client_secret='TOKEN',
                             user_agent='AGENT',
                             username='USERNAME')
        subreddit = reddit.subreddit('memes')
        memes = subreddit.new(limit=100)
        listmeme = list(memes)
        meme = random.choice(listmeme)
        embed = discord.Embed(title=meme.title,
                              url=meme.url, colour=0x1973b3)
        embed.set_image(url=meme.url)
        await ctx.send(embed=embed)

    #8ball
    @commands.command(name='8ball',
                description="Answers all your yes or no questions.",
                brief="Answers all your yes or no questions.",
                aliases=['8-ball', 'eight_ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.',]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    #finds userdefined gif
    async def find_gif(self, query):
        try:
            giphy_token = 'TOKEN'
            api_instance = giphy_client.DefaultApi()
            response = api_instance.gifs_search_get(giphy_token, query, limit=50, rating='g')
            lst = list(response.data)
            gif = random.choices(lst)
            return gif[0].url
        
        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e
        
    @commands.command(description='Sends a random gif.',
                      brief='Sends a random gif.')
    async def gif(self, ctx, *, search):
        gif = await self.find_gif(search)
        await ctx.send(gif)

def setup(client):
    client.add_cog(Fun(client))
