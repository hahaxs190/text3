[app]

# (str) Title of your application
title = 服务器工具

# (str) Package name
package.name = servertool

# (str) Package domain (needed for android/ios packaging)
package.domain = org.servertool

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs =

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,numpy,requests,android

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services =

#
# OSX Specific
#
#
# author = © Copyright Info
#
# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names: 
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray, 
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy, 
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format. 
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ 
# for general documentation. 
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = %(source.dir)s/data/presplash.json

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#android.adaptive_icon_background = %(source.dir)s/data/icon_background.png
#android.adaptive_icon_foreground = %(source.dir)s/data/icon_foreground.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
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
# down the build process.
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src = 

# (list) Android AAR archives to add
#android.add_aars = 

# (list) Put these files or directories in the apk assets directory.
#android.add_assets = 

# (list) Put these files or directories in the apk res directory.
#android.add_resources = 

# (list) Directory of Java files to add to the android project
#android.add_java_dir = 

# (str) java_dir is deprecated, use android.add_java_dir instead
#android.java_dir = 

# (str) Android app version to use
# android.version_name = 

# (int) Android version code to use
# android.version_code = 

# (list) Android application meta-data to set (key=value format)
#android.meta_data = 

# (list) Android library project to add (will be added in the
src directory of the resulting android project)
#android.library_references = 

# (list) Android shared libraries which will be added to the libs directory
# of the apk
#android.add_libs_armeabi_v7a = libs/android/armeabi-v7a/*.so
#android.add_libs_arm64_v8a = libs/android/arm64-v8a/*.so
#android.add_libs_x86 = libs/android/x86/*.so
#android.add_libs_x86_64 = libs/android/x86_64/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application tags to set (key=value format)
#android.application_tags = 

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url = https://github.com/kivy/python-for-android

# (str) python-for-android fork to use in case if p4a.url is not the default one
#p4a.fork = kivy

# (str) python-for-android branch to use
#p4a.branch = master

# (str) python-for-android specific commit to use
#p4a.commit = 

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes = 

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future, it will be the default behaviour to use the setup.py" says p4a
#android.use_setup_py = False

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
#ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
#ios.ios_deploy_branch = 1.10.0

# (bool) Whether or not to sign the code
#ios.codesign.allowed = False

# (str) Name of the certificate to use for signing the app
#ios.codesign.certificate = 

# (str) The development team name to use for signing the app
#ios.codesign.team_id = 

# (str) The provisioning profile to use for signing the app
#ios.codesign.provisioning_profile = 

# (str) The bundle identifier to use for signing the app
#ios.bundle_id = 

# (str) The URL to the icon of the application
#ios.icon_url = 

#
# Debian specific
#

# (str) Maintainer of the debian package
#maintainer =

# (str) Email of the maintainer
#maintainer.email =

# (str) License of the application
#license =

# (str) Homepage of the application
#homepage =

#
# Docker specific
#

# (str) The docker image to use for the build environment
#docker.image = kivy/buildozer

#
# Buildozer specific
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. apk, ipa)
# bin_dir = ./bin

# (list) List of plugins to use
#plugins = 
# plugins.android = 
# plugins.ios = 

# (bool) If False, use twitter bootstrap instead of the default theme
# Android only
#bootstrap_materialdesign = True

# (str) The default language for the app
# i18n.default_language = en

# (list) The languages supported by the app
# i18n.languages = en

# (str) The path to the directory containing the translation files
# i18n.source_dir = ./locale

# (str) The path to the directory to store the compiled translation files
# i18n.dest_dir = ./app/locale

# (bool) Enable AndroidX support
#android.enable_androidx = True

# (list) Enable AndroidX support for these libraries
#android.enable_androidx_libraries = 

# (bool) If True, the APK will be generated with split per ABIs.
#android.split_apk = False

# (list) The ABIs to include in the split APKs
#android.split_apk_abis = armeabi-v7a, arm64-v8a

# (bool) If True, the APK will be generated with split per languages.
#android.split_langs = False

