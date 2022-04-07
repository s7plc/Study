import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import My_Game

vk_session = vk_api.VkApi(token="25f027466fd4c9fb25c4a6654d1a1b8dc7f91cbcec550a05a6f1b3a03ae428136bc2861a164465c4e3924")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text, "random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "привет":
                send_some_msg(id, "Привет, друг! Напиши `старт` и ты сможешь поиграть в мою игру")
            elif msg == "старт":
                send_some_msg(id, My_Game.run())