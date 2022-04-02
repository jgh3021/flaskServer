from app import db
from datetime import datetime

class UserInfo(db.Model):
    __tablename__ = "userInfo"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    userId = db.Column(db.String(50), primary_key=True)
    userPassword = db.Column(db.String(500))
    email = db.Column(db.String(255))
    nickName = db.Column(db.String(255))
    userType = db.Column(db.String(1))
    registPlatform = db.Column(db.String(100))
    registDtm = db.Column(db.DateTime)
    updateDtm = db.Column(db.DateTime)

    def __init__(self, user_id=None, user_password=None, email=None,
                 nick_name=None, user_type=None, regist_platform=None):
        self.userId = user_id
        self.userPassword = user_password
        self.email = email
        self.nickName = nick_name
        self.userType = user_type
        self.registPlatform = regist_platform
        self.registDtm = datetime.now()
        self.updateDtm = datetime.now()

    def __repr__(self):
        return "userId : {}, nickName : {}, userType : {}".format(self.userId, self.nickName, self.userType)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}