from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validates_name(self,key,name):
        if not name:
            raise ValueError('Author Name required')
        return name
        
    @validates('phone_number')
    def validates_phone_number(self,key,phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number must be 10 digits')
        return phone_number

        

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
    @validates('title')
    def validates_title(self,key,title):
        if not title:
            raise ValueError('Title Required!')
        return title
    
    @validates('content','summary')
    def validates_content(self,key,string):
        if (key == 'content'):
            if len(string) <= 250:
                raise ValueError('Content too short! At least 250 characters required!')
            return string
        
        if(key == 'summary'):
            if len(string) >= 250:
                raise ValueError('Summary too short! 250 chharacters maximum')
            return string
        
    @validates('category')
    def validates_category(self,key,category):
        if (category != 'Fiction') and (category != 'Non-Fiction'):
            raise ValueError('Invalid Category')
        return category
    
    @validates('title')
    def validates_title(self,key,title):
        titles=["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in titles ):
            raise ValueError("Spice it up!")
        return title

        
   