# (list) The languages to include in the split APKs
#android.split_langs = en, es

# (bool) If True, the APK will be generated with split per density.
#android.split_density = False

# (list) The densities to include in the split APKs
#android.split_density = xxxhdpi

# (str) The path to the Android keystore file
#android.keystore_path =

# (str) The alias of the Android keystore
#android.keystore_alias =

# (str) The password of the Android keystore
#android.keystore_password =

# (str) The path to the Android keystore key password
#android.key_password =

# (bool) If True, the APK will be signed with the release key
#android.release = False

# (str) The path to the Android release keystore file
#android.release_keystore_path =

# (str) The alias of the Android release keystore
#android.release_keystore_alias =

# (str) The password of the Android release keystore
#android.release_keystore_password =

# (str) The path to the Android release key password
#android.release_key_password =

# (str) The path to the Android debug keystore file
#android.debug_keystore_path =

# (str) The alias of the Android debug keystore
#android.debug_keystore_alias =

# (str) The password of the Android debug keystore
#android.debug_keystore_password =

# (str) The path to the Android debug key password
#android.debug_key_password =

# (str) The path to the Android signing config file
#android.signing_config_path =

# (int) The minimum Android SDK version to target
#android.min_sdk_version = 21

# (int) The target Android SDK version to target
#android.target_sdk_version = 31

# (int) The Android SDK version to use for building
#android.build_sdk_version = 31

# (str) The Android NDK version to use for building
#android.ndk_version = 23

# (int) The Android NDK API version to use for building
#android.ndk_api_version = 21

# (str) The Android build tools version to use for building
#android.build_tools_version = 31.0.0

# (str) The Android gradle plugin version to use for building
#android.gradle_plugin_version = 4.2.2

# (str) The Android gradle version to use for building
#android.gradle_version = 7.0.2

# (str) The path to the Android gradle wrapper
#android.gradle_wrapper_path =

# (bool) If True, the app will be built with the Android App Bundle format
#android.build_apk = True
#android.build_aab = False

# (str) The path to the Android App Bundle output
#android.aab_path =

# (str) The path to the Android APK output
#android.apk_path =

# (str) The path to the Android mapping.txt file
#android.mapping_path =

# (str) The path to the Android R8 configuration file
#android.r8_config_path =

# (bool) If True, the app will be built with the Android R8 code shrinker
#android.use_r8 = False

# (bool) If True, the app will be built with the Android ProGuard code shrinker
#android.use_proguard = False

# (str) The path to the Android ProGuard configuration file
#android.proguard_config_path =

# (bool) If True, the app will be built with the Android multidex support
#android.use_multidex = False

# (int) The minimum number of methods required to enable multidex
#android.multidex_min_methods = 65536

# (str) The path to the Android multidex configuration file
#android.multidex_config_path =

# (bool) If True, the app will be built with the Android Jetifier tool
#android.use_jetifier = False

# (str) The path to the Android Jetifier configuration file
#android.jetifier_config_path =

# (bool) If True, the app will be built with the Android Core Library Desugaring
#android.use_core_library_desugaring = False

# (str) The path to the Android Core Library Desugaring configuration file
#android.core_library_desugaring_config_path =

# (bool) If True, the app will be built with the Android resource shrinker
#android.use_resource_shrinker = False

# (str) The path to the Android resource shrinker configuration file
#android.resource_shrinker_config_path =

# (bool) If True, the app will be built with the Android vector drawable support
#android.use_vector_drawables = False

# (bool) If True, the app will be built with the Android animated vector drawable support
#android.use_animated_vector_drawables = False

# (bool) If True, the app will be built with the Android runtime permissions
#android.use_runtime_permissions = False

# (list) The Android permissions to request at runtime
#android.runtime_permissions = 

# (bool) If True, the app will be built with the Android Google Play Services
#android.use_google_play_services = False

# (str) The Google Play Services version to use
#android.google_play_services_version =

# (bool) If True, the app will be built with the Android Google Play Services Ads
#android.use_google_play_services_ads = False

