import telebot
from telebot.types import MenuButtonWebApp, WebAppInfo

# 🔐 Thay bằng token thật của bot 69VN
TOKEN = "YOUR_69VN_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎁 Chào mừng bạn đến với 69VN!\nNhấn nút bên dưới để nhận +969K!"
    )

    try:
        # 👇 Gắn Mini App mở trang 69vntrangchu.com
        bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(
                text="🎯 ĐĂNG KÝ +969K",
                web_app=WebAppInfo(url="https://69vntrangchu.com")
            )
        )
    except Exception as e:
        print("❌ Lỗi gắn Mini App:", e)

if __name__ == "__main__":
    print("🤖 Bot 69VN đang chạy polling...")
    bot.polling(non_stop=True)
