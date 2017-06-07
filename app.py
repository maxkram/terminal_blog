from database import Database
from models.blog import Blog

Database.initialize()
blog = Blog(author="Серега",
            title="Пост ни о чем",
            description="Просто настрение хорошее")
blog.new_post()
blog.save_to_mongo()
from_database = Blog.from_mongo(blog.id)
print(blog.get_posts())