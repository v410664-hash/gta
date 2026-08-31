[app]

# Назва та пакет додатку
title = My Application
package.name =myapp
package.domain = org.example

# Головний файл коду
source.include_exts = py,png,jpg,kv,atlas
source.dir = .

# Необхідні бібліотеки (для Kivy обов'язково)
requirements = python3,kivy

# Версія
version = 0.1

# Орієнтація екрана (portrait, landscape або all)
orientation = portrait

# Права доступу (за потреби додай, наприклад, INTERNET)
android.permissions = INTERNET

# Налаштування SDK / NDK (стандартні значення)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
