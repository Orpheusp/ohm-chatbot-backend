from models.InformationCard import InformationCardDocument
from models.typedefs import INFORMATION_CARD_TYPE
from typing import List, Union, Optional


class InformationCardResource:
    resource: str
    resource_text: Optional[str]
    resource_type: str

    def __init__(
            self,
            resource: str,
            resource_type: str,
            resource_text: Optional[str]=None
    ):
        self.resource = resource
        self.resource_type = resource_type
        self.resource_text = resource_text


def get_information_cards_from_db() -> List[InformationCardDocument]:
    return InformationCardDocument.objects


def _get_information_card_resource_code(index: int) -> str:
    padded_index = f'0{index}' if index < 10 else f'{index}'
    return f'{INFORMATION_CARD_TYPE}{padded_index}'


def populate_information_card_db_entry(
        title: str,
        resources: List[InformationCardResource],
        supporting_text: Optional[str]=None,
) -> InformationCardDocument:
    index = InformationCardDocument.objects.count()

    entry = InformationCardDocument(
        auth_required=False,
        resource_code=_get_information_card_resource_code(index),
        resources=resources,
        supporting_text=supporting_text,
        title=title,
        type=INFORMATION_CARD_TYPE,
    )
    entry.save()
    return entry


def get_information_card_entry(
        card_id: str) -> Union[type(None), InformationCardDocument]:
    entry = InformationCardDocument.objects(resource_code=card_id).first()
    return entry
