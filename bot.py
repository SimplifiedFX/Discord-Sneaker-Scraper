from dataclasses import replace
from http import client
from sqlite3 import Timestamp
from urllib import response
import discord
from discord import app_commands
from discord.ext import commands
import requests
from discord.app_commands import Choice , MissingPermissions
import datetime
import urllib.parse
import json
from bs4 import BeautifulSoup
import time
import hmac
import hashlib
import math



MAX_VIEWS = 200
EBAY_VIEWER_CHANNEL_ID = 980138280911798282
invite_link = "https://discord.gg/JxSpEPRCtQ"


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or(
            '!'), intents=intents, help_command=None)

    async def on_ready(self):
        await tree.sync() 
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ExoTools"))
        print(f'Logged in as {self.user.name}')
        print(r"""


  _____                  _____                   _       
 | ____| __  __   ___   |_   _|   ___     ___   | |  ___ 
 |  _|   \ \/ /  / _ \    | |    / _ \   / _ \  | | / __|
 | |___   >  <  | (_) |   | |   | (_) | | (_) | | | \__ \
 |_____| /_/\_\  \___/    |_|    \___/   \___/  |_| |___/
        """)


bot = Bot()
tree = bot.tree






#fees
@tree.command(name="fees", description="Selling Platform Fees")
async def command_fees(interaction: discord.Interaction, price: str) -> None:
    price = float(price)
    paypal_price = price - (price*0.0267)
    klekt_price = price - (price*0.2) - 10
    goat_price = price - (price * 0.095) - 5
    stockx_level_1 = price - (price*0.13) - 5
    stockx_level_2 = price - (price*0.095) - 5
    stockx_level_3 = price - (price*0.09) - 5
    stockx_level_4 = price - (price*0.085) - 5
    stockx_level_5 = price - (price*0.08) - 5 

    em = discord.Embed(title="Fee Calculator",
                       description="```Value: "f'{price}€```', color=728634)
    em.add_field(name="PayPal", value=f"```{paypal_price}```", inline=True)
    em.add_field(name="Klekt", value=f"```{klekt_price}```", inline=True)
    em.add_field(name="Goat", value=f"```{goat_price}```", inline=True)
    em.add_field(name="StockX Level", inline=True, value="```\n Level 1 \n Level 2 \n Level 3 \n Level 4 \n Level 5 \n```"
    )
    em.add_field(name="Payout", inline=True, value=f'```\n{stockx_level_1}\n' f'{stockx_level_2}\n' f'{stockx_level_3}\n' f'{stockx_level_4}\n' f'{stockx_level_5} \n```'
    )
    em.set_footer(text="ExoTools",icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")


    await interaction.response.send_message(embed=em)

#sizes
@tree.command(name="sizechart", description="Sizechart")
async def command_sizechart(interaction: discord.Interaction) -> None:
    embed = discord.Embed(
        colour=	728634, title="Sizechart:"
    )
    embed.add_field(name="US GS:", value= "```\n3.5Y\n4Y\n4.5Y\n5Y\n5.5Y\n6Y\n6.5Y\n7Y\n```",inline=True)
    embed.add_field(name="EU GS:", value= "```\n35.5\n36\n36.5\n37.5\n38\n38.5\n39\n40\n```",inline=True)
    embed.add_field(name="\u200b", value= "\u200b",inline=True)
    embed.add_field(name="Woman US:", value= "```\n5\n5.5\n6\n6.5\n7\n7.5\n8\n8.5\n9\n9.5\n10\n10.5\n11\n11.5\n```", inline=True)
    embed.add_field(name="Men EU:", value= "```\n35.5\n36\n36.5\n37.5\n38\n38.5\n39\n40\n40.5\n41\n42\n42.5\n43\n44\n```", inline=True)
    embed.add_field(name="\u200b", value= "\u200b",inline=True)
    
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
    await interaction.user.send(embed=embed)

#suggestions
@tree.command(name="suggest", description="Make us a suggestion")
@app_commands.describe(suggestion="Make us a suggestion")
async def command_suggest(interaction: discord.Interaction, suggestion: str) -> None:
    value=suggestion

    embed = discord.Embed(
        colour=	728634, title="", description=f"**New Suggestion by {interaction.user.mention}**"
    )
    
    embed.add_field(name="Suggestion", value=value)
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
    await interaction.response.defer()
    msg = await interaction.followup.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@tree.command(name="dashboard", description="Link to our Dashboard")
async def command_dashboard(interaction: discord.Interaction,) -> None:
    embed = discord.Embed(
        colour=728634, title="Dashboard", description="Press the button to get the Dashboard-Link."
    )
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url= "https://exotools.hyper.co/", label="Link"))
    await interaction.response.send_message(embed=embed, view=view)

