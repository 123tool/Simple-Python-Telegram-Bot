from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Halo! Selamat datang di bot saya.")

def help_command(update, context):
    update.message.reply_text("Gunakan /start untuk memulai bot.")

if __name__ == '__main__':
    TOKEN = 'MASUKKAN_TOKEN_API_ANDA_DI_SINI'

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()
