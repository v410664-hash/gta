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

# --- Додайте або оновіть ці рядки для автозавантаження SDK ---
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
# -------------------------------------------------------------

android.androidx = True
p4a.branch = master
android.build_mode = debug

[buildozer]
log_level = 2
warn_root = 1
bin_dir = ./bin