@tree.command(name="guide", description="Link to our Guide")
async def command_dashboard(interaction: discord.Interaction,) -> None:
    embed = discord.Embed(
        colour=728634, title="Guide", description="Press the button to get the Guide-Link."
    )
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url= "https://exotools.hyper.co/", label="Link"))
    await interaction.response.send_message(embed=embed, view=view)

@bot.listen()
async def on_message(message):
    if message.channel.id == 971498748222001174:
        await message.add_reaction("✅")

@tree.command(name="socials", description="Get our social media links")
async def command_dashboard(interaction: discord.Interaction,) -> None:
    embed = discord.Embed(
        colour=728634, title="Social Media", description="Here you can find our social media links."
    )
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url= "https://twitter.com/Exo_Tools", label="Twitter"))
    await interaction.response.send_message(embed=embed, view=view)

@tree.command(name="snipes", description="Sizepids und Stocknumbers")
@app_commands.describe(pid = "Enter a PID of a Snipes product")
async def new_command_snipes(interaction: discord.Interaction, pid: str):
        headers= {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

        url = "https://snipes.com/p/" + pid + ".html"

        link = f"https://www.snipes.com/s/snse-DE-AT/dw/shop/v19_5/products/({pid}00000001,{pid}00000002,{pid}00000003,{pid}00000004,{pid}00000005,{pid}00000006,{pid}00000007,{pid}00000008,{pid}00000009)?client_id=cf212f59-94d1-4314-996f-7a11871156f4&locale=de-DE&expand=availability,+prices"
        s = requests.Session()          
        r = s.get(url=link, headers=headers)
        output=json.loads(r.text)
        products=output['data']

        sizes = []
        stocks = []
        size_pids = []

        stock_counter=0



        for i in products:
         product_name = i['name']
         size_pid = i['id']
         stock = i['inventory']['stock_level']
         real_sku = i['c_akeneo_wwsmanufactureno']
         color = i['c_color']
         date = i['valid_from']['default']
         
         
         size = i['c_size']

         unit = f"{size}"
         unit2 = f"{size_pid}"
         unit3 = f"{stock}"
         sizes.append(unit)
         size_pids.append(unit2)
         stocks.append(unit3)

         stock_counter=stock_counter + stock

        release_link = f"https://www.snipes.com/p/00013801899574.html?chosen=size&dwvar_" + pid + "_size=40&format=ajax" 

        release_date = s.get(url=release_link, headers=headers).json()
        price = release_date['product']['price']['sales']['formatted']        
        
        image_pid = pid.split('0001380')[1]
        imageurl = "https://www.snipes.com/dw/image/v2/BDCB_PRD/on/demandware.static/-/Sites-snse-master-eu/default/dw10fc3cac/" + image_pid + "_P.jpg?sw=780&sh=780&sm=fit&sfrm=png"


        stockx_url = "https://stockx.com/search?s="+ urllib.parse.quote(real_sku)
        goat_url = "https://www.goat.com/search?query="+ urllib.parse.quote(real_sku)

        embed = discord.Embed(
            color = 728634, title=f"{product_name} {color}", url=f"{url}", description=f"**Release:\n**```{date}```"
        )
        embed.set_thumbnail(url=imageurl)
                

        embed.add_field(name="Price", value=f"```{price}```", inline=True)
        embed.add_field(name="PID", value=f"```{pid}```", inline=True)
        embed.add_field(name="Total Stock", value= f"```{stock_counter}```",inline=True)
        sizes = "\n".join(sizes)
        size_pids = "\n".join(size_pids)
        stocks = "\n".join(stocks)
        embed.add_field(name="Size", value=f"```\n{sizes}```", inline=True)
        embed.add_field(name="Size PID", value=f"```\n{size_pids}```", inline=True)
        embed.add_field(name="Stock", value=f"```\n{stocks}```", inline=True)
        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/992436428871061605/exotools_pp.png")

        view = discord.ui.View()
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=stockx_url , label="StockX"))
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=goat_url , label="GOAT"))
        await interaction.response.send_message(embed=embed, view=view)