# (str) The Google Play Services Ads version to use
#android.google_play_services_ads_version =

# (bool) If True, the app will be built with the Android Google Play Services Analytics
#android.use_google_play_services_analytics = False

# (str) The Google Play Services Analytics version to use
#android.google_play_services_analytics_version =

# (bool) If True, the app will be built with the Android Google Play Services Location
#android.use_google_play_services_location = False

# (str) The Google Play Services Location version to use
#android.google_play_services_location_version =

# (bool) If True, the app will be built with the Android Firebase
#android.use_firebase = False

# (str) The Firebase version to use
#android.firebase_version =

# (bool) If True, the app will be built with the Android Firebase Analytics
#android.use_firebase_analytics = False

# (str) The Firebase Analytics version to use
#android.firebase_analytics_version =

# (bool) If True, the app will be built with the Android Firebase Cloud Messaging
#android.use_firebase_messaging = False

# (str) The Firebase Cloud Messaging version to use
#android.firebase_messaging_version =

# (bool) If True, the app will be built with the Android Firebase Crashlytics
#android.use_firebase_crashlytics = False

# (str) The Firebase Crashlytics version to use
#android.firebase_crashlytics_version =

# (bool) If True, the app will be built with the Android Firebase Performance Monitoring
#android.use_firebase_performance = False

# (str) The Firebase Performance Monitoring version to use
#android.firebase_performance_version =

# (bool) If True, the app will be built with the Android Firebase Remote Config
#android.use_firebase_remote_config = False

# (str) The Firebase Remote Config version to use
#android.firebase_remote_config_version =

# (bool) If True, the app will be built with the Android Firebase In-App Messaging
#android.use_firebase_in_app_messaging = False

# (str) The Firebase In-App Messaging version to use
#android.firebase_in_app_messaging_version =

# (bool) If True, the app will be built with the Android Firebase Dynamic Links
#android.use_firebase_dynamic_links = False

# (str) The Firebase Dynamic Links version to use
#android.firebase_dynamic_links_version =

# (bool) If True, the app will be built with the Android Firebase App Indexing
#android.use_firebase_app_indexing = False

# (str) The Firebase App Indexing version to use
#android.firebase_app_indexing_version =

# (bool) If True, the app will be built with the Android Firebase Authentication
#android.use_firebase_authentication = False

# (str) The Firebase Authentication version to use
#android.firebase_authentication_version =

# (bool) If True, the app will be built with the Android Firebase Realtime Database
#android.use_firebase_database = False

# (str) The Firebase Realtime Database version to use
#android.firebase_database_version =

# (bool) If True, the app will be built with the Android Firebase Cloud Firestore
#android.use_firebase_firestore = False

# (str) The Firebase Cloud Firestore version to use
#android.firebase_firestore_version =

# (bool) If True, the app will be built with the Android Firebase Storage
#android.use_firebase_storage = False

# (str) The Firebase Storage version to use
#android.firebase_storage_version =

# (bool) If True, the app will be built with the Android Firebase Functions
#android.use_firebase_functions = False

# (str) The Firebase Functions version to use
#android.firebase_functions_version =

# (bool) If True, the app will be built with the Android Firebase Machine Learning
#android.use_firebase_ml = False

# (str) The Firebase Machine Learning version to use
#android.firebase_ml_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit
#android.use_firebase_ml_kit = False

# (str) The Firebase ML Kit version to use
#android.firebase_ml_kit_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Vision
#android.use_firebase_ml_kit_vision = False

# (str) The Firebase ML Kit Vision version to use
#android.firebase_ml_kit_vision_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Natural Language
#android.use_firebase_ml_kit_natural_language = False

# (str) The Firebase ML Kit Natural Language version to use
#android.firebase_ml_kit_natural_language_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Custom Model
#android.use_firebase_ml_kit_custom_model = False

# (str) The Firebase ML Kit Custom Model version to use
#android.firebase_ml_kit_custom_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Image Labeling
#android.use_firebase_ml_kit_image_labeling = False

