from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http.response import HttpResponse
from django.urls import re_path
from django.shortcuts import reverse

from psychological_tests.models import UserExtended


@admin.register(UserExtended)
class UserExtendedAdmin(admin.ModelAdmin):

    class Media:
        js = ('external/js/jquery.js', 'admin/user_admin.js',)

    list_display = ('username', 'fio', 'group_code')

    fields = ('username', 'get_update_password', 'go_to_users_tests', 'fio', 'group_code')

    readonly_fields = ('get_update_password', 'go_to_users_tests')

    def get_update_password(self, user):
        return mark_safe('<input type="button" value="Установить пароль пользователю (длина пароля строго 8 цифр!)" '
                         'id="get_update_password" data-user-id="{}">'.format(user.id))
    get_update_password.allow_tags = True
    get_update_password.short_description = 'Установить пароль пользователю'

    def get_urls(self):
        urls = super(UserExtendedAdmin, self).get_urls()
        new_urls = [re_path(r'^(?P<id>[0-9]+)/update_password/$', self.update_password)]

        return new_urls + urls

    def update_password(self, request, id):
        """
        Обновление пароля пользователя
        """
        success = True
        password = request.GET.get('password')
        try:
            user = UserExtended.objects.get(id=id)
            user.set_password(password)
            user.save()
        except Exception as e:
            success = False
        return HttpResponse('Пароль обновлен - {}!'.format(password)) \
            if success else HttpResponse('Возникла ошибка при установке пароля')

    def go_to_users_tests(self, user):
        return mark_safe('<input type="button" value="Посмотреть все тесты пользователя" '
                         'data-user-id="{}" id="show-user-button">'.format(user.id))

    go_to_users_tests.allow_tags = True
    go_to_users_tests.short_description = 'Перейти к тестам пользователя'
