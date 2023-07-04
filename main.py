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
        return "Eee so'ramang. ....... degan qizni sevgan..."
    
    if "ish" in processed:
        return "Dasturchilik qilib rizqini terib yuribdi..."
    
    if "fuc"  in processed:
        return "So'kinma, betarbiya..."
    
    if "wtf"  in processed:
        return "So'kinma, betarbiya..."
       
    if "jigar" in processed:
        return "Yaxshiman jigar, eeh sanam yo'q bo'b ketding 'jigar,jigar' deb"
    
    if "uylangan" in processed:
        return "Yo'q, haliyam yolg'iz, sevgani ham yo'q"
    
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
    app.run_polling(poll_interval=4)