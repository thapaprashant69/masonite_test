from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
            # Route.get("/", "WelcomeController@show"),
        #   Route.get("/blog", "BlogsController@show"),
          Route.get("/", "BlogsController@show"),
          Route.get("/blog/create", "BlogsController@create"),
          Route.post("/blog/create", "BlogsController@store"),
          Route.get("/blog/@slug/item","BlogsController@single"),
          Route.get("/blog/author/@author_id", "BlogsController@allposts"),
          Route.get("blog/@id/edit", "BlogsController@editblog"),
          Route.post("blog/@id/update", "BlogsController@update"),
          Route.get("blog/@id/delete", "BlogsController@delete"),
          Route.get("blog/count", "BlogsController@getcount"),
          ]
ROUTES += Auth.routes()
