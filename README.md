# Проект SEL 2024 (1 курс)

## О проекте

Название - DuoCypher

### Описание
Полноценный курс по азбуке морзе с тестами и системой рейтинга.

### Состав команды
1) Ахмед Аль-Асри (teamlead, backend)
2) Филиппов Вадим (techlead, fronend, backend)
3) Дробышева Майя (frontend, backend)

### Требования (Use Case) для DuoCypher

Название проекта: DuoCypher

Описание проекта: DuoCypher — это интерактивное веб-приложение, предназначенное для эффективного изучения азбуки Морзе. Оно сочетает в себе образовательные уроки и тесты, позволяя пользователям не только учить азбуку Морзе, но и практиковаться и проверять свои знания. Приложение подходит как для начинающих, так и для более опытных пользователей.

---

#### Акторы:
1. Пользователь: Любой человек, который хочет изучать и практиковать азбуку Морзе.
2. Администратор: Лицо, ответственное за поддержание контента и управление приложением.

#### Функциональные требования:

1. Регистрация и аутентификация пользователей:
   - Пользователи могут создать учетную запись, используя свою электронную почту и пароль.
   - Пользователи могут входить и выходить из своих учетных записей.
   - Возможность восстановления пароля для пользователей, забывших свой пароль.

2. Управление профилем пользователя:
   - Пользователи могут просматривать и обновлять свои профили.
   - Пользователи могут отслеживать свой прогресс и просматривать результаты тестов.

3. Раздел "Уроки":
   - Предоставлять уроки по азбуке Морзе, охватывающие буквы, цифры и специальные символы.
   - Включать аудиопримеры для каждого символа.
   - Включать визуальные примеры (анимации или изображения), демонстрирующие сигналы азбуки Морзе.

4. Раздел "Тесты":
   - Тест на кодирование:
     - Отображать пользователю символ (букву, цифру или специальный символ).
     - Пользователь должен нажимать кнопку, чтобы воспроизвести азбуку Морзе для отображаемого символа.
     - Пользователь получает немедленную обратную связь.
   - Тест на декодирование:
     - Воспроизводить звук азбуки Морзе, представляющий символ.
     - Пользователь должен нажать правильный символ на клавиатуре.
     - Пользователь получает немедленную обратную связь.
   - Тесты должны быть доступны на разных уровнях сложности.

5. Система рейтингов:
   - Пользователи зарабатывают очки или значки в зависимости от своих результатов в тестах.
   - Таблица лидеров, показывающая лучших пользователей.
   - Пользователи могут видеть свой рейтинг по сравнению с другими.

6. Отслеживание прогресса:
   - Пользователи могут отслеживать свой учебный прогресс.
   - Визуальные индикаторы (например, полосы прогресса) для завершенных уроков и пройденных тестов.
   - Исторические данные о результатах тестов и успеваемости.

7. Панель администратора:
   - Администратор может добавлять, обновлять и удалять уроки.
   - Администратор может управлять пользователями (просмотр, редактирование и удаление учетных записей пользователей).
   - Администратор может просматривать общую статистику производительности и активности пользователей.

8. Управление контентом:
   - Администратор может загружать и управлять аудиофайлами для звуков азбуки Морзе.
   - Администратор может управлять визуальными примерами сигналов азбуки Морзе.

#### Нефункциональные требования:

1. Удобство использования:
   - Приложение должно быть легким в навигации и использовании.
   - Уроки и тесты должны быть четко структурированы и интуитивно понятны.

2. Производительность:
   - Приложение должно быстро загружаться и оперативно реагировать на действия пользователя.
   - Обратная связь в реальном времени во время тестов не должна иметь заметной задержки.

3. Безопасность:
   - Данные пользователей должны храниться надежно.
   - Механизмы аутентификации должны быть надежными для защиты учетных записей пользователей.
   - Следовать лучшим практикам безопасности веб-приложений для предотвращения уязвимостей.

4. Масштабируемость:
   - Приложение должно выдерживать одновременное использование несколькими пользователями без ухудшения производительности.
   - Легкость расширения для добавления новых уроков и тестов в будущем.

5. Совместимость:
   - Приложение должно работать на различных устройствах (настольные компьютеры, планшеты, смартфоны).
   - Поддержка различных веб-браузеров.
6. Доступность:
   - Обеспечить доступность приложения для пользователей с ограниченными возможностями.
   - Предоставлять альтернативный текст для визуального контента и обеспечить понятность аудиоконтента.

7. Надежность:
   - Приложение должно иметь высокую доступность.
   - Регулярные резервные копии для предотвращения потери данных.

---

#### Сценарии использования:

1. Регистрация пользователя:
   - Новый пользователь посещает сайт DuoCypher, нажимает "Зарегистрироваться", заполняет регистрационную форму и создает учетную запись.

2. Вход и выход из системы:
   - Зарегистрированный пользователь входит в свою учетную запись, используя электронную почту и пароль. По окончании сеанса выходит из учетной записи.

3. Просмотр и обновление профиля:
   - Пользователь переходит на страницу своего профиля, просматривает свой прогресс и результаты тестов, а также обновляет личную информацию при необходимости.

4. Изучение азбуки Морзе:
   - Пользователь выбирает урок, слушает аудиопримеры, смотрит визуальные демонстрации и практикуется в использовании азбуки Морзе для различных символов.

5. Прохождение теста на кодирование:
   - Пользователь выбирает тест на кодирование, видит символ и нажимает кнопку, чтобы воспроизвести соответствующий сигнал азбуки Морзе. Приложение предоставляет немедленную обратную связь по вводу пользователя.

6. Прохождение теста на декодирование:
   - Пользователь выбирает тест на декодирование, слушает звук азбуки Морзе и нажимает соответствующий символ на клавиатуре. Приложение предоставляет немедленную обратную связь по вводу пользователя.

7. Просмотр рейтинга и прогресса:
   - Пользователь проверяет свои очки, значки и положение в таблице лидеров. Также просматривает свой прогресс по урокам и тестам.

8. Администрирование контента:
   - Администратор входит в панель администратора, добавляет новый урок, загружает аудиофайлы и обновляет визуальные примеры. Также управляет учетными записями пользователей и мониторит общую статистику.

---

Этот набор требований и сценариев использования предоставляет всесторонний обзор функциональных возможностей и ожиданий для проекта DuoCypher.
