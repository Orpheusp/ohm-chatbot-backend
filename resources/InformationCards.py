from flask_restful import Resource, request
from flask import jsonify
from services.InformationCardService import *


class InformationCards(Resource):

    def get(self, card_id=None):
        in_test_mode = request.args.get('test')

        if in_test_mode not in ['True', 'true']:
            return 404

        if card_id:
            entry = get_information_card_entry(card_id)
            return jsonify(entry)

        entries = get_information_cards_from_db()
        return jsonify(entries)
