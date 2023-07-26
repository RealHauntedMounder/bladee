from django.shortcuts import render, get_object_or_404, redirect
from .models import Information, Album, Comment, UserProfile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import CommentForm, SignupForm
from datetime import datetime
from django.urls import reverse


def index(request):
    information = Information.objects.filter(is_bio=False)
    return render(request, 'core/index.html', {'information': information})

def contact(request):
    return render(request, 'core/contact.html')

def biography(request):
    bio_information = Information.objects.filter(is_bio=True)
    return render(request, 'core/biography.html', {'bio_information': bio_information})

def discography(request):
    albums = Album.objects.all()
    return render(request, 'core/discography.html', {'albums':albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tracks = album.tracks.all()

    num_comments = Comment.objects.filter(album=album).count()

    context = {
        'album': album,
        'tracks': tracks,
        'num_comments': num_comments
    }
    return render(request, 'core/album_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

@login_required
def user_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    liked_albums = user_profile.liked_albums.all()
    return render(request, 'core/user_profile.html', {'user_profile': user_profile, 'liked_albums': liked_albums})

@login_required
def like_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    user_profile = request.user.userprofile
    user_profile.liked_albums.add(album)
    print(f"{request.user.username} liked album {album.title}")
    return redirect('album_detail', album_id)

@login_required
def unlike_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    user_profile = request.user.userprofile
    user_profile.liked_albums.remove(album)
    print(f"{request.user.username} unliked album {album.title}")
    return redirect('album_detail', album_id)

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def add_comment(request, pk):
    eachAlbum = Album.objects.get(id=pk)

    form = CommentForm(instance=eachAlbum)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachAlbum)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body'];
            comment = Comment(album=eachAlbum, commenter_name=name, comment_body=body, date_added=datetime.now())
            comment.save()
            return redirect(eachAlbum.get_absolute_url())
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'core/add_comment.html', context)


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.filter(album=pk).last()
    album_id = comment.album.pk
    comment.delete()
    return redirect(reverse('album_detail', args=[album_id]))


