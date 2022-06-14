from allauth.account.adapter import DefaultAccountAdapter


class UserAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        # phone_number = data.get('phone_number')
        # if phone_number:
        #     user.phone_number = phone_number
        
        user.save()
        return super().save_user(request, user, form, commit)