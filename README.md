# company

# Использование
Структура данных

  Филиалы (Branch): Адрес и короткое название

  Отделы (Department): Название, этаж, связь с филиалом

  Сотрудники (Employee): ФИО, должность, контактные данные

Примеры запросов (через shell)

python manage.py shell

from company.models import *

# 1. Количество менеджеров
Employee.objects.filter(position='Менеджер').count()

# 2. Сотрудники на 4-х этажах
Employee.objects.filter(department__floor=4)

# 3. Сотрудники в филиалах с ID 1 и 2
from django.db.models import Q
Employee.objects.filter(Q(department__branch_id=1) | Q(department__branch_id=2))

# 4. Поиск по году рождения
Employee.objects.filter(birth_date__year=1990)