# (str) The Firebase ML Kit Image Labeling version to use
#android.firebase_ml_kit_image_labeling_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Face Detection
#android.use_firebase_ml_kit_face_detection = False

# (str) The Firebase ML Kit Face Detection version to use
#android.firebase_ml_kit_face_detection_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Text Recognition
#android.use_firebase_ml_kit_text_recognition = False

# (str) The Firebase ML Kit Text Recognition version to use
#android.firebase_ml_kit_text_recognition_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Barcode Scanning
#android.use_firebase_ml_kit_barcode_scanning = False

# (str) The Firebase ML Kit Barcode Scanning version to use
#android.firebase_ml_kit_barcode_scanning_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Object Detection and Tracking
#android.use_firebase_ml_kit_object_detection = False

# (str) The Firebase ML Kit Object Detection and Tracking version to use
#android.firebase_ml_kit_object_detection_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Language Identification
#android.use_firebase_ml_kit_language_identification = False

# (str) The Firebase ML Kit Language Identification version to use
#android.firebase_ml_kit_language_identification_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Smart Reply
#android.use_firebase_ml_kit_smart_reply = False

# (str) The Firebase ML Kit Smart Reply version to use
#android.firebase_ml_kit_smart_reply_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Translate
#android.use_firebase_ml_kit_translate = False

# (str) The Firebase ML Kit Translate version to use
#android.firebase_ml_kit_translate_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Entity Extraction
#android.use_firebase_ml_kit_entity_extraction = False

# (str) The Firebase ML Kit Entity Extraction version to use
#android.firebase_ml_kit_entity_extraction_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit Model Interpreter
#android.use_firebase_ml_kit_model_interpreter = False

# (str) The Firebase ML Kit Model Interpreter version to use
#android.firebase_ml_kit_model_interpreter_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge
#android.use_firebase_ml_kit_automl_vision_edge = False

# (str) The Firebase ML Kit AutoML Vision Edge version to use
#android.firebase_ml_kit_automl_vision_edge_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language
#android.use_firebase_ml_kit_automl_natural_language = False

# (str) The Firebase ML Kit AutoML Natural Language version to use
#android.firebase_ml_kit_automl_natural_language_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision
#android.use_firebase_ml_kit_automl_vision = False

# (str) The Firebase ML Kit AutoML Vision version to use
#android.firebase_ml_kit_automl_vision_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Entity Extraction
#android.use_firebase_ml_kit_automl_natural_language_entity_extraction = False

# (str) The Firebase ML Kit AutoML Natural Language Entity Extraction version to use
#android.firebase_ml_kit_automl_natural_language_entity_extraction_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Smart Reply
#android.use_firebase_ml_kit_automl_natural_language_smart_reply = False

# (str) The Firebase ML Kit AutoML Natural Language Smart Reply version to use
#android.firebase_ml_kit_automl_natural_language_smart_reply_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Translate
#android.use_firebase_ml_kit_automl_natural_language_translate = False

# (str) The Firebase ML Kit AutoML Natural Language Translate version to use
#android.firebase_ml_kit_automl_natural_language_translate_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Image Labeling
#android.use_firebase_ml_kit_automl_vision_edge_image_labeling = False

# (str) The Firebase ML Kit AutoML Vision Edge Image Labeling version to use
#android.firebase_ml_kit_automl_vision_edge_image_labeling_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Object Detection and Tracking
#android.use_firebase_ml_kit_automl_vision_edge_object_detection = False

# (str) The Firebase ML Kit AutoML Vision Edge Object Detection and Tracking version to use
#android.firebase_ml_kit_automl_vision_edge_object_detection_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Image Labeling
#android.use_firebase_ml_kit_automl_vision_image_labeling = False

# (str) The Firebase ML Kit AutoML Vision Image Labeling version to use
#android.firebase_ml_kit_automl_vision_image_labeling_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Object Detection and Tracking
#android.use_firebase_ml_kit_automl_vision_object_detection = False

