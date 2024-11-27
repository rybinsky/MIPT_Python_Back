from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Card, Comment, UserCardInteraction
from .forms import CardForm, CommentForm, RegistrationForm


def home_view(request):
    if request.user.is_authenticated:
        return redirect('card_list')
    else:
        return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        if not User.objects.filter(username=username).exists():
            return redirect('register')
        
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('card_list')
        else:
            form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('card_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def card_list_view(request):
    cards = Card.objects.all()
    cards = sorted(cards, key=lambda x: (-x.likes, x.dislikes))
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def card_create_view(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/card_form.html', {'form': form})

def card_detail_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    comments = card.comments.all()
    comment_form = CommentForm()
    user_interaction = UserCardInteraction.objects.filter(user=request.user, card=card).first() if request.user.is_authenticated else None
    return render(request, 'cards/card_detail.html', 
                  {'card': card, 'comments': comments, 'comment_form': comment_form, 'user_interaction': user_interaction}
    )

@login_required
def card_update_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/card_form.html', {'form': form})

@login_required
def comment_create_view(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.card = card
            comment.author = request.user
            comment.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CommentForm()
    return render(request, 'cards/comment_form.html', {'form': form, 'card': card})

@login_required
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    card_id = comment.card.id
    comment.delete()
    return redirect('card_detail', pk=card_id)

@login_required
def card_like_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    interaction, created = UserCardInteraction.objects.get_or_create(user=request.user, card=card)

    if interaction.liked:
        card.likes -= 1
        interaction.liked = False
    else:
        card.likes += 1
        interaction.liked = True
        if interaction.disliked:
            card.dislikes -= 1
            interaction.disliked = False

    interaction.save()
    card.save()
    return redirect('card_detail', pk=card.pk)

@login_required
def card_dislike_view(request, pk):
    card = get_object_or_404(Card, pk=pk)
    interaction, created = UserCardInteraction.objects.get_or_create(user=request.user, card=card)

    if interaction.disliked:
        card.dislikes -= 1
        interaction.disliked = False
    else:
        card.dislikes += 1
        interaction.disliked = True
        if interaction.liked:
            card.likes -= 1
            interaction.liked = False

    interaction.save()
    card.save()
    return redirect('card_detail', pk=card.pk)
