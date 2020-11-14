from models.ChatCard import ChatCardDocument
from models.typedefs import CHAT_CARD_SENDER_TYPE, CHAT_CARD_TYPE
from typing import List, Union


def get_chat_cards_from_db() -> List[ChatCardDocument]:
    return ChatCardDocument.objects


def _get_chat_card_resource_code(index: int) -> str:
    padded_index = f'0{index}' if index < 10 else f'{index}'
    return f'{CHAT_CARD_TYPE}{padded_index}'


def populate_chat_card_db_entry(message: str) -> ChatCardDocument:
    index = ChatCardDocument.objects.count()

    entry = ChatCardDocument(
        message=message,
        sender=CHAT_CARD_SENDER_TYPE['BOT'],
        type=CHAT_CARD_TYPE,
        resource_code=_get_chat_card_resource_code(index)
    )
    entry.save()
    return entry


def get_chat_card_entry(card_id: str) -> Union[type(None), ChatCardDocument]:
    entry = ChatCardDocument.objects(resource_code=card_id).first()
    return entry
