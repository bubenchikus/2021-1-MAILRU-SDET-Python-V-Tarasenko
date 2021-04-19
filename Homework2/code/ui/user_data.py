# mail, password
login = {
    'default': ['zapuskayte-gusya@yandex.ru', 'gus-password'],  # корректные данные для входа
    'invalid-password': ['zapuskayte-gusya@yandex.ru', 'password'],
    'empty-mail': ['', 'password'],
    'empty-password': ['zapuskayte-gusya@yandex.ru', ''],
    'mail-several': ['zapuskayte@yandex.ru gusya@yandex.ru', 'password'],
    'mail-format-1': ['nodomain', 'password'],
    'mail-format-2': ['emptydomain@', 'password'],
    'mail-format-3': ['@emptyname', 'password'],
    'mail-char-1': ["!#$%&'*+-/=?^_`{|}~@mail.com", 'pasword'],
    'mail-char-2': ["(),:;<>@[]@mail.com", 'pasword'],
    'mail-phone-1': ['666-66-66', 'password'],
    'mail-phone-2': ['(666)6666666', 'password'],
    'mail-phone-3': ['86666666666', 'password'],
    'mail-phone-4': ['+76666666666', 'password'],
    'mail-long': ['6'*1000, 'password']
    }


# fio, phone, password
change = {'default': ['Example Example Example', '+7-666-66-66', 'zapuskayte-gusya@yandex.ru'],
          'all-empty': ['', '', ''],
          'weird-symbols': ["!#$%&'*+-/=?^_`{|}~(),:;<>@[]", "!#$%&'*+-/=?^_`{|}~(),:;<>@[]",
                            "!#$%&'*+-/=?^_`{|}~(),:;<>@[]"],
          'long': ['a'*1000, '6'*1000, 'a'*1000]
          }

# goal, url, name, sex, age, geography, behavior,
# interests, context, segments, schedule_of_display,
# schedule_of_company, model, frmt, path1, path2
campaign = {}