from flask_restx import Namespace, Resource, fields
from flask_login import login_required

from ..extensions import db
from ..models import Orders

api = Namespace('order', path='/')

order_model = api.model('Order Model', {
    'oid': fields.Integer,
    'address': fields.String,
    'item': fields.String,
    'quantity': fields.Integer,
    'o_pid':fields.Integer
})

@api.route('/order')
class OrderList(Resource):
    @api.doc("Search orders")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    #@login_required
    @api.marshal_with(order_model, as_list=True)
    def get(self):
        result = Orders.query.all()
        return result

    @api.doc("Create new order")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    #@login_required
    @api.expect(order_model)
    @api.marshal_with(order_model)
    def post(self):
        result = Orders(address = order_model.address, item = order_model.item, quantity = order_model.quantity)
        db.session.add(result)
        db.session.commit()
        return result

@api.route('/order/<int:oid>')
@api.param('oid','order id')
class Order(Resource):
    @api.doc("Get order info")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    @api.marshal_with(order_model, skip_none=True)
    def get(self, oid):
        result = Orders.query.filter_by(oid=oid).first()
        if result:
            return result
        else:
            abort(400, 'No valid order')
    
    @api.doc("Get order info")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    def put(self, oid):

        return "modify order"
    
    @api.doc("delete order")
    @api.response(200, 'Success')
    @api.response(400, 'Bad Request')
    def delete(self, oid):
        result = Orders.query.filter_by(pid=pid).first()
        if result:
            db.session.delete(result)
            db.session.commit()
        else:
            abort(400, 'Failed to delete order.')





