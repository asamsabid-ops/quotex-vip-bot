import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
BOT_TOKEN = "9091110474:AAFMM8Jag-6D1jB-e_5kp2EZSA66gX7us3M"
ADMIN_ID = 6346912982
QUOTEX_LINK = "https://broker-qx.pro/sign-up/?lid=2218464"
VIP_LINK = "https://t.me/+YOUR_VIP_LINK"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🔗 Quotex একাউন্ট খুলুন", url=QUOTEX_LINK)],[InlineKeyboardButton("✅ আমি একাউন্ট করেছি", callback_data="done")]]
    await update.message.reply_text(f"👋 Sabid Trading VIP তে স্বাগতম!\n\nআমার লিংক থেকে একাউন্ট করো:\n{QUOTEX_LINK}\n\nতারপর স্ক্রিনশট দাও।", reply_markup=InlineKeyboardMarkup(kb))
async def btns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query
    await q.answer()
    if q.data=="done":
        await q.message.reply_text("📸 এখন তোমার Quotex ID এর স্ক্রিনশট পাঠাও")
    if "approve" in q.data:
        uid=int(q.data.split("_")[1])
        await context.bot.send_message(uid, f"🎉 Approved! তোমার VIP গ্রুপ: {VIP_LINK}")
        await q.edit_message_text("Approved")
    if "reject" in q.data:
        uid=int(q.data.split("_")[1])
        await context.bot.send_message(uid, "❌ Reject, আবার সঠিক ID দাও")
        await q.edit_message_text("Rejected")
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u=update.message.from_user
    await update.message.reply_text("⏳ Admin চেক করছে...")
    kb=[[InlineKeyboardButton("✅ Approve", callback_data=f"approve_{u.id}"),InlineKeyboardButton("❌ Reject", callback_data=f"reject_{u.id}")]]
    await context.bot.send_photo(ADMIN_ID, update.message.photo[-1].file_id, caption=f"New ID: @{u.username} {u.id}", reply_markup=InlineKeyboardMarkup(kb))
app=Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(btns))
app.add_handler(MessageHandler(filters.PHOTO, photo))
app.run_polling()
