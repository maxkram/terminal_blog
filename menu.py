from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Как зовут автора? ")
        self.user_blog = None
        if self._user_has_account():
            print("С возвращением {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {"author": self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Заголовок? ")
        description = input("Описание? ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Вы хотите читать (R) блог или что-нибудь (W) написать?")
        if read_or_write == 'R':
            pass
        elif read_or_write == 'W':
            pass
        else:
            print("Спасибо, что зашли")
