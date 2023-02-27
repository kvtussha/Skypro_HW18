from flask import request

from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')

        return self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        if title := request.args.get('title'):
            movie.title = title

        if description := data.get('description'):
            movie.description = description

        if trailer := data.get('trailer'):
            movie.trailer = trailer

        if year := data.get('year'):
            movie.year = year

        if rating := data.get('rating'):
            movie.rating = rating

        self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)

