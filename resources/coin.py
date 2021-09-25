from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.coin import CoinModel
 
class Coin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('slug', type=str)
    parser.add_argument('symbol', type=str)
    parser.add_argument('status', type=str)
    parser.add_argument('category', type=str)
    parser.add_argument('description', type=str)
    parser.add_argument('subreddit', type=str)
    parser.add_argument('notice', type=str)
    parser.add_argument('tags', type=str)
    parser.add_argument('tag_names', type=str)
    parser.add_argument('website', type=str)
    parser.add_argument('twitter', type=str)
    parser.add_argument('message_board', type=str)
    parser.add_argument('chat', type=str)
    parser.add_argument('explorer', type=str)
    parser.add_argument('reddit', type=str)
    parser.add_argument('technical_doc', type=str)
    parser.add_argument('source_code', type=str)
    parser.add_argument('announcement', type=str)
    parser.add_argument('platform_id', type=int)
    parser.add_argument('date_added', type=str)
    parser.add_argument('date_launched', type=str)

    @jwt_required()
    def get(self, name):
        coin = CoinModel.find_by_name(name)
        if coin:
            return coin.json()
        return {'message': 'Coin not fond'}, 404
    
    def post(self, name):
        if CoinModel.find_by_name(name):
            return {'message': "A coin with the name '{}' already exists.".format(name)}, 400

        data = Coin.parser.parse_args()
        coin = CoinModel(name,
                        data['slug'],
                        data['symbol'],
                        data['status'],
                        data['category'],
                        data['description'],
                        data['subreddit'],
                        data['notice'],
                        data['tags'],
                        data['tag_names'],
                        data['website'],
                        data['twitter'],
                        data['message_board'],
                        data['chat'],
                        data['explorer'],
                        data['reddit'],
                        data['technical_doc'],
                        data['source_code'],
                        data['announcement'],
                        data['platform_id'],
                        data['date_added'],
                        data['date_launched']
                    )
        try:
            coin.save_to_db()
        except:
            return {'message': 'An error occurred inserting coin.'}, 500

        return coin.json(), 201

    def delete(self, name):
        coin = CoinModel.find_by_name(name)
        if coin:
            coin.delete_from_db()

        return {'message': 'Coin deleted'}

    def put(self, name):
        data = Coin.parser.parse_args()
        
        coin = CoinModel.find_by_name(name)
        
        if coin is None:
            coin = CoinModel(name, **data)
        else:
            coin.slug = data['slug']
            coin.symbol = data['symbol']
            coin.status = data['status']
            coin.category = data['category']
            coin.description = data['description']
            coin.subreddit = data['subreddit']
            coin.notice = data['notice']
            coin.tags = data['tags']
            coin.tag_names = data['tag_names']
            coin.website = data['website']
            coin.twitter = data['twitter']
            coin.message_board = data['message_board']
            coin.chat = data['chat']
            coin.explorer = data['explorer']
            coin.reddit = data['reddit']
            coin.technical_doc = data['technical_doc']
            coin.source_code = data['source_code']
            coin.announcement = data['announcement']
            coin.platform_id = data['platform_id']
            coin.date_added = data['date_added']
            coin.date_launched = data['date_launched']

        coin.save_to_db()

        return coin.json()    

class CoinList(Resource):
    def get(self):
        return {'coins': list(map(lambda x: x.json(), CoinModel.query.all()))}
        # return {'coins': [x.json() for x in ItemModel.query.all()]}