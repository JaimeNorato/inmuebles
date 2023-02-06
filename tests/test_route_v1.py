from routes.route_v1 import RouteV1


def test_index():
    route = RouteV1()
    app = route.get_app()
    client = app.test_client()
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json == {"data": {"message": "run server!"}, "message": "success"}


def test_properties():
    route = RouteV1()
    app = route.get_app()
    client = app.test_client()
    response = client.get("/api/v1/properties")
    assert response.status_code == 200
    assert type(response.json) == dict


def test_properties_filter():
    route = RouteV1()
    app = route.get_app()
    client = app.test_client()
    response = client.post("/api/v1/properties", json={"status": "pre_venta"})
    assert response.status_code == 200
    assert type(response.json) == dict
