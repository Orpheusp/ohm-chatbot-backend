from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, BooleanField, ListField
from models.typedefs import TUTORIAL_CARD_RESOURCE_CODE_REGEX, TUTORIAL_CARD_TYPE, CARD_RESOURCE_TYPE, TUTORIAL_CARD_FORWARD_CONDITION_TYPE


class TutorialCardResourceDocument(EmbeddedDocument):
    resource = StringField(required=True, db_field='resource')
    resource_text = StringField(db_field='resourceText')
    forward_condition = StringField(db_field='forwardCondition')
    forward_condition_type = StringField(
        db_field='forwardConditionType',
        choices=TUTORIAL_CARD_FORWARD_CONDITION_TYPE
    )
    resource_type = StringField(
        required=True,
        db_field='resourceType',
        choices=CARD_RESOURCE_TYPE.values()
    )


class TutorialCardDocument(Document):
    meta = {'collection': 'TutorialCards', 'db_alias': 'cards'}
    auth_required = BooleanField(required=True, db_field='authRequired')
    department = StringField(db_field='department')
    owner = StringField(db_field='owner')
    resource_code = StringField(
        required=True,
        db_field='resourceCode',
        unique=True,
        regex=TUTORIAL_CARD_RESOURCE_CODE_REGEX
    )
    resources = ListField(
        field=EmbeddedDocumentField(TutorialCardResourceDocument),
        db_field='resources'
    )
    supporting_text = StringField(db_field='supportingText')
    title = StringField(required=True, db_field='title')
    type = StringField(
        required=True, db_field='type', choices=[TUTORIAL_CARD_TYPE])
