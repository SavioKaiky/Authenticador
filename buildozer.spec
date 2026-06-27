[app]

# Título exibido no celular
title = Verifyx

# Nome do pacote (sem espaços, minúsculo)
package.name = authapp

# Domínio do pacote (padrão Android)
package.domain = org.authapp

# Pasta raiz do projeto
source.dir = .

# Arquivos a incluir
source.include_exts = py,png,jpg,kv,atlas,db

# Versão do app
version = 1.0.0

# Dependências Python
requirements = python3,kivy==2.3.1,https://github.com/kivymd/KivyMD/archive/master.zip,materialyoucolor,asynckivy,pyotp,sqlalchemy==2.0.41,typing_extensions

# Pasta de assets
# (deixar vazio usa o padrão)
presplash.filename = %(source.dir)s/assets/presplash.png
icon.filename = %(source.dir)s/assets/icon.png

# Orientação
orientation = portrait

# Permissões Android necessárias
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# API Android
android.api = 33
android.minapi = 21
android.ndk = 28c
android.sdk = 33

# Arquitetura (arm64-v8a para celulares modernos + armeabi-v7a para compatibilidade)
android.archs = armeabi-v7a

# Habilitar modo fullscreen
fullscreen = 0

[buildozer]

# Nível de log (0 = erro, 1 = info, 2 = debug)
log_level = 2

# Aviso de permissões
warn_on_root = 1
android.release_artifact = apk
android.keystore = authapp.jks
android.keystore_passwd = 190378
android.keyalias = authapp
android.keyalias_passwd = 190378
