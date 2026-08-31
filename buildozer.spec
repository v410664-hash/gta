[app]

title = Конструктор розкладу БЗВП
package.name = bzvp_schedule
package.domain = org.schedule
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.ndk_api = 24
android.accept_sdk_license = True
android.build_mode = debug

# Збираємо тільки під сучасні 64-бітні процесори, щоб уникнути помилок 32-бітних ліб
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_root = 1
bin_dir = ./bin