# (str) The Firebase ML Kit AutoML Vision Object Detection and Tracking version to use
#android.firebase_ml_kit_automl_vision_object_detection_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Entity Extraction Model
#android.use_firebase_ml_kit_automl_natural_language_entity_extraction_model = False

# (str) The Firebase ML Kit AutoML Natural Language Entity Extraction Model version to use
#android.firebase_ml_kit_automl_natural_language_entity_extraction_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Smart Reply Model
#android.use_firebase_ml_kit_automl_natural_language_smart_reply_model = False

# (str) The Firebase ML Kit AutoML Natural Language Smart Reply Model version to use
#android.firebase_ml_kit_automl_natural_language_smart_reply_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Translate Model
#android.use_firebase_ml_kit_automl_natural_language_translate_model = False

# (str) The Firebase ML Kit AutoML Natural Language Translate Model version to use
#android.firebase_ml_kit_automl_natural_language_translate_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Image Labeling Model
#android.use_firebase_ml_kit_automl_vision_edge_image_labeling_model = False

# (str) The Firebase ML Kit AutoML Vision Edge Image Labeling Model version to use
#android.firebase_ml_kit_automl_vision_edge_image_labeling_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model
#android.use_firebase_ml_kit_automl_vision_edge_object_detection_model = False

# (str) The Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model version to use
#android.firebase_ml_kit_automl_vision_edge_object_detection_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Image Labeling Model
#android.use_firebase_ml_kit_automl_vision_image_labeling_model = False

# (str) The Firebase ML Kit AutoML Vision Image Labeling Model version to use
#android.firebase_ml_kit_automl_vision_image_labeling_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Object Detection and Tracking Model
#android.use_firebase_ml_kit_automl_vision_object_detection_model = False

# (str) The Firebase ML Kit AutoML Vision Object Detection and Tracking Model version to use
#android.firebase_ml_kit_automl_vision_object_detection_model_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Entity Extraction Model Builder
#android.use_firebase_ml_kit_automl_natural_language_entity_extraction_model_builder = False

# (str) The Firebase ML Kit AutoML Natural Language Entity Extraction Model Builder version to use
#android.firebase_ml_kit_automl_natural_language_entity_extraction_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Smart Reply Model Builder
#android.use_firebase_ml_kit_automl_natural_language_smart_reply_model_builder = False

# (str) The Firebase ML Kit AutoML Natural Language Smart Reply Model Builder version to use
#android.firebase_ml_kit_automl_natural_language_smart_reply_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Translate Model Builder
#android.use_firebase_ml_kit_automl_natural_language_translate_model_builder = False

# (str) The Firebase ML Kit AutoML Natural Language Translate Model Builder version to use
#android.firebase_ml_kit_automl_natural_language_translate_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Image Labeling Model Builder
#android.use_firebase_ml_kit_automl_vision_edge_image_labeling_model_builder = False

# (str) The Firebase ML Kit AutoML Vision Edge Image Labeling Model Builder version to use
#android.firebase_ml_kit_automl_vision_edge_image_labeling_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Builder
#android.use_firebase_ml_kit_automl_vision_edge_object_detection_model_builder = False

# (str) The Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Builder version to use
#android.firebase_ml_kit_automl_vision_edge_object_detection_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Image Labeling Model Builder
#android.use_firebase_ml_kit_automl_vision_image_labeling_model_builder = False

# (str) The Firebase ML Kit AutoML Vision Image Labeling Model Builder version to use
#android.firebase_ml_kit_automl_vision_image_labeling_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Object Detection and Tracking Model Builder
#android.use_firebase_ml_kit_automl_vision_object_detection_model_builder = False

# (str) The Firebase ML Kit AutoML Vision Object Detection and Tracking Model Builder version to use
#android.firebase_ml_kit_automl_vision_object_detection_model_builder_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Entity Extraction Model Evaluator
#android.use_firebase_ml_kit_automl_natural_language_entity_extraction_model_evaluator = False

