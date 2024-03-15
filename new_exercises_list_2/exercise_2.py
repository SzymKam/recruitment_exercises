# models.py
from django.db import models
from django.forms import ValidationError
from datetime import date
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage


class FootballClub(models.Model):
    name = models.CharField('nazwa', max_length=256)
    founded = models.DateField('data założenia')
    no_players = models.IntegerField('liczba piłkarzy')


class FootballPlayer(models.Model):
    first_name = models.CharField('pierwsze imię', max_length=256)
    last_name = models.CharField('nazwisko', max_length=256)
    birth_year = models.IntegerField('rok urodzenia')
    club = models.ForeignKey(FootballClub, on_delete=models.DO_NOTHING)
    nationality = models.CharField('narodowość', max_length=256, choices=['EU', 'non EU'])


# forms.py
from django.forms.models import ModelForm


class FootballPlayerForm(ModelForm):
    class Meta:
        model = FootballPlayer
        fields = '__all__'

# my validation
    def validate_birth_year(self):
        birth_year = self.cleaned_data['birth_year']
        if birth_year < date(2000, 1, 1):
            raise ValidationError('Niestety nie możesz dodać piłkarza, który urodził się przed 2000 rokiem.')

# my validation
    def validate_nationality(self):
        nationality = self.cleaned_data['nationality']
        if nationality == 'non EU':
            if len(FootballPlayer.objects.filter(nationality='non EU')) >= 3:
                raise ValidationError('Nie można dodać 4 zawodnika spoza Unii Europejskiej.')


# views.py
from django.views.generic.edit import CreateView


class AddFootballPlayerView(CreateView):
    form_class = FootballPlayerForm

    def form_valid(self, form):
        response = super().form_valid(form)
        # increase no_players in FootballClub when new player is added

        club = get_object_or_404(klass=FootballClub, pk=self.kwargs['club'])
        club.no_players += 1
        club.save()

        # send email
        self.send_mail(subject="New player", msg="Dodano poprawnie piłkarza")
        return response

    def form_invalid(self, form):
        self.send_mail(subject="Error", msg="Nie udało się dodać piłkarza")

    def send_mail(self, subject, msg):
        email = EmailMessage(
            subject=subject,
            body=msg
        )
        email.send()

    def get_all_sorted_clubs(self):
        sorted_clubs = (FootballClub.objects
                        .select_related('footballplayer')
                        .annotate(non_eu_players=models.Count('footballplayer', filter=(models.F('footballplayer__nationality') == 'non EU')))
                        .order_by('-non_eu_players'))

        return sorted_clubs
