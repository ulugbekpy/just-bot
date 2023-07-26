from typing import Final
from telegram import Update
from telegram.ext import (Application, CommandHandler,
                          MessageHandler,filters,ContextTypes)

import environ
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


TOKEN: Final = get_env_variable('TOKEN')
BOT_USERNAME: Final = '@ul_coder_bot'

# Commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Men Ulug'bekning kotibiman. Nima xizmat?")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nima xizmat dedim...")
    

async def just_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eey bilmadim, hozirgi yoshlarga nima bo'lgan...")

async def rostmi_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Koʻnglingizni menga koʻrsating —
            Sogʻinchlar sargʻayib ketgani rostmi?""")
   

# Responses
def handle_response(text:str):
    processed: str = text.lower()

    if "va alaykum" in processed:
        return "O'ziz tinchmisiz, axir?"
    
    if "qachon" in processed:
        return "Ha endi, hamma narsaning ham o'z vaqti soati bor."
    
     
    if "mahkammi" in processed:
        return "Mahkam"
    
    if "ma ish" in processed:
        return "Dasturchilik qilib rizqini terib yuribdi..."
    
    if 'sevgi'  in processed:
        return """Allohga boʻlgan sevgi va Alloh uchun boʻlgan sevgidan boshqa sevgilar 
        insonning ruhiyatini botqoqqa botiradi"""
    
    if "bek kimni sevadi" in processed:
        return "Nima ishingiz bor "
    
    if "😆" in processed:
        return """
                😁
                """
    
    if "😁" in processed:
        return """
                😆
                """
    
    if "og'a" in processed:
        return "Sarvarbek?"
    
    if "haa" in processed:
        return "hmm"
    
    if 'ok' in processed:
        return "Sog' bo'l bratishka!"
    
    if "😔" in processed:
        return "xafa bo'lmang, azizim..."
    
    if "😢" in processed:
        return "yig'lamang, azizim..."
    
    if "yana bitta" in processed:
        return """  Osmonning bir uchi ufqqa tutashgan,
                    Bulutning bir uchi boshqa bulutga.
                    Shamollar daraxtlar shoxin oʻynashgan,
                    Oy esa osmonda choʻmgan sukutga. 
                """
    
    if "haligi" in processed:
        return "Chaynalmang, tez-tez gapiring"
    
    if "yo'q" in processed:
        return "Nima bo'ldi? Tinchlikmi?"
    
    if "opam" in processed:
        return "Abdulhafiyz, senmisan uka, nimaga botga bunaqa narsalarni yozyapsan"

    if "yaxshima" in processed:
        return "Yaxshi ekaningni eshitib xursand bo'ldim."
    
    if "yaxshimis" in processed:
        return "Yaxshi rahmat"
    
    if "bek yaxshimi" in processed:
        return "Otdek"
    
    if "savol berib ham bo'lmaydimi" in processed:
        return "Savol berish mumkin, lekin ayrim narsalar haqida so'rash odobsizlikka kiradi"

    if "rost" in processed:
        return "Bilardim..."

    if "hop" in processed:
        return "Xo'p deb yoziladi"
    
    if "xo'p" in processed:
        return "Biliming chakkimas"
    
    if "rahmat" in processed:
        return "Sog' bo'l"
    
    if "kechir" in processed:
        return "Juda madaniyatli ekansan"

    if "fuc"  in processed:
        return "So'kinma, betarbiya..."
    
    if "tushunarli" in processed:
        return "Aylanay sendan, tushunadiganlar kam hozirgi zamonda"
    
    if "wtf"  in processed:
        return "So'kinma, betarbiya..."
    
    if "shunaqa de" in processed:
        return "shunaqa"

    if "obbo seney" in processed:
        return "Obbo meney"
    
    if "azgincha" in processed:
        return "Azginchamas jichcha bo'ladi biz tomonlarda"
    
    if "pul kerak" in processed:
        return "Eey jiyan, kimga ham pul kerakmas."

       
    if "jigar" in processed:
        return "Yaxshiman jigar, eeh sanam yo'q bo'b ketding 'jigar,jigar' deb"
    
    if "uylangan" in processed:
        return "Yo'q, haliyam yolg'iz, sevgani ham yo'q"
    
    if "alaykum" in processed:
        return "Va alaykum assalom"
    
    if "masalan" in processed:
        return "tarkibida rahmat, kechiring yoki sevgi kabi so'zlar bo'lsa"
    
    if "bek qayerda" in processed:
        return "O'qchida"
    
    if "bek hozir qayerda" in processed:
        return "O'qchida"

    if "misol uchun" in processed:
        return "tarkibida rahmat, kechiring yoki sevgi kabi so'zlar bo'lsa"

    if "pul" == processed:
        return "Qanaqa pul?"

    if "tog'a" in processed:
        return "Nima deysan, jiyan?"
    
    if "kotiba" in processed:
        return "Kotiba noqulayliklar tug'dirishi mumkin"
    
    return "Men ba'zi gaplarga javob bera olaman, xolos, azizim..."


async def handle_message(update:Update,context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return 'goo'
    else:
        response: str = handle_response(text)

    print('Bot:',response)
    await update.message.reply_text(response)


async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cauased error {context.error}')


if __name__ == '__main__':
    print("Starting...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('just',just_command))
    app.add_handler(CommandHandler('rostmi',rostmi_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)