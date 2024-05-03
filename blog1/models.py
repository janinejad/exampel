from django.db import models

# Create your models h

class blog(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    author = models.CharField(max_length=150,verbose_name='نام نویسنده')
    content = models.TextField(verbose_name='محتوای پست')
    created_at = models.DateTimeField(auto_now=True,verbose_name='زمان ایجاد پست')
    updated_at = models.DateTimeField(null=True,blank=True,verbose_name='زمان ویرایش پست')
    image = models.ImageField(null=True,blank=True,verbose_name='تصویر شاخص')
    emailAddress = models.EmailField(null=True,blank=True,verbose_name='ایمیل')
    interested = models.BooleanField(default=False,verbose_name='پسند شده')
    status = models.BooleanField(default=False,verbose_name='وضعیت نمایش')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='پست'
        verbose_name_plural = 'پستها'

