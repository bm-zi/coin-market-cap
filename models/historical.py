from db import db

class HistoricalModel(db.Model):
    __tablename__ = 'historicals'

    date = db.Column(db.String(80))
    coin_id = db.Column(db.Integer, primary_key=True)
    cmc_rank = db.Column(db.Integer)
    market_cap = db.Column(db.Float(precision=2))
    price = db.Column(db.Float(precision=2))
    _open = db.Column(db.Float(precision=2))
    high = db.Column(db.Float(precision=2))
    low = db.Column(db.Float(precision=2))
    close = db.Column(db.Float(precision=2))
    time_high = db.Column(db.String(80))
    time_low = db.Column(db.String(80))
    volume_24h = db.Column(db.Float(precision=2))
    percent_change_1h = db.Column(db.Float(precision=2))
    percent_change_24h = db.Column(db.Float(precision=2))
    percent_change_7d = db.Column(db.Float(precision=2))
    circulating_supply = db.Column(db.Float(precision=2))
    total_supply = db.Column(db.Float(precision=2))
    max_supply = db.Column(db.Float(precision=2))
    num_market_pairs = db.Column(db.Integer)

    def __init__(self, date, coin_id, cmc_rank, market_cap, price,
                    _open, high, low, close, time_high, time_low, 
                    volume_24h, percent_change_1h, percent_change_24h, 
                    percent_change_7d, circulating_supply, total_supply, 
                    max_supply, num_market_pairs ):
                    
        self.date = date
        self.coin_id = coin_id
        self.cmc_rank = cmc_rank
        self.market_cap = market_cap
        self.price = price
        self._open = _open
        self.high = high
        self.low = low
        self.close = close
        self.time_high = time_high
        self.time_low = time_low
        self.volume_24h = volume_24h
        self.percent_change_1h = percent_change_1h
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply
        self.max_supply = max_supply
        self.num_market_pairs = num_market_pairs

    
    def json(self):
        return {
            'date': self.date, 
            'coin_id': self.coin_id, 
            'cmc_rank': self.cmc_rank, 
            'market_cap': self.market_cap, 
            'price': self.price, 
            '_open': self._open, 
            'high': self.high, 
            'low': self.low, 
            'close': self.close, 
            'time_high': self.time_high, 
            'time_low': self.time_low, 
            'volume_24h': self.volume_24h, 
            'percent_change_1h': self.percent_change_1h, 
            'percent_change_24h': self.percent_change_24h, 
            'percent_change_7d': self.percent_change_7d, 
            'circulating_supply': self.circulating_supply, 
            'total_supply': self.total_supply, 
            'max_supply': self.max_supply, 
            'num_market_pairs': self.num_market_pairs
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod    
    def find_by_id(cls, _id):
        return cls.query.filter_by(coin_id=_id).first()        