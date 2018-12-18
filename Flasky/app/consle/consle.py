from mongoengine import *
import datetime
from app.consle import consle_api

@consle_api.route('/add')
def add():
    post1 = TextPost(title="Using MongoEngine", content='content')
    post1.save()
    return str(post1.posted)

@consle_api.route('/count')
def count():
    return str(BlogPost.objects.count())

# @consle_api.route('/all')
# def all_posts():
#    blogs = BlogPost.objects()
#    blog_array = []
#    blogs = BlogPost.objects(content='content')
#    blogs = BlogPost.objects(content__match='content')
#    blogs = BlogPost.objects(content__endswith='content')
#    blogs = BlogPost.objects(__raw__={'tags': 'codings'})
#    blogs = BlogPost.objects[:5]
#    blogs = BlogPost.objects[5:]
#    blogs = BlogPost.objects[10:15]
#    for blog in blogs:
#        blog_array.append(blog.to_json())
#     return blog_array


class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    meta = {'allow_inheritance': True}
    posted = DateTimeField(default=datetime.datetime.utcnow)

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.order_by('-posted')

    @queryset_manager
    def live_posts(doc_cls, queryset):
        return queryset.filter(posted=True)


class TextPost(BlogPost):
    content = StringField(required=True, max_length=2000)

# class AwesomerQuerySet(QuerySet):

#     def get_awesome(self):
#         return self.filter(awesome=True)

# class Page(Document):
#     meta = {'queryset_class': AwesomerQuerySet}

# BlogPost.objects.get_awesome()
# num_post = BlogPost.objects.count()
# year_expense = BlogPost.objects.sum('salary')
# mean_age = BlogPost.objects.average('age')

# class Film(Document):
#     title = StringField()
#     year = IntField()
#     rating = IntField(default=3)

# Film(title='The Shawshank', year=1993, rating=5).save()
# f = Film.objects().only('title').first()
