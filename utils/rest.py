def register_views(app, urls):
    for url in urls:
        app.add_url_rule(
            url[0], defaults={'id': None},
            view_func=url[1], methods=['GET']
        )
        app.add_url_rule(
            '%s<int:id>/' % url[0], view_func=url[1],
            methods=['GET', 'PUT', 'DELETE']
        )
        app.add_url_rule(url[0], view_func=url[1], methods=['POST'])
