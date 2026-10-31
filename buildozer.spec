[app]

# (str) Title of your application
title = Amie AI

# (str) Package name
package.name = amieai

# (str) Package domain (needed for android/ios packaging)
package.domain = org.amieai

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# (list) List of inclusions using patterns
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .git, .github, .buildozer

# (str) Application versioning (method 1)
version = 0.1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,plyer,android,pyjnius,openssl,requests,urllib3,certifi,charset-normalizer,idna

# (str) Custom source folders for requirements
# Requirements listed here will be searched for in these directories first
#requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,VIBRATE,RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android App Interface.
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for possible values
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please ensure all these gradle repositories have a unique name
# android.gradle_repositories = repository_name1:repo_url1, repository_name2:repo_url2

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to $(builddir)/src/main/res/xml/ for use with intent-filter
#android.res_xml = path/to/xml1.xml,path/to/xml2.xml

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on while the app is running or not
#android.wakelock = False

# (list) Android application meta-data to add (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# android.library.reference.N format that gradle uses).
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This takes a map of the placeholders in the XML and their replacements.
#android.manifest_placeholders = [localApplicationId:'android:label=@string/app_name']

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android branch to use, if not master, useful to try something new.
#p4a.branch = master

# (str) python-for-android specific bootstrap to use
#p4a.bootstrap = sdl2

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port to use for serving any artifacts for your package (will be used for the URL)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to the setup.py of the
# app (and thus python-for-android) - this is a temporary work-around for some
# packages.
# --use-setup-py forces use of a setup.py labelled APP (inside the APP project)
# --ignore-setup-py forces ignoring any setup.py that may exist in the APP project
# either will result in failure if they are not able to be used, so the default is
# currently --ignore-setup-py until a better solution is found.
# p4a.setup_py = true

# (str) extra command line arguments to pass when invoking python-for-android
#p4a.extra_args =

#
# iOS specific
#

# (str) Path to a custom icon
#ios.icon.icon = %(source.dir)s/icon.png

# (str) Path to a custom icon (iPad)
#ios.icon.icon_ipad = %(source.dir)s/icon_ipad.png

# (str) Path to a custom icon (iPhone retina)
#ios.icon.icon_iphone_retina = %(source.dir)s/icon_iphone_retina.png

# (str) Path to a custom icon (iPad retina)
#ios.icon.icon_ipad_retina = %(source.dir)s/icon_ipad_retina.png

# (str) Path to a custom splash
#ios.splash.image = %(source.dir)s/data/splash.png

# (str) Path to a custom storyboard
#ios.splash.storyboard = %(source.dir)s/data/splash.storyboard

# (bool) Whether or not to use an alternative launch storyboard
#ios.alternative_launch_storyboard = no

# (str) Path to a custom launch image
#ios.launch_image = %(source.dir)s/data/launch.png

# (list) List of resources to include
#ios.resources = 

# (str) The display name of the application
#ios.display_name = Amie AI

# (str) The identifier of the application
#ios.identifier = org.amieai

# (str) The version of the application
#ios.version = 0.1.0

# (str) The short version of the application
#ios.short_version = 0.1

# (str) The deployment target of the application
#ios.deployment_target = 9.0

# (str) The architecture of the application
#ios.arch = arm64

# (str) The orientation of the application
#ios.orientation = Portrait

# (bool) Whether or not to enable bitcode
#ios.enable_bitcode = no

# (bool) Whether or not to enable metal
#ios.enable_metal = no

# (str) Path to a custom entitlements file
#ios.entitlements = 

# (list) List of frameworks to include
#ios.frameworks = 

# (list) List of libraries to include
#ios.libraries = 

# (str) Path to a custom Info.plist
#ios.info_plist = 

# (str) Path to a custom launch storyboard
#ios.launch_storyboard = 

# (str) Path to a custom settings bundle
#ios.settings_bundle = 

# (str) Path to a custom icon set
#ios.icon_set = 

#
# OSX specific
#

# (str) Path to a custom icon
#osx.icon.icon = %(source.dir)s/icon.png

# (str) Path to a custom icon (retina)
#osx.icon.icon_retina = %(source.dir)s/icon_retina.png

# (str) Path to a custom icon (1024)
#osx.icon.icon_1024 = %(source.dir)s/icon_1024.png

# (str) Path to a custom splash
#osx.splash.image = %(source.dir)s/data/splash.png

# (str) The display name of the application
#osx.display_name = Amie AI

# (str) The identifier of the application
#osx.identifier = org.amieai

# (str) The version of the application
#osx.version = 0.1.0

# (str) The short version of the application
#osx.short_version = 0.1

# (str) The deployment target of the application
#osx.deployment_target = 10.14

# (str) The architecture of the application
#osx.arch = x86_64

# (str) The orientation of the application
#osx.orientation = Portrait

# (bool) Whether or not to enable bitcode
#osx.enable_bitcode = no

# (bool) Whether or not to enable metal
#osx.enable_metal = no

# (str) Path to a custom entitlements file
#osx.entitlements = 

# (list) List of frameworks to include
#osx.frameworks = 

# (list) List of libraries to include
#osx.libraries = 

# (str) Path to a custom Info.plist
#osx.info_plist = 

# (str) Path to a custom launch storyboard
#osx.launch_storyboard = 

# (str) Path to a custom settings bundle
#osx.settings_bundle = 

# (str) Path to a custom icon set
#osx.icon_set = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define multiple sections of the same type that will be used for
#    the same purpose. For example, you can define multiple [app] sections
#    for different environments (e.g. [app] for development, [app-production]
#    for production).
#
#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can define multiple profiles which will use different [app] sections
#    for different environments (e.g. [app] for development, [app-production]
#    for production).
#
#    -----------------------------------------------------------------------------
