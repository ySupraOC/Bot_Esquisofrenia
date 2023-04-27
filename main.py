from typing import Optional
import discord
import json
from discord.ext import commands
from discord import app_commands

MY_GUILD = discord.Object(id=1081377819864596571)

with open("config.json") as e:
    config = json.load(e)
    TOKEN = config["token"]

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = commands.Bot(command_prefix=".", intents = discord.Intents.all())
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


# Comando Hello
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """..."""
    await interaction.response.send_message(f'Olá, {interaction.user.mention} Bem vindo ao Clube da Progamação', ephemeral=True)


# Comando Rules
@client.tree.command()
async def rules(interaction: discord.Interaction):
    """..."""

    embed = discord.Embed(
        title = "***REGRAS***",
        description = '**Bem vindo(a) ao Clube, mais antes de começar a usar tem que saber as regras para uma conversa amigavel :P**',
        colour = 16777215
    )
    #Regra 01
    embed.add_field(name= "**-> 01**", value= "```É proibida a marcação exagerada de cargos ou membros.```", inline= False)

    #Regra 02
    embed.add_field(name= "**-> 02**", value= "```Respeito e educação são fundamentais: Os membros do servidor devem se tratar com respeito e educação. Discriminação, racismo, sexismo, homofobia e qualquer forma de intolerância não serão tolerados.```", inline= False)

    #Regra 03
    embed.add_field(name= "**-> 03**", value= "```Mantenha o foco: O servidor é destinado à programação e discussões relacionadas. Evite desviar o assunto ou enviar mensagens que não estão relacionadas ao tema do servidor.```", inline= False)

    #Regra 04
    embed.add_field(name= "**-> 04**", value= "```Utilize os chats com suas devidas funções.```", inline= False)

    #Regra 05
    embed.add_field(name= "**-> 05**", value= "```Não publique conteúdo inapropriado: É proibido postar conteúdo sexual explícito, violento, assédio ou qualquer outro tipo de material que possa ofender ou incomodar os membros.```", inline= False)

    #Regra 06
    embed.add_field(name= "**-> 06**", value= "```Ajude os outros membros: Se você é experiente em programação, ajude os membros que precisam de ajuda e compartilhe seus conhecimentos. Se você é um iniciante, não hesite em pedir ajuda.```", inline= False)

    #Regra 07
    embed.add_field(name= "**-> 07**", value= "```Não seja tóxico: Não seja negativo, ofensivo ou desrespeitoso em relação às ideias ou opiniões dos outros membros. Se você discorda de algo, expresse sua opinião de maneira respeitosa e construtiva.```", inline= False)

    #Regra 08
    embed.add_field(name= "**-> 08**", value= "```Evite spam e autopromoção: Não envie mensagens repetidas, links desnecessários ou faça autopromoção excessiva. Se você deseja compartilhar algo, certifique-se de que seja relevante e útil para os membros do servidor.```", inline= False)

    #Regra 09
    embed.add_field(name= "**-> 09**", value= "```Tenha bom senso: Use o bom senso em todas as suas interações no servidor e lembre-se de que suas ações podem afetar os outros membros. Seja um membro responsável e contribua para criar um ambiente positivo e produtivo no servidor.```", inline= False)
    
    
    #imagens e roda pé
    embed.set_image(url= "https://thumbs.gfycat.com/LimitedLonelyAsp-max-1mb.gif")
    embed.set_thumbnail(url= "https://i.pinimg.com/originals/c7/c4/6b/c7c46b55b96a5477d29c12dc023fc176.jpg")
    embed.set_footer(text= "© Todos os creditos do bot reservados ao ySupra#9509.")
    await interaction.response.send_message(embed=embed, ephemeral=True)


client.run(TOKEN)
