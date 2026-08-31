[app]

# (str) Title of your application
title = Конструктор розкладу БЗВП

# (str) Package name
package.name = bzvp_schedule

# (str) Package domain (needed for android packaging)
package.domain = org.schedule

# (list) Source files to include (let it include python and kv files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to exclude (let it exclude specific files)
source.exclude_exts = spec

# (list) List of directory to exclude from distribution
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions in glob format
source.exclude_patterns = license, images/*.jpg

# --- ПІДКЛЮЧЕННЯ PYTHON 3.10 ТА KIVY ---
# (str) Application versioning
version = 1.0

# (list) Application requirements
# Вказуємо чітко python3 та kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services =

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for Android)
#android.presplash_color = #FFFFFF

# (string) Adaptive icon background color (android 8.0+)
#android.adaptive_icon_background = #FFFFFF

# (list) Permissions
# Дозволи на читання та запис пам'яті телефону для завантаження та збереження JSON
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (list) Features (optional)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API to use.
#android.ndk_api = 21

# (bool) Use Android X
android.androidx = True

# (list) Graphic API to use ('gles2' or 'opengl' - default is gles2)
#android.graphics = gles2

# (str) python-for-android branch to use
p4a.branch = master

# (str) OUYA Console support
#ouya.console.supported = False

# (str) XML extensions to add to AndroidManifest.xml
#android.manifest_xml = p4a-recipes

# (str) Intent filters to add to AndroidManifest.xml
#android.manifest_intent_filters =

# (string) format to building. Can be 'apk' or 'aab'
android.build_mode = debug


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact storage
bin_dir = ./bin
