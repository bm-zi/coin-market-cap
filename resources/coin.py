from flask_restful import Resource, reqparse
from models.coin import CoinModel
 
class Coin(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('slug',
        type=str,
    )

    parser.add_argument('symbol',
        type=str,
    )

    parser.add_argument('status',
        type=str,
    )

    parser.add_argument('category',
        type=str,
    )

    parser.add_argument('description',
        type=str,
    )

    parser.add_argument('subreddit',
        type=str,
    )

    parser.add_argument('notice',
        type=str,
    )

    parser.add_argument('tags',
        type=str,
    )

    parser.add_argument('tag_names',
        type=str,
    )

    parser.add_argument('website',
        type=str,
    )

    parser.add_argument('twitter',
        type=str,
    )

    parser.add_argument('message_board',
        type=str,
    )

    parser.add_argument('chat',
        type=str,
    )

    parser.add_argument('explorer',
        type=str,
    )

    parser.add_argument('reddit',
        type=str,
    )

    parser.add_argument('technical_doc',
        type=str,
    )

    parser.add_argument('source_code',
        type=str,
    )

    parser.add_argument('announcement',
        type=str,
    )

    parser.add_argument('platform_id',
        type=int,
    )

    parser.add_argument('date_added',
        type=str,
    )

    parser.add_argument('date_launched',
        type=str,
    )

    def get(self, name):
        coin = CoinModel.find_by_name(name)
        if coin:
            return coin.json()
        return {'message': 'Coin not fond'}, 404

class CoinList(Resource):
    def get(self):
        return {'coins': list(map(lambda x: x.json(), CoinModel.query.all()))}
        # return {'coins': [x.json() for x in ItemModel.query.all()]}