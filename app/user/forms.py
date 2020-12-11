from core.models import MyProfile
from django import forms


class MyProfileForm(forms.ModelForm):
    """User Details"""
    class Meta:
        model = MyProfile
        fields = ['position', 'image']


class PersonalityForm(forms.Form):
    """Personality Test"""
    CHOICES_1 = [('answer_1', 'Run your own tavern?'),
                 ('answer_2', 'Have a sword twice as powerful as any other in the game?'),
                 ('answer_3', 'Three charges of a spell that allows you control other players, against their will?'),
                 ('answer_4', 'Know more secrets than any other players?')]

    question_1 = forms.CharField(label="In a game, would you rather:", widget=forms.RadioSelect(choices=CHOICES_1))

    CHOICES_2 = [('answer_1', 'A great storyline.'),
                 ('answer_2', 'Solving a riddle no one else has gotten.'),
                 ('answer_3', 'Being the most Feared person in the game.'),
                 ('answer_4', 'Making your own maps of the world and selling them.')]

    question_2 = forms.CharField(label="In a game, you enjoy the most:", widget=forms.RadioSelect(choices=CHOICES_2))

    CHOICES_3 = [('answer_1', 'You get a big group of players to help you defeat it.'),
                 ('answer_2', 'Find the way to kill monsters by yourself as no one did before.'),
                 ('answer_3', 'You attack him before he attacks you.'),
                 ('answer_4', 'Hide somewhere you know the monster cannot follow you.')]

    question_3 = forms.CharField(label="In a game, you have encountered big monster:",
                                 widget=forms.RadioSelect(choices=CHOICES_3))

    CHOICES_4 = [('answer_1', 'A bard, who is a good friend and who is great for entertaining you and your friends?'),
                 ('answer_2', 'A wizard, to identify the items that you find there?'),
                 ('answer_3', 'An amulet that increases the damage you do against other players by 10%?'),
                 ('answer_4', 'Magic cloak so you can move around the area without restrictions?')]

    question_4 = forms.CharField(label="For the dungeon you'll take:", widget=forms.RadioSelect(choices=CHOICES_4))

    CHOICES_5 = [('answer_1', 'Have a biggest clan on a server?'),
                 ('answer_2', 'Have the highest score on the list?'),
                 ('answer_3', 'Be undefeated PvP player on server?'),
                 ('answer_4', 'Design my own area in a game?')]

    question_5 = forms.CharField(label="In a game, You'd prefer to:", widget=forms.RadioSelect(choices=CHOICES_5))

    CHOICES_6 = [('answer_1', 'You prefer to hear what someone has to say?'),
                 ('answer_2', 'You are bragging about having best equipment in the area?'),
                 ('answer_3', 'How many other players you have defeated in challenges?'),
                 ('answer_4', 'About how to find a secret item?')]

    question_6 = forms.CharField(label="In a game you talk about:", widget=forms.RadioSelect(choices=CHOICES_6))

