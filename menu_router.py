from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboard_menu import (
    identity_menu,
    identity_passport_services,
    identity_registration_services,
    identity_foreigner_services,
    identity_abroad_services,
    menu_keyboard,
    citizens_menu,
    family_menu,
    family_child_services,
    family_marital_services,
    family_guardian_services,
    health_menu,
    education_menu,
    jobs_menu,
    jobs_search_services,
    jobs_public_services,
    social_menu,
    social_pension_services,
    social_disability_services,
    social_family_support_services,
    social_unemployment_services


)

router = Router()

@router.callback_query(F.data == "category_citizens")
async def show_citizens(callback: CallbackQuery):
    await callback.message.edit_text("👤 Гражданам:", reply_markup=citizens_menu)
    await callback.answer()


@router.callback_query(F.data == "citizens_family")
async def show_family(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F476 Семья:", reply_markup=family_menu)
    await callback.answer()

@router.callback_query(F.data == "family_child")
async def show_family_child(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F9D2 Услуги для ребёнка:", reply_markup=family_child_services)
    await callback.answer()

@router.callback_query(F.data == "family_marital")
async def show_family_marital(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F48D Семейное положение:", reply_markup=family_marital_services)
    await callback.answer()

@router.callback_query(F.data == "family_guardian")
async def show_family_guardian(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F6E1\ufe0f Опека и попечительство:", reply_markup=family_guardian_services)
    await callback.answer()

@router.callback_query(F.data == "citizens_health")
async def show_health(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F3E5 Здравоохранение:", reply_markup=health_menu)
    await callback.answer()



@router.callback_query(F.data == "citizens_education")
async def show_education(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F393 Образование:", reply_markup=education_menu)
    await callback.answer()



@router.callback_query(F.data == "citizens_jobs")
async def show_jobs(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F4BC Трудоустройство:", reply_markup=jobs_menu)
    await callback.answer()

@router.callback_query(F.data == "jobs_search")
async def show_jobs_search(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F50D Поиск работы:", reply_markup=jobs_search_services)
    await callback.answer()

@router.callback_query(F.data == "jobs_public")
async def show_jobs_public(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F4C5 Госслужба:", reply_markup=jobs_public_services)
    await callback.answer()

@router.callback_query(F.data == "citizens_social")
async def show_social(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F91D Соцобеспечение:", reply_markup=social_menu)
    await callback.answer()

@router.callback_query(F.data == "social_pension")
async def show_social_pension(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F9D3\u200D\U0001F9AF Пенсии:", reply_markup=social_pension_services)
    await callback.answer()

@router.callback_query(F.data == "social_disability")
async def show_social_dis(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F9BD Инвалидность:", reply_markup=social_disability_services)
    await callback.answer()

@router.callback_query(F.data == "social_family")
async def show_social_family(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F46A Поддержка семей:", reply_markup=social_family_support_services)
    await callback.answer()

@router.callback_query(F.data == "social_unemployed")
async def show_social_unem(callback: CallbackQuery):
    await callback.message.edit_text("\U0001F6AA Безработица:", reply_markup=social_unemployment_services)
    await callback.answer()
@router.callback_query(F.data == "citizens_identity")
async def show_identity(callback: CallbackQuery):
    await callback.message.edit_text("📄 Гражданство и миграция:", reply_markup=identity_menu)
    await callback.answer()

@router.callback_query(F.data == "identity_passports")
async def show_passports(callback: CallbackQuery):
    await callback.message.edit_text("🪪 Паспорта и документы:", reply_markup=identity_passport_services)
    await callback.answer()

@router.callback_query(F.data == "identity_registration")
async def show_registration(callback: CallbackQuery):
    await callback.message.edit_text("📍 Регистрация и учёт:", reply_markup=identity_registration_services)
    await callback.answer()

@router.callback_query(F.data == "identity_foreigners")
async def show_foreigners(callback: CallbackQuery):
    await callback.message.edit_text("🌐 Иностранные граждане:", reply_markup=identity_foreigner_services)
    await callback.answer()

@router.callback_query(F.data == "identity_abroad")
async def show_abroad(callback: CallbackQuery):
    await callback.message.edit_text("✈️ Выезд за границу:", reply_markup=identity_abroad_services)
    await callback.answer()