@tree.command(name="footlocker", description="Sizepids and Stock")
@app_commands.describe(sku = "Enter SKU of a Footlocker product", region = "Enter a region")
@app_commands.choices(region=[Choice(name= "Germany", value="DE"),Choice(name= "United Kingdom", value="UK"),Choice(name= "France", value="FR"),Choice(name= "Belgium", value="BE"), Choice(name= "Italy", value="IT"),Choice(name= "Netherlands", value="NL"),Choice(name= "Poland", value="PL"),Choice(name= "Spain ", value="ES")])
async def new_command_footlocker(interaction: discord.Interaction, sku: str, region: str):
        headers= {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }



        url = "https://www.footlocker."+region+"/api/products/pdp/"+sku
        product_url = "https://www.footlocker."+region+"/en/product/~/"+sku+".html"

        image_url = "https://images.footlocker.com/is/image/FLEU/"+sku+"_01?wid=500&hei=500&fmt=png-alpha"
        s = requests.Session()
        output = s.get(url=url, headers=headers).json()


        sizes = []
        sizeSkus = []
        stocks = []
        

        price = output["sellableUnits"][0]["price"]["value"]
        product_name = output['name']
        for output in output["sellableUnits"]:
            size = output["attributes"][0]["value"]
            sizeSku = output["sku"]
            stock = output["stockLevelStatus"]
            if 'inStock' in stock:
             stock='TRUE'
            else:
             stock='FALSE'
            unit = f"{size}"
            unit2 = f"{sizeSku}"
            unit3 = f"{stock}"
            sizes.append(unit)
            sizeSkus.append(unit2)
            stocks.append(unit3)

            

        
        AT = "https://www.footlocker.at/en/product/~/"+ sku +".html"
        BE = "https://www.footlocker.be/en/product/~/"+ sku +".html"
        CZ = "https://www.footlocker.cz/en/product/~/"+ sku +".html"
        DK = "https://www.footlocker.dk/en/product/~/"+ sku +".html"
        FR = "https://www.footlocker.fr/en/product/~/"+ sku +".html"
        DE = "https://www.footlocker.de/en/product/~/"+ sku +".html"
        GR = "https://www.footlocker.gr/en/product/~/"+ sku +".html"
        HU = "https://www.footlocker.hu/en/product/~/"+ sku +".html"
        IE = "https://www.footlocker.ie/en/product/~/"+ sku +".html"
        IT = "https://www.footlocker.it/en/product/~/"+ sku +".html"
        LU = "https://www.footlocker.lu/en/product/~/"+ sku +".html"
        NL = "https://www.footlocker.nl/en/product/~/"+ sku +".html"
        NO = "https://www.footlocker.no/en/product/~/"+ sku +".html"
        PL = "https://www.footlocker.pl/en/product/~/"+ sku +".html"
        PT = "https://www.footlocker.pt/en/product/~/"+ sku +".html"
        ES = "https://www.footlocker.es/en/product/~/"+ sku +".html"
        SW = "https://www.footlocker.se/en/product/~/"+ sku +".html"
        GB = "https://www.footlocker.co.uk/en/product/~/"+ sku +".html"


        
        
    


        
        #color
        #sizeskus
        #stockx, goat

        stockx_url = "https://stockx.com/search?s="+ urllib.parse.quote(product_name)
        goat_url = "https://www.goat.com/search?query="+ urllib.parse.quote(product_name)
        
        
        embed = discord.Embed(color = 728634, title = product_name, url = product_url, description = f"\n")
        embed.set_thumbnail(url = image_url)
        embed.add_field(name = "Region", value = f'```{region}```', inline = True)
        embed.add_field(name = "SKU", value = f"```{sku}```", inline = True)
        embed.add_field(name = "Price", value = f"```{price}€```", inline = True)
        sizes = "\n".join(sizes)
        sizeSkus = "\n".join(sizeSkus)
        stocks = "\n".join(stocks)

        embed.add_field(name = "Sizes", value = f'```{sizes}```', inline = True)
        embed.add_field(name = "Size-SKUs", value = f'```{sizeSkus}```', inline = True)
        embed.add_field(name = "Stock", value = f'```{stocks}```', inline = True)
        embed.add_field(name = "Important Regions", value = f"[DE]({DE})", inline = True)
        embed.timestamp = datetime.datetime.now()

        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/992436428871061605/exotools_pp.png")

        view = discord.ui.View()
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=stockx_url , label="StockX"))
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=goat_url , label="GOAT"))
        await interaction.response.send_message(embed=embed, view=view)