# (str) The Firebase ML Kit AutoML Natural Language Entity Extraction Model Evaluator version to use
#android.firebase_ml_kit_automl_natural_language_entity_extraction_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Smart Reply Model Evaluator
#android.use_firebase_ml_kit_automl_natural_language_smart_reply_model_evaluator = False

# (str) The Firebase ML Kit AutoML Natural Language Smart Reply Model Evaluator version to use
#android.firebase_ml_kit_automl_natural_language_smart_reply_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Translate Model Evaluator
#android.use_firebase_ml_kit_automl_natural_language_translate_model_evaluator = False

# (str) The Firebase ML Kit AutoML Natural Language Translate Model Evaluator version to use
#android.firebase_ml_kit_automl_natural_language_translate_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Image Labeling Model Evaluator
#android.use_firebase_ml_kit_automl_vision_edge_image_labeling_model_evaluator = False

# (str) The Firebase ML Kit AutoML Vision Edge Image Labeling Model Evaluator version to use
#android.firebase_ml_kit_automl_vision_edge_image_labeling_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Evaluator
#android.use_firebase_ml_kit_automl_vision_edge_object_detection_model_evaluator = False

# (str) The Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Evaluator version to use
#android.firebase_ml_kit_automl_vision_edge_object_detection_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Image Labeling Model Evaluator
#android.use_firebase_ml_kit_automl_vision_image_labeling_model_evaluator = False

# (str) The Firebase ML Kit AutoML Vision Image Labeling Model Evaluator version to use
#android.firebase_ml_kit_automl_vision_image_labeling_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Object Detection and Tracking Model Evaluator
#android.use_firebase_ml_kit_automl_vision_object_detection_model_evaluator = False

# (str) The Firebase ML Kit AutoML Vision Object Detection and Tracking Model Evaluator version to use
#android.firebase_ml_kit_automl_vision_object_detection_model_evaluator_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Entity Extraction Model Trainer
#android.use_firebase_ml_kit_automl_natural_language_entity_extraction_model_trainer = False

# (str) The Firebase ML Kit AutoML Natural Language Entity Extraction Model Trainer version to use
#android.firebase_ml_kit_automl_natural_language_entity_extraction_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Smart Reply Model Trainer
#android.use_firebase_ml_kit_automl_natural_language_smart_reply_model_trainer = False

# (str) The Firebase ML Kit AutoML Natural Language Smart Reply Model Trainer version to use
#android.firebase_ml_kit_automl_natural_language_smart_reply_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Natural Language Translate Model Trainer
#android.use_firebase_ml_kit_automl_natural_language_translate_model_trainer = False

# (str) The Firebase ML Kit AutoML Natural Language Translate Model Trainer version to use
#android.firebase_ml_kit_automl_natural_language_translate_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Image Labeling Model Trainer
#android.use_firebase_ml_kit_automl_vision_edge_image_labeling_model_trainer = False

# (str) The Firebase ML Kit AutoML Vision Edge Image Labeling Model Trainer version to use
#android.firebase_ml_kit_automl_vision_edge_image_labeling_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Trainer
#android.use_firebase_ml_kit_automl_vision_edge_object_detection_model_trainer = False

# (str) The Firebase ML Kit AutoML Vision Edge Object Detection and Tracking Model Trainer version to use
#android.firebase_ml_kit_automl_vision_edge_object_detection_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Image Labeling Model Trainer
#android.use_firebase_ml_kit_automl_vision_image_labeling_model_trainer = False

# (str) The Firebase ML Kit AutoML Vision Image Labeling Model Trainer version to use
#android.firebase_ml_kit_automl_vision_image_labeling_model_trainer_version =

# (bool) If True, the app will be built with the Android Firebase ML Kit AutoML Vision Object Detection and Tracking Model Trainer
#android.use_firebase_ml_kit_automl_vision_object_detection_model_trainer = False

# (str) The Firebase ML Kit AutoML Vision Object Detection and Tracking Model Trainer version to use
#android.firebase_ml_kit_automl_vision_object_detection_model_trainer_version =