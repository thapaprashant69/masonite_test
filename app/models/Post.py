""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin


class Post(Model):
    """Post Model"""
    
    __fillable__ = ['title','slug','description','author_id']
    __dates__ = ['deleted_at']
    
    @belongs_to('author_id','id')
    def author(self):
        from app.models.User import User
        return User
    
    # def generate_unique_slug(self, title):
    #     slug = slugify(title)
    #     count = 1
    #     while Post.where('slug', slug).exists():
    #         slug = slugify('{} {}'.format(title, count))
    #         count += 1
    #     return slug