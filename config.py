import os

class Config:
    # Local development: SQLite dosyası kullan
    # Production: MySQL kullan (DO sunucusunda)
    
    if os.getenv('DATABASE_URL'):  # Production (GitHub Actions secret olarak set edilecek)
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    else:  # Local development
        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
