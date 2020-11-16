from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, BooleanField, ListField
from models.typedefs import INFORMATION_CARD_RESOURCE_CODE_REGEX, INFORMATION_CARD_TYPE, CARD_RESOURCE_TYPE


class InformationCardResourceDocument(EmbeddedDocument):
    resource = StringField(required=True, db_field='resource')
    resource_text = StringField(db_field='resourceText')
    resource_type = StringField(
        required=True,
        db_field='resourceType',
        choices=CARD_RESOURCE_TYPE.values()
    )


class InformationCardDocument(Document):
    meta = {'collection': 'InformationCards', 'db_alias': 'cards'}
    auth_required = BooleanField(required=True, db_field='authRequired')
    department = StringField(db_field='department')
    owner = StringField(db_field='owner')
    resource_code = StringField(
        required=True,
        db_field='resourceCode',
        unique=True,
        regex=INFORMATION_CARD_RESOURCE_CODE_REGEX
    )
    resources = ListField(
        field=EmbeddedDocumentField(InformationCardResourceDocument),
        db_field='resources'
    )
    supporting_text = StringField(db_field='supportingText')
    title = StringField(required=True, db_field='title')
    type = StringField(
        required=True, db_field='type', choices=[INFORMATION_CARD_TYPE])
