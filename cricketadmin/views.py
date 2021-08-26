import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q


import random

from cricketadmin.models import Player, Team, Match, Winner


def index(request):
    teamobj = Team.objects.all()
    return render(request, 'cricketadmin/index.html', {'teamobj': teamobj})


def result(request):
    teamobj = Team.objects.all()
    winnerobj = Winner.objects.all()
    matches = Match.objects.all()
    randomMatch = random.choice(matches)
    print(randomMatch)
    state = request.POST.get('club_state')
    print(state)
    if state == "State Level":
        teams = Team.objects.filter(Q(club_state="State Level"))
        # print(teams)
        # teamchoice = random.choices(teams, k=2)
        # print(teamchoice)
        team_a = random.choice(teams)
        print(team_a)
        team_b = random.choice(teams)
        print(team_b)
    elif state == "National Level":
        teams = Team.objects.filter(Q(club_state="National Level"))
        # print(teams)
        # teamchoice = random.choices(teams, k=2)
        # # print(teamchoice)
        team_a = random.choice(teams)
        print(team_a)
        team_b = random.choice(teams)
        print(team_b)
    else:
        teams = Team.objects.filter(Q(club_state="International Level"))
        # print(teams)
        # teamchoice = random.choices(teams, k=2)
        # print(teamchoice)
        team_a = random.choice(teams)
        print(team_a)
        team_b = random.choice(teams)
        print(team_b)

    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2025, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    # print(random_date)
    score_a = random.randint(10,1000)
    print(score_a)
    score_b = random.randint(10,1000)
    print(score_b)
    if score_a > score_b:
        winner_team = team_a
    else:
        winner_team = team_b
    return render(request, 'cricketadmin/result.html', {'state':state, 'winnerobj': winnerobj, 'randomMatch':randomMatch,'team_a':team_a,'team_b':team_b,'random_date':random_date, 'score_a':score_a,'score_b':score_b,'winner_team':winner_team})

