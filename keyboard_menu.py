from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👤 Гражданам", callback_data="category_citizens")],
    [InlineKeyboardButton(text="💼 Бизнесу", callback_data="category_business")],
    [InlineKeyboardButton(text="🔥 Популярное", callback_data="category_popular")]
])

citizens_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🧒 Семья", callback_data="citizens_family")],
    [InlineKeyboardButton(text="🏥 Здравоохранение", callback_data="citizens_health")],
    [InlineKeyboardButton(text="📚 Образование", callback_data="citizens_education")]
])

family_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤔 Ребёнок", callback_data="family_child")],
    [InlineKeyboardButton(text="💍 Семейное положение", callback_data="family_marital")],
    [InlineKeyboardButton(text="🛡️ Опека и попечительство", callback_data="family_guardian")]
])

family_child_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация рождения за рубежом", url="https://egov.kz/cms/ru/services/child/pass33-2_mid")],
    [InlineKeyboardButton(text="Усыновление детей", url="https://egov.kz/cms/ru/services/child/pass79_mon")],
    [InlineKeyboardButton(text="Приемная семья и выплаты", url="https://egov.kz/cms/ru/services/child/pass82-1_mon")],
    [InlineKeyboardButton(text="Справка о рождении", url="https://egov.kz/cms/ru/services/child/e_020")],
    [InlineKeyboardButton(text="Изменения в актах", url="https://egov.kz/cms/ru/services/child/pass192_mu")]
])

family_marital_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация смерти", url="https://egov.kz/cms/ru/services/marital_status/pass015_mu")],
    [InlineKeyboardButton(text="Справка о заключении брака", url="https://egov.kz/cms/ru/services/marital_status/e_019")],
    [InlineKeyboardButton(text="Повторное свидетельство о рождении", url="https://egov.kz/cms/ru/services/marital_status/e_024")],
    [InlineKeyboardButton(text="Брак за рубежом", url="https://egov.kz/cms/ru/services/marital_status/pass33-4_mid")],
    [InlineKeyboardButton(text="Аннулирование записей", url="https://egov.kz/cms/ru/services/marital_status/pass30-2_mu")],
    [InlineKeyboardButton(text="Справка о брачной правоспособности", url="https://egov.kz/cms/ru/services/marital_status/pass108-3_mw")]
])

family_guardian_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Справки по опеке", url="https://egov.kz/cms/ru/services/guardianship/206pass_mon")],
    [InlineKeyboardButton(text="Усыновление детей (повтор)", url="https://egov.kz/cms/ru/services/guardianship/pass79_mon")],
    [InlineKeyboardButton(text="Компенсация за обучение на дому", url="https://egov.kz/cms/ru/services/guardianship/pass173_mtszn")],
    [InlineKeyboardButton(text="Пособие по инвалидности ребёнка", url="https://egov.kz/cms/ru/services/guardianship/pass158_mtszn")],
    [InlineKeyboardButton(text="Опека над взрослыми", url="https://egov.kz/cms/ru/services/guardianship/pass402013_mtszn")],
    [InlineKeyboardButton(text="Повторное св-во о разводе", url="https://egov.kz/cms/ru/services/guardianship/e_023")]
])

health_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Запись на вакцинацию", url="https://egov.kz/cms/ru/services/health_care/Zapis-na-vakcinaciyu")],
    [InlineKeyboardButton(text="🏠 Вызов врача на дом", url="https://egov.kz/cms/ru/services/health_care/496pass_mz")],
    [InlineKeyboardButton(text="📄 Информация об ОСМС", url="https://egov.kz/cms/ru/services/health_care/pass171-2_mz")],
    [InlineKeyboardButton(text="⌚ Запись на приём к врачу", url="https://egov.kz/cms/ru/services/health_care/495pass_mz")],
    [InlineKeyboardButton(text="🏥 Прикрепление к поликлинике", url="https://egov.kz/cms/ru/services/health_care/494pass_mz")],
    [InlineKeyboardButton(text="📏 Отказ/согласие на донорство", url="https://egov.kz/cms/ru/services/health_care/mzsr_132_1")],
    [InlineKeyboardButton(text="💲 Цены на лекарства", url="https://egov.kz/cms/ru/services/pharmaceutics/pass601013_mz")],
    [InlineKeyboardButton(text="📊 Предоставленные лекарства", url="https://egov.kz/cms/ru/services/pharmaceutics/pass710_mz")],
    [InlineKeyboardButton(text="🔢 Эффективность лекарств", url="https://egov.kz/cms/ru/services/pharmaceutics/153-3pass_mz")],
])

