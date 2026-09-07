""" Script de création du build et de l'installateur MSI pour Windows."""

from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [],
    "excludes": [],
    "include_files": ["fonctions/sync_fonctions.py",
                      "fonctions/config_windows.py",
                      "fonctions/utils.py",
                      "config.conf",
                      "ffmpeg.exe"],
}

msi_data = {
    "Icon": [
        ("IconId", "ressources/logo.ico"),
    ],
}

bdist_msi_options = {
    "add_to_path": True,
    "data": msi_data,
    "launch-on-finish": True,
}

executables = [
    Executable("soundcloud sync.py",
               base="gui",
               shortcut_dir="DesktopFolder",
               shortcut_name="SoundCloud Sync",
               icon="ressources/logo.ico")]

setup(
    name="SoundCloud Sync",
    version="1.3",
    description="Téléchargez et synchronisez vos musiques, playlists, albums et artistes SoundCloud localement.",
    executables=executables,
    options={"build_exe": build_exe_options,
             "bdist_msi": bdist_msi_options},
)