from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Profile, Post, User, Contact
from .forms import LogInForm, UserEditForm, ProfileEditForm
import json
from django.http import JsonResponse

# user interactions


@csrf_exempt
def like(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        fuser = User.objects.get(pk=request.user.id)
        x = post.like.add(fuser)
        return HttpResponseRedirect(reverse("index"))
    except:
        return JsonResponse({"error": "error"})


@csrf_exempt
def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    post.like.remove(user)
    return HttpResponseRedirect(reverse("index"))


@login_required
def follow(request):
    selected_user = request.POST["user_follow"]
    user_follow = User.objects.get(username=selected_user)
    requesting_user = request.user
    uid = user_follow.id
    current_user = User.objects.get(pk=requesting_user.id)
    new_contact = Contact.objects.create(follower=current_user, following=user_follow)
    new_contact.save()
    return HttpResponseRedirect(reverse("profile_view", kwargs={"post_user_id": uid}))


@login_required
def unfollow(request):
    selected_user = request.POST["user_unfollow"]
    user_follow = User.objects.get(username=selected_user)
    requesting_user = request.user
    current_user = User.objects.get(pk=requesting_user.id)
    x = Contact.objects.get(follower=current_user, following=user_follow)
    x.delete()
    uid = user_follow.id
    return HttpResponseRedirect(reverse("profile_view", kwargs={"post_user_id": uid}))


# user actions
def add_post(request, user_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            post = data["content"]
            active_user = User.objects.get(pk=user_id)
            x = Post.objects.create(user=active_user, content=post)
            x.save()
            return JsonResponse({"message": "success"})
        except:
            return JsonResponse({"message": "error"})


def edit_post(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.content = data["content"]
        edit_post.save()
        return JsonResponse({"message": "Change successful", "data": data["content"]})


def delete_post(request, post_id):
    if request.method == "GET":
        obj = Post.objects.filter(pk=post_id)
        obj.delete()
        return JsonResponse({"message": "post deleted successfully"})


# site navigation
@login_required
def index(request):
    all_posts = Post.objects.all()
    pagination = Paginator(all_posts, 10)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)
    liked_posts = Post.objects.filter(like=request.user.id)
    context = {"page_obj": page_obj, "liked_posts": liked_posts}
    return render(request, "network/all_posts.html", context)


@login_required
def following(request):
    users_followed = Contact.objects.filter(follower=request.user)

    followed_user_list = []
    for x in users_followed:
        followed_user_list.append(x.following)
    # followed_user_list is a query set of followed users
    followed_user_posts = []
    for x in followed_user_list:
        a = Post.objects.filter(user=x)
        for n in a:
            followed_user_posts.append(n)
    # followed_user_posts is a queryset of all posts of all followed users

    pagination = Paginator(followed_user_posts, 10)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)
    liked_posts = Post.objects.filter(like=request.user.id)
    context = {
        "followed": users_followed,
        "page_obj": page_obj,
        "liked_posts": liked_posts,
    }

    return render(request, "network/following.html", context)


@login_required
def all_users(request):
    all_users = User.objects.all()
    all_profiles = Profile.objects.all()
    context = {
        "all_users": all_users,
        "all_profiles": all_profiles,
        "active_user": request.user,
    }
    return render(request, "network/users.html", context)


def profile_view(request, post_user_id):
    selected_user = User.objects.get(pk=post_user_id)
    selected_user_posts = Post.objects.filter(user=selected_user)

    user_follows = Contact.objects.filter(follower=selected_user)
    followed_by = Contact.objects.filter(following=selected_user)

    try:
        is_follower = Contact.objects.get(
            following=selected_user, follower=request.user
        )
        is_follower = True
    except:
        is_follower = False

    pagination = Paginator(selected_user_posts, 10)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)
    liked_posts = Post.objects.filter(like=request.user.id)

    context = {
        "selected_user": selected_user,
        "following": user_follows,
        "followers": followed_by,
        "page_obj": page_obj,
        "current_user": request.user,
        "is_follower": is_follower,
        "liked_posts": liked_posts,
    }

    return render(request, "network/profile.html", context)


# login/registration/profile edit & creation
@login_required
def profile_update(request, id):
    # CP'd from book#
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_form.is_valid:
            user_form.save()
            profile_form.save()
            return render(request, "network/login_admin/update_profile.html")

    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)
        context = {
            "user_edit_form": user_edit_form,
            "profile_edit_form": profile_edit_form,
        }

        return render(request, "network/login_admin/update_profile.html", context)


def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse("Invalid login.")
    else:
        form = LogInForm()
        context = {"form": form}
        return render(request, "network/login_admin/login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request,
                "network/login_admin/register.html",
                {"message": "Passwords must match."},
            )

        # Attempt to create new user
        try:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            Profile.objects.create(user=new_user)
        except IntegrityError:
            return render(
                request,
                "network/login_admin/register.html",
                {"message": "Username already taken."},
            )
        login(request, new_user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/login_admin/register.html")
