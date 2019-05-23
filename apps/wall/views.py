from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def wall(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        data = {
            "all_msgs": Message.objects.all().order_by("-created_at")
        }
        return render(request, "wall/wall.html", data)

def post_message(request):
    thisUser = User.objects.get(id=request.session['user_id'])
    Message.objects.create(user=thisUser, message=request.POST['msgText'])
    return redirect("/wall")

def post_comment(request, msg_id):
    thisUser = User.objects.get(id=request.session['user_id'])
    thisMsg = Message.objects.get(id=msg_id)
    Comment.objects.create(message=thisMsg, user=thisUser, comment=request.POST['cmntText'])
    return redirect("/wall")

def delete_msg(request, msg_id):
    thisMsg = Message.objects.get(id=msg_id)
    theseComments = thisMsg.comments.all()
    for cmnt in theseComments:
        cmnt.delete()
    thisMsg.delete()
    return redirect("/wall")

def edit_page(request):
    data = {
        "thisUser": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "wall/edit.html", data)

def update(request):
    errors = User.objects.validator(request.POST, "update")

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/edit_page")
    else:
        thisUser = User.objects.get(id=request.session['user_id'])
        thisUser.first_name = request.POST['fname']
        thisUser.last_name = request.POST['lname']
        if request.POST['pword']:
            thisUser.password = request.POST['pword']
        request.session['user_fname'] = thisUser.first_name
        thisUser.save()
        return redirect("/wall")

def user_posts(request, user_id):
    thisUser = User.objects.get(id=user_id)
    data = {
        "user_messages": thisUser.messages.all(),
        "user_comments": thisUser.comments.all()
    }
    return render(request, "wall/posts.html", data)

def like_message(request, msg_id):
    thisUser = User.objects.get(id=request.session['user_id'])
    thisMsg = Message.objects.get(id=msg_id)
    thisMsg.like.add(thisUser)
    thisMsg.save()
    return redirect("/wall")

def like_comment(request, cmnt_id):
    thisUser = User.objects.get(id=request.session['user_id'])
    thisCmnt = Comment.objects.get(id=cmnt_id)
    thisCmnt.like.add(thisUser)
    thisCmnt.save()
    return redirect("/wall")

def logout(request):
    request.session.clear()
    return redirect("/")