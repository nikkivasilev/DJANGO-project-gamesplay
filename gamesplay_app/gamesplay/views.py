from django.shortcuts import render, redirect

from gamesplay_app.gamesplay.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, \
    EditProfileForm, DeleteProfileForm
from gamesplay_app.gamesplay.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def profile_fullname():
    profile = get_profile()
    full_name = []
    if profile.first_name:
        full_name.append(profile.first_name)
    if profile.last_name:
        full_name.append(profile.last_name)
    if full_name:
        return " ".join(full_name)
    else:
        return None


def game_average_rating():
    total_ratings = 0
    if Game.objects.all().count() < 1:
        return 0

    for game in Game.objects.all():
        total_ratings += game.rating
    return total_ratings / Game.objects.all().count()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'base/home-page.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context=context)


def details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'full_name': profile_fullname(),
        'total_games': Game.objects.all().count(),
        'average_rating': game_average_rating(),
    }
    return render(request, 'profile/details-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context=context)


def dashboard(request):
    context = {
        'games': Game.objects.all(),
    }

    return render(request, 'base/dashboard.html', context=context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'game/create-game.html', context=context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }
    return render(request, 'game/details-game.html', context=context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/edit-game.html', context=context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/delete-game.html', context=context)
