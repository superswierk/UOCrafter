# setup.py
from distutils.core import setup
import py2exe
import sys

# Użyj tej samej logiki do uzyskania pełnej wersji co w GitHub Actions
# Musisz dostosować, jak ta zmienna jest przekazywana do setup.py
# W GitHub Actions, możesz przekazać ją jako zmienną środowiskową,
# a następnie odczytać ją tutaj.
# Poniżej zakładam, że będziesz przekazywać ją jako argument linii komend
# lub zmienną środowiskową do skryptu setup.py
# Dla uproszczenia w setup.py, możemy założyć, że to będzie stała wartość
# lub pobierzemy ją z argumentów, jeśli zdecydujesz się na bardziej złożone podejście.
# Na potrzeby tego przykładu, upraszczamy wersję do odczytu z kontekstu budowania
# co nie jest idealne, ale pozwoli na uruchomienie.
# Idealnie, Twoja wersja byłaby np. w oddzielnym pliku version.py lub przekazana.

# Na potrzeby tego setup.py, załóżmy, że wersja jest stała lub zostanie
# podmieniona w czasie budowania przez skrypt w GitHub Actions.
# Prostsze podejście to:
# from UOCrafter import __version__ # jeśli masz wersję w skrypcie głównym
# lub użyj zmiennej środowiskowej
try:
    # Pobieranie wersji ze zmiennej środowiskowej ustawionej przez GitHub Actions
    FULL_VERSION = sys.argv[sys.argv.index('--version-build') + 1]
    # Usuwamy argumenty, aby py2exe ich nie interpretował
    sys.argv.remove('--version-build')
    sys.argv.remove(FULL_VERSION)
except (ValueError, IndexError):
    FULL_VERSION = "0.0.0.0" # Domyślna wersja na wypadek braku argumentu

# Jeśli używasz ikon, musisz je również podać.
# Pliki danych (np. grafiki, dane konfiguracyjne) również muszą być dołączone.
# Przykład dla plików danych: data_files=[("my_data_folder", ["my_data_folder/data.txt"])]

setup(
    windows=[
        {
            "script": "UOCrafter.py",
            "icon_resources": [(1, "icon.ico")], # Upewnij się, że icon.ico jest w tym samym katalogu
            "version": FULL_VERSION.lstrip('v').replace('.', ','), # Format 1,2,3,4
            "product_version": FULL_VERSION.lstrip('v').replace('.', ','),
            "comments": "UOCrafter GUI Tool",
            "company_name": "RichRichie",
            "file_description": "UOCrafter GUI Tool",
            "internal_name": "UOCrafter",
            "original_filename": "UOCrafter.exe",
            "product_name": "UOCrafter Crafting Assistant",
        }
    ],
    options={
        "py2exe": {
            "bundle_files": 1, # 1 dla pojedynczego pliku EXE (wszystko w jednym)
            "compressed": True,
            "optimize": 2,
            "includes": ["tkinter"], # Dodaj tutaj inne moduły, jeśli py2exe ich nie znajdzie
            "packages": [], # Dodaj pakiety, jeśli używasz
            "dist_dir": "dist_py2exe" # Katalog wyjściowy
        }
    },
    zipfile=None, # Nie używamy oddzielnego pliku ZIP wewnątrz EXE
)