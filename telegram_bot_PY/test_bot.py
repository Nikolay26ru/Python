import pytest
import os
import sqlite3
from aiogram import types
import asyncio
from bot import init_db

@pytest.mark.asyncio
async def test_db_init_and_add():
    if os.path.exists("tasks.db"):
        os.remove("tasks.db")
    await init_db()
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (user_id, text) VALUES (?, ?)", (1, "test task"))
    c.execute("SELECT text FROM tasks WHERE user_id = 1")
    assert c.fetchone()[0] == "test task"
    conn.close()
