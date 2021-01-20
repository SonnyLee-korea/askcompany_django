from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,ArchiveIndexView,YearArchiveView,MonthArchiveView,DayArchiveView,TodayArchiveView
from django.shortcuts import render,HttpResponse,Http404,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
def post_new(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request,'instagram/post_form.html',{
        'form':form,
    })



# /instagram/
# /instagram/1/
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','') # 두번째 인자는 없을 때 대신인자
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#         'q' : q,
#     })

# def post_detail(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     return render(request,'instagram/post_detail.html',{
#         'post':post,
#     })


# post_list = login_required(ListView.as_view(model=Post,paginate_by=10))


# @method_decorator(login_required,name='dispatch')
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 10
    
post_list = PostListView.as_view()
# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))


# 비 로그인 시 공개된 것만 봐라
class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated: # 로그인 여부
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request,year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post,date_field='created_at',paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post,date_field='created_at',make_object_list=True)

post_archive_month = MonthArchiveView.as_view(model=Post,date_field='created_at')

post_archive_day = DayArchiveView.as_view(model=Post,date_field='created_at')


# django authentication system (장고 인증 시스템)