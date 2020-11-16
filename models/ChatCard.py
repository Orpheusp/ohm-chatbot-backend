from mongoengine import Document, StringField
from models.typedefs import CHAT_CARD_RESOURCE_CODE_REGEX, CHAT_CARD_TYPE, CHAT_CARD_SENDER_TYPE


class ChatCardDocument(Document):
    meta = {'collection': 'ChatCards', 'db_alias': 'cards'}
    message = StringField(required=True, db_field='message')
    resource_code = StringField(
        required=True,
        db_field='resourceCode',
        unique=True,
        regex=CHAT_CARD_RESOURCE_CODE_REGEX
    )
    sender = StringField(
        required=True,
        db_field='sender',
        choices=CHAT_CARD_SENDER_TYPE.values()
    )
    type = StringField(required=True, db_field='type', choices=[CHAT_CARD_TYPE])
