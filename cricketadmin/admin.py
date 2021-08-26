from django.contrib import admin

# Register your models here.
from cricketadmin.models import Match, Team, Player, Winner

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Winner)
