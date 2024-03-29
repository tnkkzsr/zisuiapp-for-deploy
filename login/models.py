from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager
import datetime

Gradechoices = [
    
    ("大学1年", "大学1年"),
    ("大学2年", "大学2年"),
    ("大学3年", "大学3年"),
    ("大学4年", "大学4年"),
    ("大学院1年", "大学院1年"),
    ("大学院2年", "大学院2年"),
    ("社会人", "社会人"),
    ("その他", "その他"),

]

Livingalonechoice = [
    
    ("1年", "1年"),
    ("2年", "2年"),
    ("3年", "3年"),
    ("4年", "4年"),
    ("5年", "5年"),
    ("6年", "6年"),
    ("7年以上", "7年以上"),

]
class CustomUserManager(UserManager):
    def create_superuser(self, email, username=None, password=None, **extra_fields):

        if username is None:
            username = email

        extra_fields.setdefault('staff', True)
        extra_fields.setdefault('admin', True)
        
        if extra_fields.get('staff') is not True:
            raise ValueError('Superuser must have staff=True.')
        if extra_fields.get('admin') is not True:
            raise ValueError('Superuser must have admin=True.')
        
        return self._create_user(email, username, password, **extra_fields)


#独自のユーザーモデルを定義
class User(AbstractBaseUser):
    
    email = models.EmailField('Eメールアドレス(ログイン時に使用）', max_length=255, unique=True,)
    username = models.CharField('ニックネーム', max_length=128,default="")
    userimage = models.ImageField('プロフィール画像',upload_to="images/", default="",)
    years =  models.CharField('学年', max_length=128,choices=Gradechoices,default="大学1年")
    living_alone = models.CharField('一人暮らし歴', max_length=128,choices =Livingalonechoice,default="1年")
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    active = models.BooleanField(default=True)
    zisui_count = models.IntegerField("総自炊回数",default=0)
    consecutive_zisui_count = models.IntegerField("総自炊回数",default=0)
    recent_created_at = models.DateTimeField("最後の投稿日",editable=True,blank=False,null=False, default=datetime.date.today())
    

    
    USERNAME_FIELD = 'email'
   
    objects = CustomUserManager()
    
    
    def __str__(self):             
        return self.username

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

   