@tree.command(name="sidestep", description="Sizepids and Stock")
@app_commands.describe(sku = "Enter SKU of a Footlocker product", region = "Enter a region")
@app_commands.choices(region=[Choice(name= "Germany", value="DE"),Choice(name= "United Kingdom", value="UK"),Choice(name= "France", value="FR"),Choice(name= "Belgium", value="BE"), Choice(name= "Italy", value="IT"),Choice(name= "Netherlands", value="NL"),Choice(name= "Poland", value="PL"),Choice(name= "Spain ", value="ES")])
async def new_command_footlocker(interaction: discord.Interaction, sku: str, region: str):
        headers= {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

        url = "https://www.sidestepstore."+region+"/api/products/pdp/"+sku
        product_url = "https://www.sidestepstore."+region+"/en/product/~/"+sku+".html"


        image_url = "https://images.footlocker.com/is/image/FLEU/"+sku+"_01?wid=500&hei=500&fmt=png-alpha"
        s = requests.Session()
        output = s.get(url=url, headers=headers).json()


        sizes = []
        sizeSkus = []
        stocks = []

        

        price = output["sellableUnits"][0]["price"]["value"]
        product_name = output['name']
        for output in output["sellableUnits"]:
            size = output["attributes"][0]["value"]
            sizeSku = output["sku"]
            stock = output["stockLevelStatus"]
            if 'inStock' in stock:
             stock='TRUE'
            else:
             stock='FALSE'
            unit = f"{size}"
            unit2 = f"{sizeSku}"
            unit3 = f"{stock}"
            sizes.append(unit)
            sizeSkus.append(unit2)
            stocks.append(unit3)

            


            

        
        AT = "https://www.sidestepstore.at/en/product/~/"+ sku +".html"
        BE = "https://www.sidestepstore.be/en/product/~/"+ sku +".html"
        CZ = "https://www.sidestepstore.cz/en/product/~/"+ sku +".html"
        DK = "https://www.sidestepstore.dk/en/product/~/"+ sku +".html"
        FR = "https://www.sidestepstore.fr/en/product/~/"+ sku +".html"
        DE = "https://www.sidestepstore.de/en/product/~/"+ sku +".html"
        GR = "https://www.sidestepstore.gr/en/product/~/"+ sku +".html"
        HU = "https://www.sidestepstore.hu/en/product/~/"+ sku +".html"
        IE = "https://www.sidestepstore.ie/en/product/~/"+ sku +".html"
        IT = "https://www.sidestepstore.it/en/product/~/"+ sku +".html"
        LU = "https://www.sidestepstore.lu/en/product/~/"+ sku +".html"
        NL = "https://www.sidestepstore.nl/en/product/~/"+ sku +".html"
        NO = "https://www.sidestepstore.no/en/product/~/"+ sku +".html"
        PL = "https://www.sidestepstore.pl/en/product/~/"+ sku +".html"
        PT = "https://www.sidestepstore.pt/en/product/~/"+ sku +".html"
        ES = "https://www.sidestepstore.es/en/product/~/"+ sku +".html"
        SW = "https://www.sidestepstore.se/en/product/~/"+ sku +".html"
        GB = "https://www.sidestepstore.co.uk/en/product/~/"+ sku +".html"



        
        
    


        
        #color
        #sizeskus
        #stockx, goat

        stockx_url = "https://stockx.com/search?s="+ urllib.parse.quote(product_name)
        goat_url = "https://www.goat.com/search?query="+ urllib.parse.quote(product_name)
        
        
        embed = discord.Embed(color = 728634, title = product_name, url = product_url, description = f"\n")
        embed.set_thumbnail(url = image_url)
        embed.add_field(name = "Region", value = f'```{region}```', inline = True)
        embed.add_field(name = "SKU", value = f"```{sku}```", inline = True)
        embed.add_field(name = "Price", value = f"```{price}€```", inline = True)
        sizes = "\n".join(sizes)
        sizeSkus = "\n".join(sizeSkus)
        stocks = "\n".join(stocks)

        embed.add_field(name = "Sizes", value = f'```{sizes}```', inline = True)
        embed.add_field(name = "Size-SKUs", value = f'```{sizeSkus}```', inline = True)
        embed.add_field(name = "Stock", value = f'```{stocks}```', inline = True)
        embed.add_field(name = "Important Regions", value = f"[DE]({DE})", inline = True)
        embed.timestamp = datetime.datetime.now()

        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/992436428871061605/exotools_pp.png")

        view = discord.ui.View()
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=stockx_url , label="StockX"))
        view.add_item(discord.ui.Button(style = discord.ButtonStyle.url, url=goat_url , label="GOAT"))
        await interaction.response.send_message(embed=embed, view=view)


