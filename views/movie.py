from flask import request
from flask_restx import Namespace, Resource
from dao.model.movie import Movie, MovieSchema
from implemented import movie_service

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        genre = request.args.get('genre_id')
        director = request.args.get('director_id')
        year = request.args.get('year')
        movies = movie_service.get_all(genre, director, year)

        return movies_schema.dump(movies), 200

    def post(self):
        data = request.json
        movie_service.create(data)
        return "", 201

@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req = request.json
        req['id'] = mid

        movie_service.update(req)

        return "", 204


    def patch(self, mid):
        req = request.json
        req['id'] = mid

        movie_service.update_partial(req)

        return '', 204


    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204