education_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎓 Детский сад", url="https://egov.kz/cms/ru/services/pre_school/037pass_mon")],
    [InlineKeyboardButton(text="📅 Очередь в сад", url="https://egov.kz/cms/ru/services/pre_school/199pass_mon")],
    [InlineKeyboardButton(text="🌐 Лицензирование", url="https://egov.kz/cms/ru/services/pre_school/204pass_mon")],
    [InlineKeyboardButton(text="📑 Экспертиза учебников", url="https://egov.kz/cms/ru/services/pre_school/pass206_mon")],
    [InlineKeyboardButton(text="🌟 Аттестация педагогов", url="https://egov.kz/cms/ru/services/pre_school/certification_1")],
    [InlineKeyboardButton(text="📖 Средняя школа", url="https://egov.kz/cms/ru/services/secondary_school/pass_30_17_mp")],
    [InlineKeyboardButton(text="✏️ Зачисление в 1 класс", url="https://egov.kz/cms/ru/services/secondary_school/pass_mp_203")],
    [InlineKeyboardButton(text="🏫 Спецшколы", url="https://egov.kz/cms/ru/services/secondary_school/pass73-3_mks")],
    [InlineKeyboardButton(text="🏀 ДЮСШ", url="https://egov.kz/cms/ru/services/secondary_school/pass73-4_mks")],
    [InlineKeyboardButton(text="🏛️ Конкурсы", url="https://egov.kz/cms/ru/services/secondary_school/konkurs_1")],
    [InlineKeyboardButton(text="🏫 Колледжи", url="https://egov.kz/cms/ru/services/professional_education/pr_5")],
    [InlineKeyboardButton(text="📃 Среднее образование", url="https://egov.kz/cms/ru/services/professional_education/185pass_mon")],
    [InlineKeyboardButton(text="🌐 Спецколледжи", url="https://egov.kz/cms/ru/services/professional_education/pass73-3_mks")],
    [InlineKeyboardButton(text="🏫 Вузы и последипломное", url="https://egov.kz/cms/ru/services/university_degree/pass_mon")],
    [InlineKeyboardButton(text="📚 Актуализация данных", url="https://egov.kz/cms/ru/services/university_degree/passP50_07_mp_mnvo")],
    [InlineKeyboardButton(text="🌐 Регистрация за рубежом", url="https://egov.kz/cms/ru/services/university_degree/6-51pass_mon")],
    [InlineKeyboardButton(text="🌎 Конкурсы за рубеж", url="https://egov.kz/cms/ru/services/university_degree/pass203_mon")],
])

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

jobs_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔍 Поиск работы", callback_data="jobs_search")],
    [InlineKeyboardButton(text="🏛 Госслужба", callback_data="jobs_public")]
])

jobs_search_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Справка о несудимости", url="https://egov.kz/cms/ru/services/job_search/e_004")],
    [InlineKeyboardButton(text="Постановка на учет", url="https://egov.kz/cms/ru/services/job_search/pass190-3_mtszn")],
    [InlineKeyboardButton(text="Помощь в поиске работы", url="https://egov.kz/cms/ru/services/job_search/pass177_mtszn")],
    [InlineKeyboardButton(text="Пособие по безработице", url="https://egov.kz/cms/ru/services/job_search/pass155_mtszn")]
])

jobs_public_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Конкурс на госслужбу", url="https://egov.kz/cms/ru/services/state_service/pass_25_07_mdgs")],
    [InlineKeyboardButton(text="Тестирование госслужащих", url="https://egov.kz/cms/ru/services/state_service/553pass_adgs")],
    [InlineKeyboardButton(text="Оценка личных качеств", url="https://egov.kz/cms/ru/services/state_service/pass_25_10_mdgs")]
])

