import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def slots(ctx):
    """🎰 Simple emoji slot machine"""
    emojis = ["🍒", "🍋", "🍉", "🍀", "💎"]
    spinning_message = await ctx.send("🎰 Spinning the slot machine...")

    # Simulate spinning animation
    for _ in range(3):
        slots = [random.choice(emojis) for _ in range(3)]
        await spinning_message.edit(content=f"🎰 | {' | '.join(slots)} |")
        await asyncio.sleep(0.8)

    # Final result
    result = [random.choice(emojis) for _ in range(3)]
    await spinning_message.edit(content=f"🎰 **Final Result:** | {' | '.join(result)} |")

    # Check for matches
    if result[0] == result[1] == result[2]:
        await ctx.send(f"💎 JACKPOT! {ctx.author.mention} won big! 🎉")
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        await ctx.send(f"😊 Nice! {ctx.author.mention} got a small win!")
    else:
        await ctx.send(f"😢 No luck this time, {ctx.author.mention}!")

bot.run("MTQzMjEyMTQwOTI0MDU2ODA4Mw.GSmJgc.f-762DoYUnlJxr54epmqLdA-ESoCjZl  6M7GPDo")
