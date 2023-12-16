import discord
from discord.ext import commands
#------------------------------------------------------------------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True
#------------------------------------------------------------------------------------------------------------------
bot = commands.Bot(command_prefix='%', intents=intents)
#------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
#------------------------------------------------------------------------------------------------------------------
@bot.command()
async def presentatiom(ctx):
    await ctx.send(f'Salute Utente. Io sono GreenBot. Digita %helpme per una lista completa dei miei comandi')
#------------------------------------------------------------------------------------------------------------------
@bot.command()
async def helpme(ctx):
    await ctx.send(f'Per te una lista di comandi che puoi dirmi:')
    await ctx.send(f'Il comando %list ti da una lista di alimenti e di dove devi buttarli')
    await ctx.send(f'Il comando %info ti da delle informazioni sui rifiuti che ti possono essere molto utili')
    await ctx.send(f'Il comando %tips ti da dei consigli molto utili')
    await ctx.send(f'Se vuoi delle statistiche ecco: https://www.europarl.europa.eu/news/it/headlines/society/20180328STO00751/statistiche-sulla-gestione-dei-rifiuti-in-europa-infografica-con-fatti-e-cifre')
#------------------------------------------------------------------------------------------------------------------
@bot.command()
async def list(ctx):
    await ctx.send(f'Per te una lista dei rifiuti attualmente registrati. È sempre modificabile con altri comandi che trovi con %helpme')
    await ctx.send(f'Se vuoi delle statistiche ecco: https://www.europarl.europa.eu/news/it/headlines/society/20180328STO00751/statistiche-sulla-gestione-dei-rifiuti-in-europa-infografica-con-fatti-e-cifre')
    await ctx.send(f'-Imballaggi-')
    imballaggi = {
        "imballaggio di polistirolo":"plastica",
        "imballaggio di merendine":"plastica",
        "imballaggio della pasta":"plastica",
        "imballaggio della cioccolata":"plastica",
        "imballaggio di uova":"carta/plastica",
        "imballaggio di tetrapak":"plastica"
    }
    await ctx.send(imballaggi)
    await ctx.send(f'-Oggetti vari-')
    oggetti_vari = {
        "penna":"umido_secco",
        "matita":"umido_secco",
        "pennarello":"umido_secco",
        "temperino":"plastica",
        "righello":"plastica",
        "squadra":"plastica",
        "cover_telefono":"plastica",
        "fazzoletti":"umido_secco",
        "giornali":"carta",
        "bucce":"umido_secco",
        "vestiti":"indifferenziata",
        "lana":"indifferenziata",
        "gomme da masticare":"indifferenziata",
        "lattine":"alluminio(di solito va insieme alla plastica)",
        "cotton-fioc":"indifferenziata",
        "schede telefoniche":"cassonetto RAEE",
        "batterie":"sono rifiuti pericolosi, quinid cerca nella zona un centro di raccolta pile",
    }
    await ctx.send(oggetti_vari)
    await ctx.send(f'Fonti varie, eccone una:https://www.buonalavita.it/dovelobutto/')
#------------------------------------------------------------------------------------------------------------------
@bot.command()
async def info(ctx):
    await ctx.send(f'Per te una lista di info sulle cose che buttiamo per strada')
    await ctx.send(f'Se vuoi delle statistiche ecco: https://www.europarl.europa.eu/news/it/headlines/society/20180328STO00751/statistiche-sulla-gestione-dei-rifiuti-in-europa-infografica-con-fatti-e-cifre')
    ogg_decomp = {
        "fazzoletti":"fino a 3 mesi",
        "giornali":"fino a 3 mesi",
        "bucce":"fino a 3 mesi",
        "verdura":"fino a 3 mesi",
        "vestiti":"da 3 a 6 mesi",
        "confezioni di tetrapak":"da 3 a 6 mesi",
        "fiammiferi":"da 3 a 6 mesi",
        "lana":"da 6 mesi a 1 anno",
        "sigarette":"da 1 a 2 anni",
        "bucce d'arancia":"da 1 a 2 anni",
        "gomme da masticare":"fino a 4 anni",
        "lattine":"dai 10 ai 20 anni",
        "cotton-fioc":"dai 10 ai 20 anni",
        "pannolini":"dai 30 ai 50 anni",
        "pneumatici":"dai 30 ai 50 anni",
        "bottiglie di plastica":"dai 100 ai 1000 anni",
        "accendini":"dai 100 ai 1000 anni",
        "polistirolo":"dai 100 ai 1000 anni",
        "barattoli di latta":"dai 100 ai 1000 anni",
        "lenza da pesca":"dai 100 ai 1000 anni",
        "schede telefoniche":"dai 100 ai 1000 anni",
        "batterie":"oltre 1000 anni",
        "vetro":"oltre 1000 anni"
    }
    await ctx.send(ogg_decomp)
    await ctx.send(f'Fonte:https://discarica.roma.it/decomposizione-rifiuti/')
#------------------------------------------------------------------------------------------------------------------
@bot.command()
async def tips(ctx):
    await ctx.send(f'Per te alcuni consigli che puoi seguire:')
    await ctx.send(f'Prima di differenziare il vetro o i contenitori di alimentari puliscili')
    await ctx.send(f'Quando differenzi la plastica togli le etichette')
    await ctx.send(f'Nella carta non buttare gli scontrini e i fazzoletti')
    await ctx.send(f'Ricla il più possibile')
    await ctx.send(f'Se vuoi delle statistiche ecco: https://www.europarl.europa.eu/news/it/headlines/society/20180328STO00751/statistiche-sulla-gestione-dei-rifiuti-in-europa-infografica-con-fatti-e-cifre')
#------------------------------------------------------------------------------------------------------------------
bot.run("MTE4MzA2ODg0MjQ4NjkzOTgzMA.GkipzE.kR5wyGNS4-cakSd2Lccr8n3Ub_UVrAhJ8rAPSk")
