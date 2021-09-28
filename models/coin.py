from sqlalchemy.sql import sqltypes
from db import db

class CoinModel(db.Model):
    __tablename__ = 'coins'

    # coin_id = db.Column(db.Integer, db.ForeignKey('historicals.coin_id'))
    # historicals = db.relationship('HistoricalModel')

    id = db.Column(sqltypes.Integer, primary_key=True)
    name = db.Column(sqltypes.Text)
    slug = db.Column(sqltypes.Text)
    symbol = db.Column(sqltypes.Text)
    status = db.Column(sqltypes.Text)
    category = db.Column(sqltypes.Text)
    description = db.Column(sqltypes.Text)
    subreddit = db.Column(sqltypes.Text)
    notice = db.Column(sqltypes.Text)
    tags = db.Column(sqltypes.Text)
    tag_names = db.Column(sqltypes.Text)
    website = db.Column(sqltypes.Text)
    twitter = db.Column(sqltypes.Text)
    message_board = db.Column(sqltypes.Text)
    chat = db.Column(sqltypes.Text)
    explorer = db.Column(sqltypes.Text)
    reddit = db.Column(sqltypes.Text)
    technical_doc = db.Column(sqltypes.Text)
    source_code = db.Column(sqltypes.Text)
    announcement = db.Column(sqltypes.Text)
    platform_id = db.Column(sqltypes.Integer)
    date_added = db.Column(sqltypes.Text)
    date_launched = db.Column(sqltypes.Text)

    def __init__(self, name, slug, symbol, status, category, description,
                    subreddit, notice, tags, tag_names, website, twitter,
                    message_board, chat, explorer, reddit, technical_doc,
                    source_code, announcement, platform_id, date_added,
                    date_launched):

        self.name = name
        self.slug = slug
        self.symbol = symbol
        self.status = status
        self.category = category
        self.description = description
        self.subreddit = subreddit
        self.notice = notice
        self.tags = tags
        self.tag_names = tag_names 
        self.website = website
        self.twitter = twitter
        self.message_board = message_board
        self.chat = chat
        self.explorer = explorer
        self.reddit = reddit
        self.technical_doc =technical_doc 
        self.source_code = source_code
        self.announcement = announcement
        self.platform_id = platform_id
        self.date_added = date_added
        self.date_launched = date_launched
        
    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'slug': self.slug, 
                'symbol': self.symbol, 
                'status': self.status,
                'category': self.category,
                'description': self.description,
                'subreddit': self.subreddit,
                'notice': self.notice, 
                'tags': self.tags,
                'tag_names': self.tag_names, 
                'website': self.website,
                'twitter': self.twitter,
                'message_board': self.message_board,
                'chat': self.chat,
                'explorer': self.explorer,
                'reddit': self.reddit,
                'technical_doc': self.technical_doc,
                'source_code': self.source_code,
                'announcement': self.announcement,
                'platform_id': self.platform_id,
                'date_added': self.date_added, 
                'date_launched': self.date_launched
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()