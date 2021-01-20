from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.urls import reverse




class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d') #/media/instagram/post/
    tag_set = models.ManyToManyField('Tag',blank=True) # m : n 에서는 blank 를 True로 보통해야함 : 태그를 안하는 경우도 있으니까 => 장고 유효성 검사에서 걸림
    is_public = models.BooleanField(default=False,verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message
    
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    class Meta:
        ordering = ['-id']
    # Java의 toString
    
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,
                                limit_choices_to={'is_public':True}) #instagram.Post    => post_id 필드가 생성이 됩니다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    # post_set = models.ManyToManyField(Post) 혹은

    def __str__(self):
        return self.name