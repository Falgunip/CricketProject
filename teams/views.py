from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from cricketadmin.models import Team, Match, Player


def index(request):
    name_list = Team.objects.order_by('-created_date')
    return render(request, 'teams/index.html', {'name_list':name_list})

def teamdetail(request,team_id):
    team = Team.objects.get(identifier=team_id)
    players = team.players.all()
    # print(players)
    return render(request, 'teams/teamdetail.html', {'t': team,'players':players})

def createteam(request):
    players = Player.objects.all()
    return render(request, 'teams/createteam.html', {'players':players})

def save(request):
    playerlist = request.POST.getlist('players')
    result = []
    for p in playerlist:
         playerObj = Player.objects.get(identifier=p)
         # print(playerObj)
         result.append(playerObj)

    # print(result)
    # print(playerObjs)
    team = Team.objects.create(teamName=request.POST.get('teamName'), logouri=request.FILES['logouri'], club_state=request.POST.get('club_state'))
    team.players.add(*result)
    return HttpResponseRedirect('/teams')



