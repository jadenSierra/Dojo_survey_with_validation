from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = "dojo_survey_schema"

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name , location , language, comment, created_at, updated_at) VALUES ( %(name)s , %(d_location)s, %(language)s, %(comments)s, NOW(), NOW() );"
        print(query)
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL(DB).query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        # print(dojos)
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL("users_schema").query_db(query,data)
        return cls(result[0])

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['language']) < 3:
            flash("Please leave us a comment.")
            is_valid = False
        return is_valid