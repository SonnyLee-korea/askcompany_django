from django.contrib import admin
from .models import Post,Comment,Tag
from django.utils.safestring import mark_safe
# admin.site.register(Post)

@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','message','message_length','is_public','created_at','updated_at'] # id -> 별칭 pk(alias)
    list_display_links = ['message'] # 링크 걸기
    list_filter = ['created_at','is_public'] # 지정 필드값으로 필터링 옵션 제공
    search_fields = ['message'] # 해당 필드의 검색을 할 수 있게 해줌
    # form = PostForm
    
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px;"/>')
        return None

    def message_length(self,post):
        return f"{len(post.message)}글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass