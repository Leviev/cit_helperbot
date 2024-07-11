import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="*just paste*",
        parse_mode='Markdown'
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=escape_underline(replace_bold(update.message.text)),
        parse_mode='Markdown'
    )


def escape_underline(message: str):
    return message.replace('_', '\_')


def replace_bold(message: str):
    return message.replace('**', '*')


if __name__ == '__main__':
    application = ApplicationBuilder().token('0000001111:TELEGRAM_TOKEN_HERE').build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
