from os import write
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer, PasswordChangeSerializer
from django.contrib.auth import get_user_model
import re
UserModel = get_user_model()
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
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'gender'):
            extra_fields.append('gender')
        if hasattr(UserModel, 'assets'):
            extra_fields.append('assets')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
        if hasattr(UserModel, 'job'):
            extra_fields.append('job')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        error_messages={
            'required': '아이디를 입력해주세요.',
            'blank': '아이디를 입력해주세요.',
        }
    )
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            'required': '비밀번호를 입력해주세요.',
            'blank': '비밀번호를 입력해주세요.',
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            'required': '비밀번호를 확인해야 합니다.',
            'blank': '비밀번호를 확인해야 합니다.',
        }
    )
    email = serializers.EmailField(
        required=True,
        error_messages={
            'required': '이메일을 입력해주세요.',
            'blank': '이메일을 입력해주세요.',
        }
    )
    nickname = serializers.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': '닉네임을 입력해주세요.',
            'blank': '닉네임을 입력해주세요.',
        }
    )
    age = serializers.IntegerField(
        required=True,
        error_messages={
            'required': '나이를 입력해주세요.',
            'invalid': '유효한 나이를 입력해주세요.',
        }
    )
    gender = serializers.ChoiceField(
        choices=[('남', '남'), ('여', '여')],
        required=True,
        error_messages={
            'required': '성별을 선택해주세요.',
            'invalid_choice': '유효한 성별을 선택해주세요.',
        }
    )
    job = serializers.ChoiceField(
        choices= NCS_JOB_CHOICES,
        required=True,
        error_messages={
            'required': '직업을 선택해주세요.',
            'invalid_choice': '유효한 직업을 선택해주세요.',
        }
    )
    assets = serializers.IntegerField(
        required=True,
        error_messages={
            'required': '자산을 입력해주세요.',
            'invalid': '유효한 자산 금액을 입력해주세요.',
        }
    )
    salary = serializers.IntegerField(
        required=True,
        error_messages={
            'required': '연봉을 입력해주세요.',
            'invalid': '유효한 연봉 금액을 입력해주세요.',
        }
    )

    def validate_username(self, value):
        # 유효성 검사: 5~20자의 영문 소문자와 숫자만 허용
        if not re.match(r'^[a-z0-9]{5,20}$', value):
            raise serializers.ValidationError("아이디는 5~20자의 영문 소문자와 숫자만 사용할 수 있습니다.")
        if UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError("이미 사용 중인 아이디입니다.")
        return value

    def validate_password1(self, value):
        # 유효성 검사: 8~20자의 영문 대/소문자, 숫자, 특수문자 포함
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,20}$', value):
            raise serializers.ValidationError("비밀번호는 8~20자의 영문 대/소문자, 숫자, 특수문자를 포함해야 합니다.")
        return value

    def validate_password2(self, value):
        # password2가 빈 값인 경우 처리
        password1 = self.initial_data.get('password1')
        if not value:
            raise serializers.ValidationError("비밀번호를 확인해야 합니다.")
        # password1과 일치하지 않는 경우 처리
        if password1 and password1 != value:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return value

    def validate_nickname(self, value):
        # 닉네임 중복 확인
        if UserModel.objects.filter(nickname=value).exists():
            raise serializers.ValidationError("이미 사용 중인 닉네임입니다.")
        return value

    def validate_age(self, value):
        # 나이는 1 이상의 정수만 허용
        if value < 1:
            raise serializers.ValidationError("유효한 나이를 입력해주세요.")
        return value

    def validate_assets(self, value):
        # 자산은 0 이상의 정수만 허용
        if value < 0:
            raise serializers.ValidationError("유효한 자산 금액을 입력해주세요.")
        return value

    def validate_salary(self, value):
        # 연봉은 0 이상의 정수만 허용
        if value < 0:
            raise serializers.ValidationError("유효한 연봉 금액을 입력해주세요.")
        return value

    def get_cleaned_data(self):
        print(self.data)
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', 0),
            'gender': self.validated_data.get('gender', ''),
            'assets': self.validated_data.get('assets', 0),
            'salary': self.validated_data.get('salary', 0),
            'job': self.validated_data.get('job', ''),
        }


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(
        required=True,
        error_messages={
            'required': '아이디를 입력해주세요.',
            'blank': '아이디를 입력해주세요.',
        }
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={
            'required': '비밀번호를 입력해주세요.',
            'blank': '비밀번호를 입력해주세요.',
        }
    )

    def validate_username(self, value):
        # 사용자 정의 ID 형식 검사 (5~20자의 영문 소문자와 숫자만 허용)
        if not re.match(r'^[a-z0-9]{5,20}$', value):
            raise serializers.ValidationError("아이디는 5~20자의 영문 소문자와 숫자만 사용할 수 있습니다.")
        return value

    def validate(self, attrs):
        # 추가적인 로그인 실패 조건 처리
        username = attrs.get('username')
        password = attrs.get('password')

        # ID 또는 비밀번호가 입력되지 않은 경우
        if not username or not password:
            raise serializers.ValidationError("아이디와 비밀번호를 입력해주세요.")

        # 사용자 존재 여부 확인
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("아이디 또는 비밀번호가 올바르지 않습니다.")

        # 비밀번호 확인
        if not user.check_password(password):
            raise serializers.ValidationError("아이디 또는 비밀번호가 올바르지 않습니다.")

        # 유효성 검사가 모두 통과되면 attrs 반환
        return super().validate(attrs)
    

class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    new_password1 = serializers.CharField(
        required=True,
        error_messages={
            'required': '새 비밀번호를 입력해주세요.',
            'blank': '새 비밀번호를 입력해주세요.'
        }
    )
    new_password2 = serializers.CharField(
        required=True,
        error_messages={
            'required': '새 비밀번호 확인란을 입력해주세요.',
            'blank': '새 비밀번호 확인란을 입력해주세요.'
        }
    )
    def validate(self, attrs):
        errors = {}  # 모든 에러를 저장할 딕셔너리
        # 새로운 비밀번호와 확인 비밀번호 일치 여부 확인
        new_password1 = attrs.get('new_password1')  # 안전한 접근
        new_password2 = attrs.get('new_password2')
        # 새 비밀번호와 확인란 비교
        if new_password1 != new_password2:
            errors['new_password2'] = '새 비밀번호가 일치하지 않습니다.'

        # 새 비밀번호 유효성 검사 (8~20자, 영문 대소문자, 숫자, 특수문자 포함)
        password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,20}$'
        if not re.match(password_pattern, new_password1):
            errors['new_password1'] = '새 비밀번호는 8~20자의 영문 대소문자, 숫자, 특수문자를 포함해야 합니다.'

        # 에러가 있다면 ValidationError 발생
        if errors:
            raise serializers.ValidationError(errors)

        # 부모 클래스의 추가 유효성 검사 수행
        return super().validate(attrs)