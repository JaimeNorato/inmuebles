from routes.route import Route

if __name__ == '__main__':
    route = Route()
    app = route.get_app()
    app.run(debug=True)