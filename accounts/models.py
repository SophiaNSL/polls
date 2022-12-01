from django.db import models

# Create your models here.

class CommonModel(models.Model):
    created_at = models.DateTimeField('created_time', auto_now_add=True)
    updated_at = models.DateTimeField('updated_time', auto_now=True)

    class Meta:
        abstract = True



class User(CommonModel):

    USER_STATUS = (
        (1, 'Normal'),
        (0, 'Deleted'),
    )

    username = models.CharField('username', max_length=128, unique=True)
    password = models.CharField('password', max_length=256)
    nickname = models.CharField('nickname', max_length=256, null=True, blank=True)
    avatar = models.ImageField('avatar', upload_to='avatar', null=True, blank=True)
    status = models.SmallIntegerField('status', default=1, choices=USER_STATUS)
    is_super = models.BooleanField('is_superuser', default=False)

    # users = models.Manager()
    
    class Meta:
        db_table = 'accounts_user'

    def __str__(self):
        return self.username

class UserProfile(CommonModel):
    SEX_CHOICES = (
        (0, 'Prefer not to say'),
        (1, 'Male'),
        (2, 'Female'),
    )
    user = models.OneToOneField(User, verbose_name='related user',
                                related_name='profile',
                                on_delete=models.CASCADE)
    username = models.CharField('username', max_length=128, unique=True)
    real_name = models.CharField('real_name', max_length=128, null=True, blank=True)
    sex = models.SmallIntegerField('sex', default=0, choices=SEX_CHOICES)
    maxim = models.CharField('maxim', max_length=128, null=True, blank=True)
    address = models.CharField('address', max_length=128, null=True, blank=True)
 
    class Meta:
        db_table = 'accounts_user_profile'

class LoginHistory(models.Model):
    user = models.ForeignKey(User, related_name='login_history_list',
                             on_delete=models.CASCADE,
                             verbose_name='related user')
    username = models.CharField('username', max_length=128)
    login_type = models.CharField('login_type', max_length=128)
    ip = models.CharField('ip', max_length=32, default='')
    ua = models.CharField('ua', max_length=128, default='')
    created_at = models.DateTimeField('login_time', auto_now_add=True)
    
    class Meta:
        db_table = 'accounts_login_history'
        ordering = ['-created_at']

