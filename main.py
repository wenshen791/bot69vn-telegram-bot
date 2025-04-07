import telebot
from telebot.types import MenuButtonWebApp, WebAppInfo

TOKEN = "7545734397:AAG2Vs_3qzHP9W9xA2HArLSlRRVadowUwGs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Gửi tin nhắn chào mừng
    bot.send_message(
        message.chat.id,
        "🎁 Chào mừng bạn đến với 69VN!\nNhấn nút bên dưới để nhận +969K!"
    )

    try:
        # Gắn Mini App trỏ về trang chủ 69VN
        bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(
                text="🎯 ĐĂNG KÝ +969K",
                web_app=WebAppInfo(url="https://69vntrangchu.com")
            )
        )
    except Exception as e:
        print("❌ Lỗi khi gắn Mini App:", e)

if __name__ == "__main__":
    print("🤖 Bot 69VN đang chạy polling...")
    bot.polling(non_stop=True)
