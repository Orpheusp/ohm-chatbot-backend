from flask_restful import Resource, request
from flask import jsonify
from secrets import CHATBOT_DEVELOPER_ACCESS_TOKEN
from models.ChatCard import ChatCardDocument
from models.InformationCard import InformationCardDocument
from models.TutorialCard import TutorialCardDocument
from models.typedefs import CHAT_CARD_TYPE, TUTORIAL_CARD_TYPE, INFORMATION_CARD_TYPE, CHAT_CARD_RESOURCE_CODE_REGEX, TUTORIAL_CARD_RESOURCE_CODE_REGEX, INFORMATION_CARD_RESOURCE_CODE_REGEX
from typing import Union, List, NewType, Optional
from services.ChatCardService import get_chat_card_entry
from services.InformationCardService import get_information_card_entry
from services.TutorialCardService import get_tutorial_card_entry

import requests
import re


CHATBOT_API_URL = 'https://api.chatbot.com/query'


OhmCard = NewType(
    'OhmCard',
    Union[ChatCardDocument, InformationCardDocument, TutorialCardDocument]
)


class Chats(Resource):

    def _send_message(self, message: Optional[str]=None):
        headers = {
            'authorization': f'Bearer {CHATBOT_DEVELOPER_ACCESS_TOKEN}',
            'content-type': 'application/json',
        }
        payload = {
            'sessionId': '13456132138',
        }
        if message:
            payload['query'] = message
        else:
            payload['trigger'] = 'welcome'

        response = requests.post(
            CHATBOT_API_URL, json=payload, headers=headers)
        return response.json()

    def _extract_response(self, response: object):
        if response['result'] and \
                response['result']['fulfillment'] and \
                len(response['result']['fulfillment']) and \
                response['result']['fulfillment'][0] and \
                response['result']['fulfillment'][0]['message']:
            return response['result']['fulfillment'][0]['message']

    def _get_card_type(self, card_id: str) -> Optional[str]:
        if re.fullmatch(CHAT_CARD_RESOURCE_CODE_REGEX, card_id):
            return CHAT_CARD_TYPE

        if re.fullmatch(TUTORIAL_CARD_RESOURCE_CODE_REGEX, card_id):
            return TUTORIAL_CARD_TYPE

        if re.fullmatch(INFORMATION_CARD_RESOURCE_CODE_REGEX, card_id):
            return INFORMATION_CARD_TYPE

        return None

    def _get_card_entry(self, card_id: str) -> Optional[OhmCard]:
        card_type = self._get_card_type(card_id)
        card = None

        if card_type == CHAT_CARD_TYPE:
            card = get_chat_card_entry(card_id)
        elif card_type == TUTORIAL_CARD_TYPE:
            card = get_tutorial_card_entry(card_id)
        elif card_type == INFORMATION_CARD_TYPE:
            card = get_information_card_entry(card_id)

        return card

    def post(self):
        message = request.json.get('message', None)
        response = self._send_message(message)
        card_ids = self._extract_response(response)
        assert (card_ids)
        card_ids = card_ids.split(',')
        cards: List[OhmCard] = []

        for card_id in card_ids:
            card = self._get_card_entry(card_id)
            if card:
                cards.append(card)

        return jsonify(cards)
