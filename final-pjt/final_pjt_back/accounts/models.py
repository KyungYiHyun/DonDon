from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

NCS_JOB_CHOICES = [
    ("경영·사무", "경영·사무"),
    ("금융·보험", "금융·보험"),
    ("교육", "교육"),
    ("자연·사회과학", "자연·사회과학"),
    ("법률·경찰·소방·교도·국방", "법률·경찰·소방·교도·국방"),
    ("보건·의료", "보건·의료"),
    ("사회복지·종교", "사회복지·종교"),
    ("문화·예술·디자인·방송", "문화·예술·디자인·방송"),
    ("운전·운송", "운전·운송"),
    ("영업·판매", "영업·판매"),
    ("경비·청소", "경비·청소"),
    ("미용·숙박·여행·오락·스포츠", "미용·숙박·여행·오락·스포츠"),
    ("음식서비스", "음식서비스"),
    ("건설", "건설"),
    ("기계", "기계"),
    ("재료", "재료"),
    ("화학", "화학"),
    ("섬유·의복", "섬유·의복"),
    ("전기·전자", "전기·전자"),
    ("정보통신", "정보통신"),
    ("식품가공", "식품가공"),
    ("인쇄·목재·가구·공예", "인쇄·목재·가구·공예"),
    ("환경·에너지·안전", "환경·에너지·안전"),
    ("농림어업", "농림어업"),
    ("학생", "학생"),
    ("무직", "무직")
]

class User(AbstractUser):
    nickname = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    # DB에 저장되는 값 = 남/여 , UI에서 보이는 값 = 남/여
    gender = models.CharField(max_length=2, choices=[('남', '남'), ('여', '여')])
    assets = models.IntegerField()
    salary = models.IntegerField()
    job = models.CharField(
    max_length=50,
    choices=NCS_JOB_CHOICES,
)
    
    def __str__(self):
        return self.username