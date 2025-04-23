import sqlite3
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = "tasks.db"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, user_id INTEGER, text TEXT)")
    conn.commit()
    conn.close()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для учёта задач. Добавь задачу: /add <текст>")

@dp.message(Command("add"))
async def add_task(message: types.Message):
    task_text = message.text.partition(' ')[2]
    if not task_text:
        await message.answer("Укажите текст задачи после /add")
        return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (user_id, text) VALUES (?, ?)", (message.from_user.id, task_text))
    conn.commit()
    conn.close()
    await message.answer("Задача добавлена!")

@dp.message(Command("list"))
async def list_tasks(message: types.Message):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, text FROM tasks WHERE user_id = ?", (message.from_user.id,))
    rows = c.fetchall()
    conn.close()
    if not rows:
        await message.answer("У вас нет задач.")
    else:
        tasks = "\n".join([f"{row[0]}. {row[1]}" for row in rows])
        await message.answer(f"Ваши задачи:\n{tasks}")

@dp.message(Command("delete"))
async def delete_task(message: types.Message):
    try:
        task_id = int(message.text.partition(' ')[2])
    except Exception:
        await message.answer("Укажите id задачи после /delete")
        return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE user_id = ? AND id = ?", (message.from_user.id, task_id))
    conn.commit()
    conn.close()
    await message.answer("Задача удалена (если была найдена).")

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
