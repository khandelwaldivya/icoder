from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from blog.models import BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allposts = Post.objects.all()
    context={'allposts' : allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post= Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments,'user':request.user}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno = postSno)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,'your comment has been posted successful')
    return redirect("/blog/{post.slug}")


