from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        gender = data.get("gender")
        assets = data.get("assets")
        salary = data.get("salary")
        job = data.get("job")

        user_email(user, email)
        user_username(user, username)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if gender:
            user_field(user, "gender", gender)
        if assets:
            user.assets = assets
        if salary:
            user.salary = salary
        if job:
            user.job = job
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
            self.populate_username(request, user)
        if commit:
            user.save()
        return user