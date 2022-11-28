from django import forms
from .models import Players


class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = [
            "name",
            "english_name",
            "back_number",
            "birthdate",
            "team",
            "position",
            "height",
            "weight",
            "player_image",
        ]
        labels = {
            "name": "선수이름",
            "english_name": "영문 이름",
            "back_number": "등번호",
            "birthdate": "생년월일",
            "team": "소속 구단",
            "position": "Position",
            "height": "신장",
            "weight": "몸무게",
            "player_image": "선수 사진",
        }