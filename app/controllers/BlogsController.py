from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Post import Post
from masoniteorm.query import QueryBuilder
builder = QueryBuilder(model=Post)
# print(dir(builder))


class BlogsController(Controller):
    def show(self, view: View, request: Request):
        blogs = Post.all()
        return view.render("homepage",{"blogs":blogs,"user":request.user()})
    
    def create(self, view: View):
        return view.render("blog")
    
    def single(self, view: View,request: Request):
        post_obj = Post.where("slug",request.param("slug")).first()
        # return post_obj
        return view.render("displayblog",{"post":post_obj})
    
    def allposts(self, view:View, request: Request):
        post_objs = Post.where("author_id",request.param("author_id")).get()
        return view.render("allblogs",{"posts":post_objs})
    
    def store(self, view: View, request : Request):
        try:
            count = Post.last().id+1
        except:
            count = 1
        Post.create(
            title = request.input('title'),
            description = request.input('description'),
            author_id = request.user().id,
            slug = f"article-{count}"
            # slug = Post.generate_unique_slug(request.input('title'))
        )
        
        return 'post created'
    
    def editblog(self, view: View, request : Request):
        blog = Post.find(request.param("id"))
        return view.render("editblog",{"blog":blog})
    
    def update(self, view: View, request : Request):
        post = Post.find(request.param("id"))
        post.title = request.input('title')
        post.description = request.input('description')
        post.save()
        return "Blog updated"
    
    def delete(self, view: View, request : Request):
        post = Post.find(request.param("id"))
        post.delete()
        return 'post deleted'
        
    def getcount(self,request:Request):
        # posts_count = QueryBuilder(table="users").group_by('post')
        # posts_count = QueryBuilder(table="posts").sum('author_id').group_by('author_id').count()
        # posts_count = QueryBuilder(table="posts").count("author_id").group_by('author_id').get(['author_id'])
        # posts_count = QueryBuilder(table="posts").group_by_raw('COUNT("author_id")').get()
        # posts_count = builder.table("users").select_raw("author_id","COUNT('author_id') as count").group_by('author_id').get()
        posts_count = builder.statement("SELECT author_id,COUNT(*) as count FROM posts GROUP BY author_id;")
        
        return posts_count
