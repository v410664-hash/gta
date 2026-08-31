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

# Використання готових компонентів середовища GitHub замість завантаження з інтернету
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

[buildozer]
log_level = 2
warn_root = 1
bin_dir = ./bin
