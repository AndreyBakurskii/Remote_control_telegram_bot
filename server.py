import telegram.ext as tg_ext
import telegram as tg

from config import TOKEN
import commands as cmd


import signal
import os

updater = tg_ext.Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: tg.Update, context: tg_ext.CallbackContext):

    list_button = [[tg.KeyboardButton(text="/space")],
                   [tg.KeyboardButton(text="/volume_up"), tg.KeyboardButton(text="/volume_mute"),
                    tg.KeyboardButton(text="/volume_down")],
                   [tg.KeyboardButton(text="/left"), tg.KeyboardButton(text="/right")],
                   [tg.KeyboardButton(text="/turn_off")],

                   ]
    reply_markup = tg.ReplyKeyboardMarkup(list_button)

    update.message.reply_text("Hello", reply_markup=reply_markup)


dispatcher.add_handler(tg_ext.CommandHandler("start", callback=start))


def volume_up(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("Volume up")
    cmd.volume_up()


dispatcher.add_handler(tg_ext.CommandHandler("volume_up", callback=volume_up))


def volume_mute(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("Volume mute")
    cmd.volume_mute()


dispatcher.add_handler(tg_ext.CommandHandler("volume_mute", callback=volume_mute))


def volume_down(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("Volume down")
    cmd.volume_down()


dispatcher.add_handler(tg_ext.CommandHandler("volume_down", callback=volume_down))


def space(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("Press space")
    cmd.space()


dispatcher.add_handler(tg_ext.CommandHandler("space", callback=space))


def left(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("press left")
    cmd.left()


dispatcher.add_handler(tg_ext.CommandHandler("left", callback=left))


def right(update: tg.Update, context: tg_ext.CallbackContext):
    update.message.reply_text("press right")
    cmd.right()


dispatcher.add_handler(tg_ext.CommandHandler("right", callback=right))

# command to turn off your computer
# def turn_off(update: tg.Update, context: tg_ext.CallbackContext):
#
#     keyboard = [[tg.InlineKeyboardButton("Yes", callback_data="1"),
#                  tg.InlineKeyboardButton("No", callback_data="0")]]
#
#     reply_markup = tg.InlineKeyboardMarkup(keyboard)
#
#     update.message.reply_text("Are you sure?", reply_markup=reply_markup)
#
#
# dispatcher.add_handler(tg_ext.CommandHandler('turn_off', callback=turn_off))


# def answer_turn_off(update: tg.Update, context: tg_ext.CallbackContext):
#
#     query = update.callback_query
#
#     query.answer()
#
#     answer = query.data
#
#     if int(answer):
#         cmd.turn_off()
#         exit_tg(update, context)
#
#     else:
#         update.effective_user.send_message("Ok!")


# dispatcher.add_handler(tg_ext.CallbackQueryHandler(answer_turn_off))


def exit_tg(update: tg.Update, context: tg_ext.CallbackContext):
    update.effective_user.send_message("Bye, bye!!!")
    os.kill(os.getpid(), signal.SIGINT)


dispatcher.add_handler(tg_ext.CommandHandler("exit", callback=exit_tg))


updater.start_polling()
