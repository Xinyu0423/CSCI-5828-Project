from flask_restx import Resource, Namespace, fields, marshal_with, abort
from flask_login import login_required

from ..extensions import db
from ..models import Products

api = Namespace('product', path='/')

product_model = api.model('Product Model', {
    'pid': fields.Integer,
    'name': fields.String,
    'intro': fields.String,
    'price': fields.Float,
    'rating': fields.Float
})

@api.route('/product')
class ProductList(Resource):
    @api.doc("Get product list")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    @api.marshal_with(product_model, as_list=True)
    def get(self):
        result = Products.query.all()
        return result

    @api.doc("Create new product")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    #@login_required
    @api.expect(product_model)
    @api.marshal_with(product_model)
    def post(self):
        result = Product(name=product_model.name, intro= product_model.intro, price = product_model.price)
        db.session.add(result)
        db.commit()
        return result

@api.route('/product/<int:pid>')
@api.param('pid','product id')
@api.doc(params={'pid': 'Product ID'})
class Product(Resource):
    @api.doc("Get Product Info with product id")
    @api.response(200,'Success')
    @api.response(400, 'Invalid Request')
    @api.marshal_with(product_model, skip_none=True)
    def get(self, pid):
        result = Products.query.filter_by(pid=pid).first()
        if result:
            return result
        else:
            abort(400, 'No valid product.')
    
    @api.doc("Modify Product Info with product id")
    @api.response(200,'Success')
    @api.response(400, 'Invalid Request')
    #@login_required
    def put(self, pid):

        return "modify product"


    @api.doc("Delete Product")
    @api.response(200,'Product Deleted')
    @api.response(400, 'Invalid Request')
    #@login_required
    def delete(self, pid):
        result = Products.query.filter_by(pid=pid).first()
        if result:
            db.session.delete(result)
            db.session.delete()
        else:
            abort(400, 'Failed to delete product.')

    