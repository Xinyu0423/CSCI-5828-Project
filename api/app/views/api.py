import os
from flask import Blueprint

from ..extensions import api
from .auth import api as auth_ns
from .order import api as order_ns
from .product import api as product_ns

api_blueprint = Blueprint('api', __name__)
api.init_app(api_blueprint)

api.add_namespace(auth_ns)
api.add_namespace(order_ns)
api.add_namespace(product_ns)