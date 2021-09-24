from flask_restful import Resource, reqparse
from models.historical import HistoricalModel

class Historical(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('date',
        type=str,
    )

    parser.add_argument('coin_id',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('cmc_rank',
        type=int,
    )    

    parser.add_argument('market_cap',
        type=float,
    )    

    parser.add_argument('price',
        type=float,
    )  

    parser.add_argument('_open',
        type=float,
    ) 

    parser.add_argument('high',
        type=float,
    ) 

    parser.add_argument('low',
        type=float,
    ) 

    parser.add_argument('close',
        type=float,
    )

    parser.add_argument('time_high',
        type=str,
    ) 

    parser.add_argument('time_low',
        type=str,
    ) 

    parser.add_argument('volume_24h',
        type=float,
    ) 

    parser.add_argument('percent_change_1h',
        type=float,
    ) 

    parser.add_argument('percent_change_24h',
        type=float,
    ) 

    parser.add_argument('percent_change_7d',
        type=float,
    ) 

    parser.add_argument('circulating_supply',
        type=str,
    ) 

    parser.add_argument('total_supply',
        type=float,
    ) 

    parser.add_argument('max_supply',
        type=float,
    ) 

    parser.add_argument('num_market_pairs',
        type=int,
    ) 

    def get(self, coin_id):
        historical = HistoricalModel.find_by_id(coin_id)
        if historical:
            return historical.json()
        return {'message': 'Historical not fond'}, 404


class HistoricalList(Resource):
    def get(self):
        return {'historical': list(map(lambda x: x.json(), HistoricalModel.query.all()))}