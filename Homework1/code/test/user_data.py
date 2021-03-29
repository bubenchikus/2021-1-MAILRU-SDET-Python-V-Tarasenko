# mail, password
login = {'default': ['zapuskayte-gusya@yandex.ru', 'gus-password'],  # корректные данные для входа
         'invalid-password': ['zapuskayte-gusya@yandex.ru', 'password'],
         'empty-mail': ['', 'password'],
         'empty-password': ['zapuskayte-gusya@yandex.ru', ''],
         'mail-several': ['zapuskayte@yandex.ru gusya@yandex.ru', 'password'],
         'mail-format-1': ['nodomain', 'password'],
         'mail-format-2': ['emptydomain@', 'password'],
         'mail-format-3': ['@emptyname', 'password'],
         'mail-char-1': ["!#$%&'*+-/=?^_`{|}~@mail.com", 'pasword'],
         'mail-char-2': ["(),:;<>@[]@mail.com", 'pasword'],
         'mail-numeric-1': ['7-901-666-66-66', 'password'],
         'mail-numeric-2': ['+79016666666', 'password'],
         'mail-numeric-3': ['7-(901)-666-66-66', 'password'],
         'mail-numeric-4': ['7(901)6666666', 'password'],
         'mail-numeric-5': ['7-901-666-66-66-66-66', 'password'],
         'mail-numeric-6': ['12345678900', 'password'],
         'mail-numeric-7': ['0000', 'password']
         }


# fio, phone, password
change = {'default': ['Example Example Example', '+7-900-00-00', 'zapuskayte-gusya1@yandex.ru'],
          'all-empty': ['', '', ''],
          'wrong-phone': ['example', '0000', 'zapuskayte-gusya1@yandex.ru'],
          'wrong-mail': ['example', '+7-900-00-00', 'zapuskayte-gusya']
          }
