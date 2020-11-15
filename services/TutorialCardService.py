from models.TutorialCard import TutorialCardDocument
from models.typedefs import TUTORIAL_CARD_TYPE
from typing import Optional, List, Union


class TutorialCardResource:
    resource: str
    resource_text: Optional[str]
    resource_type: str
    forward_condition: Optional[str]
    forward_condition_type: Optional[str]

    def __init__(
            self,
            resource: str,
            resource_type: str,
            resource_text: Optional[str]=None,
            forward_condition: Optional[str]=None,
            forward_condition_type: Optional[str]=None
    ):
        self.resource = resource
        self.resource_type = resource_type
        self.resource_text = resource_text
        self.forward_condition = forward_condition
        self.forward_condition_type = forward_condition_type


def get_tutorial_cards_from_db() -> List[TutorialCardDocument]:
    return TutorialCardDocument.objects


def _get_tutorial_card_resource_code(index: int) -> str:
    padded_index = f'0{index}' if index < 10 else f'{index}'
    return f'{TUTORIAL_CARD_TYPE}{padded_index}'


def populate_tutorial_card_db_entry(
        resources: List[TutorialCardResource],
        title: str,
        supporting_text: Optional[str]=None
) -> TutorialCardDocument:
    index = TutorialCardDocument.objects.count()

    entry = TutorialCardDocument(
        auth_required=False,
        resource_code=_get_tutorial_card_resource_code(index),
        resources=resources,
        supporting_text=supporting_text,
        title=title,
        type=TUTORIAL_CARD_TYPE,

    )
    entry.save()
    return entry


def get_tutorial_card_entry(
        card_id: str) -> Union[type(None), TutorialCardDocument]:
    entry = TutorialCardDocument.objects(resource_code=card_id).first()
    return entry
