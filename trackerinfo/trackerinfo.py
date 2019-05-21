from redbot.core import commands
import discord

import aiohttp

class Trackerinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def ptp(self, ctx):
        """gets info on ptp"""
        async with self.session.get("https://ptp.trackerstatus.info/api/status/") as r:
            data = await r.json()
        color = await ctx.embed_color()
        website = data["Website"]
        irc = data["IRC"]
        ircannounce = data["IRCTorrentAnnouncer"]
        embed = discord.Embed(description="Status of PTP tracker", color=color)
        embed.set_image(url="https://ptp.trackerstatus.info/images/logo.png")
        embed.add_field(name="Website", value="{}".format(website))
        embed.add_field(name="IRC", value="{}".format(irc))
        embed.add_field(name="IRC Torrent Announcer", value="{}".format(ircannounce))
        embed.set_footer(text="0 means down and 1 means up")
        
        await ctx.send(embed=embed)