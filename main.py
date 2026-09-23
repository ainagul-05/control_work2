import asyncio
import logging
from config import bot, dp, path_db
from handlers import commands, fsm_add_books 
from database import db



dp.include_router(router=commands.router_commands)

dp.include_router(router=fsm_add_books.router_addbooks)




if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO)
    asyncio.run(db.init_db())
    asyncio.run(dp.start_polling(bot))
