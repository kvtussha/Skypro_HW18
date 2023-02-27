from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        all_genre= genre_service.get_all()
        return genres_schema.dump(all_genre), 200



@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200