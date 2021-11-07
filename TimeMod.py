#автор roki_crazy
from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(TimeMod()) 
 
class TimeMod(loader.Module): 
    """Покажу время всех городов мира""" 
    strings = {'name': 'TimeMod | by @roki_crazy'} 
 
    async def timecmd(self, message): 
        """Используйте .time время <город>.""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@just_zhenya_bot" 
            if not text and not reply: 
                await message.edit("<b>Нет аргумента!!! Пиши time. + свой город </b>") 
                return 
            if text: 
                await message.edit("<b> узнаю...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=528677877)) 
                        await message.client.send_message(chat, "Время " + text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Разблокируй этого @just_zhenya_bot бота! </b>") 
                        return 
                    if not response.text: 
                        await message.edit("<попробуй ещё раз.</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                await message.edit("<b>Узнаю...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=528677877)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Разблокируй этого @just_zhenya_bot бота!</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<Попробуй ещё раз.</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("<b>Неизвестная ошибка.</b>")
