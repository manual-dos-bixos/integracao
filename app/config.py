import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:H%40XRTei%24K5aPGU.@db.otehdyoibzmgrqufxbgm.supabase.co:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False