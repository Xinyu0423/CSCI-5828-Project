import requests
def getProducts():
    response=requests.get("https://csci5828api.herokuapp.com/api/product")
    assert response.status_code==200

def getProductinfo():
    response=requests.get("http://csci5828api.herokuapp.com/api/product/100001")
    assert response.status_cdoe==200

def getOrders():
    response=requests.get("http://csci5828api.herokuapp.com/api/order")
    assert response.status_cdoe==200

def getOrderinfo():
    response=requests.get("http://csci5828api.herokuapp.com/api/order/101")
    assert response.status_code==200