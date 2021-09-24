from db import db

class CoinModel(db.Model):
    __tablename__ = 'coins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    slug = db.Column(db.String(80))
    symbol = db.Column(db.String(80))
    status = db.Column(db.String(80))
    category = db.Column(db.String(80))
    description = db.Column(db.String(80))
    subreddit = db.Column(db.String(80))
    notice = db.Column(db.String(80))
    tags = db.Column(db.String(80))
    tag_names = db.Column(db.String(80))
    website = db.Column(db.String(80))
    twitter = db.Column(db.String(80))
    message_board = db.Column(db.String(80))
    chat = db.Column(db.String(80))
    explorer = db.Column(db.String(80))
    reddit = db.Column(db.String(80))
    technical_doc = db.Column(db.String(80))
    source_code = db.Column(db.String(80))
    announcement = db.Column(db.String(80))
    platform_id = db.Column(db.Integer)
    date_added = db.Column(db.String(80))
    date_launched = db.Column(db.String(80))

    def __init__(self, _id, name, slug, symbol, status, category, description,
                    subreddit, notice, tags, tag_names, website, twitter,
                    message_board, chat, explorer, reddit, technical_doc,
                    source_code, announcement, platform_id, date_added,
                    date_launched):
                    
        self.id = _id
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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod    
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()