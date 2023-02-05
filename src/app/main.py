from routes.route_v1 import RouteV1

if __name__ == '__main__':
    route = RouteV1()
    app = route.get_app()
    app.run(debug=True)