import sys

sys.path.insert(0, '../')
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, random
vk_session = vk_api.VkApi(login= "87766290334", password= "BOLA20052005", app_id=2685278)
vk_session.auth(token_only=True)

anime = ["photo412963799_457467618","photo412963799_457467619","photo412963799_457467620","photo412963799_457467621","photo412963799_457467644","photo412963799_457467645","photo412963799_457467646", "photo412963799_457467647", "photo412963799_457467648", "photo412963799_457467649", "photo412963799_457467650", "photo412963799_457467651", "photo412963799_457467652","photo412963799_457467653", "photo412963799_457467654","photo412963799_457467655","photo-78170322_456239459","photo-78170322_456239456","photo-78170322_456239455","photo-78170322_456239454%2","photo-78170322_456239453","photo-78170322_456239451","photo-78170322_456239450","photo-78170322_456239450","photo-128535882_457266289","photo-128535882_457266288","photo-128535882_457266287","photo-128535882_457266282",'photo-128535882_457266237','photo-128535882_457266278','photo-128535882_457266275','photo-128535882_457266274','photo-128535882_457266267','photo-128535882_457266239','photo-128535882_457266262','photo-128535882_457266261','photo-128535882_457266260','photo-95972039_457264327','photo-128535882_457266257','photo-128535882_457266255','photo-128535882_457266254','photo-95972039_456252043','photo-128535882_457266253','photo-95972039_456252040','photo-95972039_456252039','photo-128535882_457266252','photo-95972039_456252037','photo-95972039_456252036','photo-95972039_456252035','photo-128535882_457266251','photo-95972039_456252034','photo-128535882_457266247','photo-128535882_457266242','photo-95972039_456252009','photo-95972039_456252008','photo-128535882_457266241','photo-95972039_456252004','photo-95972039_456252001','photo-128535882_457266233','photo-95972039_456252000','photo-128535882_457266210','photo-95972039_456251999','photo-128535882_457266232','photo-95972039_456251998','photo-95972039_456251994','photo-95972039_456251992','photo-95972039_456251993','photo-95972039_456251990','photo-95972039_456251989','photo-128535882_457266222','photo-95972039_456251985','photo-95972039_456251983','photo-95972039_456251982','photo-95972039_456251981','photo-95972039_456251979','photo-95972039_456251977','photo-95972039_456251975','photo-95972039_456251974','photo-95972039_456251973','photo-95972039_456251972','photo-95972039_456251970','photo-95972039_456251969','photo-95972039_456251968','photo-95972039_456251966','photo-95972039_456251963','photo-95972039_456251958','photo-95972039_456251957','photo-95972039_456251953','photo-95972039_456251949','photo-95972039_456250353','photo-95972039_456246835','photo-95972039_456246834','photo-128535882_457266219','photo-95972039_456243116','photo-95972039_456243115','photo-95972039_456243114','photo-95972039_456243113','photo-95972039_456243112','photo-95972039_456243110','photo-95972039_456243108','photo-95972039_456241475','photo-95972039_456239842','photo-95972039_456239640','photo-128535882_457266218','photo-95972039_456239590','photo-95972039_456239375','photo-128535882_457266213']

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachment, keyboard=keyboard, payload=payload)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Текст сообщения: ' + str(event.text))
        response = event.text.lower()
        if response =='!аним фото':
            #uploader = vk_api.upload.VkUpload(vk_session)
            #img = uploader.photo_messages("9AhMTXoopmY.jpg")
            #media_id = str(img[0]['id'])
            #owner_id = str(img[0]['owner_id'])
            #print("photo" + owner_id + "_" + media_id,)
            send_message(peer_id=event.peer_id,message='Скинул рандомную аниме фоточку!\nЕсли у вас есть еще подобные фотографии, обратитесь к разработчику: @deadinside.creepy',attachment=random.choice(anime))
        if response =='ок':
        	session_api.messages.send(peer_id=event.peer_id, sticker_id=16964, random_id=random.randint(-2147483648, +2147483648),)
while True:
	pass