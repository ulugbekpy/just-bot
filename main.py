from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,filters,ContextTypes

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
   

# Responses
def handle_response(text:str):
    processed: str = text.lower()

    if "va alaykum" in processed:
        return "O'ziz tinchmisiz, axir?"
    
    if "qachon" in processed:
        return "Ha endi, hamma narsaning ham o'z vaqti soati bor."
    
    if "sevgan" in processed:
        return "Eee so'ramang. M...... degan qizni sevgan."
    
    if "ish" in processed:
        return "Dasturchilik qilib rizqini terib yuribdi..."
    
    if 'sevgi'  in processed:
        return """Allohga boʻlgan sevgi va Alloh uchun boʻlgan sevgidan boshqa sevgilar 
        insonning ruhiyatini botqoqqa botiradi"""
    
    if "ulug'bek kimni sevadi" in processed:
        return "Nima ishingiz bor "
    
    if "bitta eshitaylik" in processed:
        return """
                Koʻnglingizni menga koʻrsating —
                Sogʻinchlar sargʻayib ketgani rostmi?
                Pichoqlar suyakka yetgani rostmi?
                Siz kabi dunyoga sigʻmagan ozmi?
                """
    
    if "yana bitta" in processed:
        return """  Osmonning bir uchi ufqqa tutashgan,
                    Bulutning bir uchi boshqa bulutga.
                    Shamollar daraxtlar shoxin oʻynashgan,
                    Oy esa osmonda choʻmgan sukutga. 
                """
    
    if "haligi" in processed:
        return "Chaynalmang, tez-tez gapiring"
    
    if "begim" in processed:
        return "Yaxshimisan"
    
    if "yo'q" in processed:
        return "Nima bo'ldi? Tinchlikmi?"

    if "yaxshi" in processed:
        return "Yaxshi ekaningni eshitib xursand bo'ldim."
    
    if "savol berib ham bo'lmaydimi" in processed:
        return "Savol berish mumkin, lekin ayrim narsalar haqida so'rash odobsizlikka kiradi"

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

    if "opam" in processed:
        return "Abdulhafiyz, senmisan uka, nimaga botga bunaqa narsalarni yozyapsan"
       
    if "jigar" in processed:
        return "Yaxshiman jigar, eeh sanam yo'q bo'b ketding 'jigar,jigar' deb"
    
    if "uylangan" in processed:
        return "Yo'q, haliyam yolg'iz, sevgani ham yo'q"
    
    if "ha bo'pti" in processed:
        return "Jahl qilma eee"
    
    if "pul" == processed:
        return "Qanaqa pul?"

    if "tog'a" in processed:
        return "Nima deysan, jiyan?"
    
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

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)