@tree.command(name="shopify-check", description="Gives you the information if a store is a shopify store")
@app_commands.describe(url = "Enter the url of the store")
async def new_command_footlocker(interaction: discord.Interaction, url: str):
        headers= {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

        s = requests.Session()
        check_url = url + "/products.json"
        response = s.get(url=check_url, headers=headers)
        r = response.status_code

        embed = discord.Embed(color=728634, title="Shopify-Checker", description="\n")
        embed.add_field(name="URL", value=f"```{url}```", inline=True)
        embed.add_field(name="Result", value="``` ✅```", inline=True)
        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
        
        em = discord.Embed(color=728634, title="Is Not Shopify", description=f"{url} is a not Shopify Store")
        em = discord.Embed(color=728634, title="Shopify-Checker", description="\n")
        em.add_field(name="URL", value=f"```{url}```", inline=True)
        em.add_field(name="Result", value="```❌```", inline=True)
        em.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")
        
        
        if r == 200:
            await interaction.response.send_message(embed=embed)
        elif r == 404:
            await interaction.response.send_message(embed=em)


@tree.command(name="asphaltgold", description="Stock, Sizes and Size-Skus of any product")
@app_commands.describe(url = "Enter the url of the product.")
async def new_command_asphaltgold(interaction: discord.Interaction, url: str):

    s = requests.Session()
    html=s.get(url=url)

    soup=BeautifulSoup(html.content,'html.parser')

    varients=soup.find('script',{'data-product':'last-seen'}).text
    json_variants=json.loads(varients)
    image=json_variants['featured_image']
    j_variants=json_variants['variants']
    name= json_variants['title']

    image_url = "https:"+image

    stocks =[]
    sizes =[]
    skus = []

    stock_counter=0

    for v in j_variants:
        
        size = v['option1']
        sku= v['id']
        price=v['price']
        final_price=price/100
        stock=v['inventory_quantity']
        if stock <0: 
         stock = stock *-1

        
        unit1 = f"{stock}"
        unit2 = f"{sku}"
        unit3 = f"{size}"
        stocks.append(unit1)
        
        
        skus.append(unit2)
        
        
        sizes.append(unit3)

        stock_counter=stock_counter + stock



    
 
        
    


    embed=discord.Embed(color=728634,title=name, url=url)
    embed.set_thumbnail(url=image_url)
    sizes = "\n".join(sizes)
    stocks = "\n".join(stocks)
    skus = "\n".join(skus)
    embed.add_field(name='Price', value=f"```{final_price}€```", inline=True)
    embed.add_field(name='Total Stock', value=f"```{stock_counter}```", inline=True)
    embed.add_field(name='\u200b', value="\u200b", inline=True)
    embed.add_field(name='Sizes', value=f"```{sizes}```", inline=True)
    embed.add_field(name='Size-Skus', value=f"```{skus}```", inline=True)
    embed.add_field(name='Stock', value=f"```{stocks}```", inline=True)
    embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")


    await interaction.response.send_message(embed=embed)




@tree.command(name="adidas", description="Stock, Sizes and Size-Skus of any product")
@app_commands.describe(sku = "Enter the sku of the product." , region = "Select a region.")
@app_commands.choices(region=[Choice(name= "Germany", value="DE"),Choice(name= "Australia", value="com.au")])
async def new_command_adidas(interaction: discord.Interaction, sku: str, region: str):
        headers={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        }


        sizes = []
        stocks = []
        skus = []

        
        s = requests.Session()
        url = 'https://www.adidas.'+region+'/api/products/'+sku+'/availability'
        product_url='https://www.adidas.'+region+'/'+sku+'.html'
        output = s.get(url=url, headers=headers).json()
        output2  = s.get(url=product_url, headers=headers)
        
        
        soup=BeautifulSoup(output2.content,'html.parser')
        name=soup.find('h1',{'class':'gl-heading gl-heading--regular gl-heading--italic name___1EbZs'}).text
        price = soup.find('div',{'class':'product-price___gJhOl'}).text
        image = soup.find('link',{'id':'pdp-hero-image'})['href']

        infos=output['variation_list']

        stock_counter=0

        for item in infos:
            size_skus=item['sku']
            size = item['size']
            stock = item['availability']

            stock_counter=stock_counter + stock
            
            
            unit = f"{size}"
            unit2 = f"{size_skus}"
            unit3 = f"{stock}"
            sizes.append(unit)
            skus.append(unit2)
            stocks.append(unit3)

            


        embed = discord.Embed(color = 728634, title = name, url = product_url)
        embed.set_thumbnail(url=image)
        embed.add_field(name = "SKU", value = f"```{sku}```", inline = True)
        embed.add_field(name = "Price", value = f"```{price}```", inline = True)
        embed.add_field(name = "Total Stock", value = f"```At least {stock_counter}```", inline = True)
        sizes = "\n".join(sizes)
        skus = "\n".join(skus)
        stocks = "\n".join(stocks)
        embed.add_field(name = "Sizes", value = f'```\n{sizes}```', inline = True)
        embed.add_field(name = "Size-SKUs", value = f'```\n{skus}```', inline = True)
        embed.add_field(name = "Stock", value = f'```\n{stocks}```', inline = True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/992436428871061605/exotools_pp.png")
        await interaction.response.send_message(embed=embed)

@tree.command(name="zalando", description="Zalando Pids and Stock")
@app_commands.describe(url = "Enter the url of the product.")
async def command_zalando(interaction: discord.Interaction , url: str) -> None:
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    
    s = requests.Session()
    html = s.get(url=url, headers=headers)

    soup = BeautifulSoup(html.content, 'html.parser')

    products_info = soup.find('script', {'class': 're-1-12'}).text

    product_json = json.loads(products_info)
    
    id = url.split('/')[3].removesuffix(".html")

    all_skus = product_json['graphqlCache']['{\"id\":\"752e19d21ed6235098581c9b17164f7171520bd790bef1c9538268831f7ebef0\",\"variables\":{\"id\":\"ern:product:uri:'+ id +'\"}}']['data']['context']['simples']
    
    sizes=[]
    skus=[]
    stocks=[]

    if '.de' in url:
        region = 'DE'

    
    

    for i in all_skus:
        size_skus = i['sku']
        size = i['size']
        stock = i['offer']['stock']['quantity']
        if 'OUT_OF_STOCK' in stock:
         stock='OOS'
        unit = f"{size}"
        unit2 = f"{size_skus}"
        unit3 = f"{stock}"
        sizes.append(unit)
        skus.append(unit2)
        stocks.append(unit3)

    name = soup.find('span',{'class':'EKabf7 R_QwOV'}).text
    price = soup.find('p',{'class':'RYghuO uqkIZw FxZV-M pVrzNP'}).text
    color = soup.find('p',{'class':'RYghuO u-6V88 dgII7d pVrzNP zN9KaA'}).text
    image = soup.find('img', {'class':'RYghuO u-6V88 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy'})['src']
    
    

    

    embed = discord.Embed(title=name, url=url, description=f'```{region}```')
    embed.set_thumbnail(url=image)
    sizes = "\n".join(sizes)
    skus = "\n".join(skus)
    stocks = "\n".join(stocks)
    embed.add_field(name="Price", value=f'```{price}```', inline=True)
    embed.add_field(name="Color", value=f'```{color}```', inline=True)
    embed.add_field(name="Region", value=f'```{region}```', inline=True)
    embed.add_field(name="Sizes", value=f'```{sizes}```', inline=True)
    embed.add_field(name="Sizes-SKUs", value=f'```{skus}```', inline=True)
    embed.add_field(name="Stock", value=f'```{stocks}```', inline=True)




    await interaction.response.send_message(embed=embed)

@tree.command(name="luisaviaroma", description="Stock and Sizes  of any product. Must be available")
@app_commands.describe(sku = "Enter the sku of the product." , gender = "Select a Gender.")
@app_commands.choices(gender=[Choice(name="Men", value=1),Choice(name="Women", value=2)])
async def command_luisaviaroma(interaction: discord.Interaction, sku: str, gender: Choice[int]) -> None:
    key = bytes([142, 167, 155, 206, 195, 213, 69, 151, 239, 225, 134, 120, 10, 131, 92, 7, 84, 0, 98, 58, 17, 72, 29, 61, 23, 221, 146, 233, 5, 219, 182, 21])

    timeInMs = time.time() * 1000

    startTime = math.floor((timeInMs - 300000) / 1000)
    endTime = math.floor((timeInMs + 1800000) / 1000)

    data = f'st={startTime}~exp={endTime}~acl=*'
    hmac_token = hmac.new(key, bytes(data, 'utf-8'), digestmod=hashlib.sha256).hexdigest()

    token = f'{data}~hmac={hmac_token}'
    headers = {
    "__lvr_mobile_api_token__":f"{token}",
    "user-agent":"LVR/2.1.9 (iPhone; iOS 15.6.1)",
    "authtoken":"JFjs8bR2vnQDW1PZxHxaIpjino1IFB9k9WSoslEySOMU2w09TgQm6NCExiOxWxNDvicRHl0ofLSfEZ3/P3nA/cGAp1XvmHi2SIHINbsoLBykniBkmOo4mogTruDyiwAfOKVNI/fFHDNEVdVuR9lZE5eRUCp6lXer5pcvSGIEJoOvDsn5mst/G2EurVNlPn5ydroCyu1OFTuz9KJWCiec3b1rqY42PqRZxxVfwTR/+1kpG976QW71xXEz/Vy1Ny7JH+eY27qVhkvdYfO/gF1rmJ7amTbqbzIHbu2UgA8aghwHCl3FMzufv4dfMI73cXa/34jz9LjI/ilitveZJ3XXkg6DeFIpGEn22J4cMJ+oAto=|u=7PMravXeHDKxIyxSomR5eQ=="
    }
    r_url = "https://www.luisaviaroma.com/"+sku
    isku = sku[-3:]
    msku = sku[0:-7]
    csku = sku[4:-3]
    
    if gender.value == 1:
        M_url = f"https://api.luisaviaroma.com/lvrapprk/public/v1/itemminimal?CollectionId={csku}&GenderMemo=men&ItemCode={sku}&ItemId={isku}&SeasonId={msku}&SeasonMemo=actual&Language=EN&Country=DE&CurrencyView=EUR&CurrencyFatt=EUR&App=true&format=json"
        s = requests.Session()
        response = s.get(url=M_url, headers=headers).json()

        sizes = []
        stocks = []

        name =response['DescriptionText']
        genders = response['BreadcrumbCategoryParameters']['Gender']
        if 'men' in genders:
         genders = '(M)'
        price = response['ItemCodeDetails'][sku]['InvoiceFinalPriceValue']
        infos=response['AvailabilityByColor'][0]['SizeAvailability']

        stock_counter=0

        for i in infos:
            
            color = i['ComColorDescription']
            size = i['SizeValue']
            stock = i['QuantitiesTotal']['Available']
            stock_counter=stock_counter + stock
            unit = f"{size}"
            unit3 = f"{stock}"
            sizes.append(unit)
            stocks.append(unit3)
        
        
        
        

        sizes = "\n".join(sizes)
        stocks = "\n".join(stocks)
        embed = discord.Embed(title=f"{name} {genders}", url=r_url, description=f'```{sku}```',color = 728634)
              
        embed.add_field(name= "Price", value=f'```{price}€```', inline=True) 
        embed.add_field(name= "Region", value=f'```DE```', inline=True) 
        embed.add_field(name= "Total Stock", value=f'```{stock_counter}```', inline=True)
        embed.add_field(name = "UK Sizes", value = f'```\n{sizes}```', inline=True)
        embed.add_field(name = "Stock", value=f'```\n{stocks}```', inline=True)
        

        await interaction.response.send_message(embed=embed)

    elif gender.value == 2:
        W_url = f"https://api.luisaviaroma.com/lvrapprk/public/v1/itemminimal?CollectionId={csku}&GenderMemo=women&ItemCode={sku}&ItemId={isku}&SeasonId={msku}&SeasonMemo=actual&Language=EN&Country=DE&CurrencyView=EUR&CurrencyFatt=EUR&App=true&format=json"
        s = requests.Session()
        response = s.get(url=W_url, headers=headers).json()

        sizes = []
        stocks = []
        name =response['DescriptionText']
        genders = response['BreadcrumbCategoryParameters']['Gender']
        if 'women' in genders:
         genders = '(W)'
        price = response['ItemCodeDetails'][sku]['InvoiceFinalPriceValue']
        infos=response['AvailabilityByColor'][0]['SizeAvailability']

        stock_counter=0

        for i in infos:
            
            color = i['ComColorDescription']
            size = i['SizeValue']
            stock = i['QuantitiesTotal']['Available']
            stock_counter=stock_counter + stock
            
            
            unit = f"{size}"
            unit3 = f"{stock}"
            sizes.append(unit)
            stocks.append(unit3)

        image = response['PhotosByColor']['228451|700'][1]
        
        image_url = "https://images.lvrcdn.com/"+"Big"+image
        
        
        


  
        embed = discord.Embed(title=f"{name} {genders}", url=r_url, description=f'```{sku}```',color = 728634)
        
        
        sizes = "\n".join(sizes)
        stocks = "\n".join(stocks)
        embed.set_thumbnail(url=image_url)
        embed.add_field(name= "Price", value=f'```{price}€```', inline=True) 
        embed.add_field(name= "Region", value=f'```DE```', inline=True) 
        embed.add_field(name= "Total Stock", value=f'```{stock_counter}```', inline=True)
        embed.add_field(name = "UK Sizes", value = f'```\n{sizes}```', inline=True)
        embed.add_field(name = "Stock", value=f'```\n{stocks}```', inline=True)
        

        

        await interaction.response.send_message(embed=embed)

@tree.command(name="nike-snkrs", description="Release Webhook")
@app_commands.choices(site=[Choice(name="NIKE", value=1),Choice(name="SNKRS", value=2)])
async def new_command_release(interaction: discord.Interaction,site: Choice[int],sku: str,release: str, resell: str):
    headers= {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,de;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }



    url = f"https://api.nike.com/product_feed/threads/v2?filter=language(de)&filter=marketplace(DE)&filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.styleColor({sku})"
    stockx_url = "https://stockx.com/search?s="+ urllib.parse.quote(sku)
    goat_url = "https://www.goat.com/search?query="+ urllib.parse.quote(sku)


    s = requests.Session()
    r = s.get(url=url, headers=headers)

    output=json.loads(r.text)

    sizes =[]
    stocks = []
    
    sizelist = r.json()['objects'][0]["productInfo"][0]["skus"]
    for size in sizelist:
     ussize = (size["nikeSize"])
     eusize = (size["countrySpecifications"][0]["localizedSize"])

     unit = f"{eusize}"
     sizes.append(unit)



    stocklist = r.json()['objects'][0]["productInfo"][0]["availableSkus"]
    
    for stock in stocklist:
     level = (stock["level"])
     unit1 = f"{level}"
     stocks.append(unit1)
    
    
    
    products = output['objects']
    
    for i in products:
     product_info = i['publishedContent']['properties']['productCard']
     image_url = product_info['properties']['squarishURL']
     
     

     products_infoss = i['productInfo'][0]

     names = products_infoss['productContent']['title']
     slug = products_infoss['productContent']['slug']
     price = products_infoss["merchPrice"]["currentPrice"]

     
    

    
    
    


    if site.value == 1:
        embed = discord.Embed(title=names,url=f"https://www.nike.com/de/t/{slug}", description=f'**SKU**\n```{sku}```\n**Release Date**\n ```29.05.22```')
        embed.set_thumbnail(url=image_url)
        embed.add_field(name="Price", value=f'```{price}€```', inline=True)
        embed.add_field(name="Release Method", value=f'```asdasd```', inline=True)
        embed.add_field(name="Exclusive Access", value=f'```TRUE```', inline=True)
        sizes = "\n".join(sizes)
        stocks = "\n".join(stocks)
        embed.add_field(name="Sizes", value=f'```{sizes}```', inline=True)    
        embed.add_field(name='Stock', value=f"```{stocks}```", inline=True)
        embed.add_field(name='🔗 | Links:', value=f"[StockX]({stockx_url}) • [GOAT]({goat_url})", inline=False)
        embed.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")

   

        await interaction.channel.send(embed=embed)
    elif site.value == 2:
        embed1=discord.Embed(color=728634,title=names, url=f"https://www.nike.com/de/launch/t/{slug}",description=f'**SKU**\n```{sku}```\n**Release Date**\n ```29.05.22```')
        embed1.set_thumbnail(url=image_url)
        embed1.set_thumbnail(url=image_url)
        embed1.add_field(name="Price", value=f'```{price}€```', inline=True)
        embed1.add_field(name="Release Method", value=f'```asdasd```', inline=True)
        embed1.add_field(name="Exclusive Access", value=f'```TRUE```', inline=True)
        sizes = "\n".join(sizes)
        stocks = "\n".join(stocks)
        embed1.add_field(name="Sizes", value=f'```{sizes}```', inline=True)    
        embed1.add_field(name='Stock', value=f"```{stocks}```", inline=True)
        
        embed1.add_field(name='🔗 | Links:', value=f"[StockX]({stockx_url}) • [GOAT]({goat_url})", inline=False)
        embed1.set_footer(text="ExoTools", icon_url="https://cdn.discordapp.com/attachments/973630172899201054/994586940223528990/exotools_pprund.png")

        

        
        await interaction.channel.send(embeds=[embed1])
    
    


bot.run("place token here")
