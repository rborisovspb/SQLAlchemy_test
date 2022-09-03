from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('store',
        type = str,
        required=True,
        help="This field cannot be left blank")


    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message" : "Store not found"}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return {"message" : "Store already exists."}, 400
        store = StoreModel(name)
        store.save_to_db()
        return {"message" : "Store created successfully."}, 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {"message" : "Store already exists."}, 400
        store.delete_from_db()
        return {"message" : "Store is deleted."}, 201       
        


class StoreList(Resource):
    def get(self):
        return {"stores" : list(map(lambda store: store.json(), StoreModel.query.all()))}