social_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👴 Пенсии", callback_data="social_pension")],
    [InlineKeyboardButton(text="♿ Инвалидность", callback_data="social_disability")],
    [InlineKeyboardButton(text="👨‍👩‍👧‍👦 Поддержка семей", callback_data="social_family")],
    [InlineKeyboardButton(text="🚪 Безработица", callback_data="social_unemployed")]
])

social_pension_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назначение базовой пенсии", url="https://egov.kz/cms/ru/services/pension/pass152_mtszn")],
    [InlineKeyboardButton(text="Возврат пени", url="https://egov.kz/cms/ru/services/pension/passP6-72_mtszn")],
    [InlineKeyboardButton(text="Пенсия из ЕНПФ", url="https://egov.kz/cms/ru/services/pension/pass171-5_mtszn")]
])

social_disability_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Соцвыплаты", url="https://egov.kz/cms/ru/services/disabled_persons/pass172_mtszn")],
    [InlineKeyboardButton(text="Установление инвалидности", url="https://egov.kz/cms/ru/services/disabled_persons/pass159_mtszn")],
    [InlineKeyboardButton(text="Реабилитация", url="https://egov.kz/cms/ru/services/disabled_persons/pass170_mtszn")]
])

social_family_support_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Выплаты по потере кормильца", url="https://egov.kz/cms/ru/services/family_support/pass196_mtszn")],
    [InlineKeyboardButton(text="Жилпомощь", url="https://egov.kz/cms/ru/services/family_support/pass672_mir")],
    [InlineKeyboardButton(text="Пособие на детей с инвалидностью", url="https://egov.kz/cms/ru/services/family_support/pass158_mtszn")],
    [InlineKeyboardButton(text="Многодетным семьям", url="https://egov.kz/cms/ru/services/family_support/mtczn_00402014")]
])

social_unemployment_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Постановка на учет", url="https://egov.kz/cms/ru/services/for_unemployed/pass034_mtszn")],
    [InlineKeyboardButton(text="Выплаты при потере работы", url="https://egov.kz/cms/ru/services/for_unemployed/pass155_mtszn")],
    [InlineKeyboardButton(text="С дипломом в село", url="https://egov.kz/cms/ru/services/for_unemployed/pass180_msh")]
])


identity_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🪪 Паспорта и документы", callback_data="identity_passports")],
    [InlineKeyboardButton(text="📍 Регистрация и учет", callback_data="identity_registration")],
    [InlineKeyboardButton(text="🌐 Иностранные граждане", callback_data="identity_foreigners")],
    [InlineKeyboardButton(text="✈️ Выезд за границу", callback_data="identity_abroad")]
])

identity_passport_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Выдача удостоверения личности", url="https://egov.kz/cms/ru/services/passport/pass003_mvd")],
    [InlineKeyboardButton(text="Заказ паспорта за рубежом", url="https://egov.kz/cms/ru/services/passport/pass545_mid")]
])

identity_registration_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Учет по месту пребывания", url="https://egov.kz/cms/ru/services/registration/reg_grazhdan")],
    [InlineKeyboardButton(text="Учет по месту жительства", url="https://egov.kz/cms/ru/services/registration/pass001_mvd")],
    [InlineKeyboardButton(text="Снятие с учета", url="https://egov.kz/cms/ru/services/registration/002pass_mvd")]
])

identity_foreigner_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Разрешение на временное проживание", url="https://egov.kz/cms/ru/services/for_foreigners/00203002_mvd")],
    [InlineKeyboardButton(text="Вид на жительство", url="https://egov.kz/cms/ru/services/for_foreigners/012pass_mvd")],
    [InlineKeyboardButton(text="Региональная квота кандасов", url="https://egov.kz/cms/ru/services/for_foreigners/pass179-1_mtszn")]
])

identity_abroad_services = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация брака за рубежом", url="https://egov.kz/cms/ru/services/move_abroad/pass33-4_mid")],
    [InlineKeyboardButton(text="Разрешение на выезд", url="https://egov.kz/cms/ru/services/move_abroad/services_sr14")],
    [InlineKeyboardButton(text="Регистрация смерти за рубежом", url="https://egov.kz/cms/ru/services/move_abroad/pass33-8_mid")],
    [InlineKeyboardButton(text="Легализация документов", url="https://egov.kz/cms/ru/services/move_abroad/pass542_mid")]
])
