from flask_restx import Namespace, Resource
from dao.model.director import DirectorSchema
from implemented import director_service

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200