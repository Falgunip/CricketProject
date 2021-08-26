from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from cricketadmin.models import Team, Match, Player


def index(request):
    name_list = Player.objects.order_by('-created_date')
    # print(name_list)
    return render(request, 'players/index.html', {'name_list': name_list})

def playerdetail(request, player_id):
    players = Player.objects.get(identifier=player_id)
    return render(request, 'players/playerdetail.html', {'p': players})

def createplayer(request):
    matches = Match.objects.all()
    teams = Team.objects.all()
    return render(request, 'players/createplayer.html', {'matches':matches, 'teams':teams})

def save(request):
    matchObj = Match.objects.get(id=request.POST.get('matches'))
    Player.objects.create(firstName=request.POST.get('firstName'), lastName=request.POST.get('lastName'), imageUri=request.FILES['imageUri'], player_jersey_number=request.POST.get('player_jersey_number'),country=request.POST.get('country'),matches=matchObj,run=request.POST.get('run'),highest_scores=request.POST.get('highest_scores'))
    return HttpResponseRedirect('/players')






