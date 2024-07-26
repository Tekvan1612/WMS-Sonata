import os
import sys
import ctypes

def load_python_dll():
    possible_paths = [
        os.path.join(os.path.dirname(sys.executable), 'python312.dll'),
        'C:\\Program Files\\Python312\\python312.dll',
        'C:\\Program Files\\Python\\python312.dll',
    ]

    for path in possible_paths:
        if os.path.exists(path):
            ctypes.windll.LoadLibrary(path)
            break
    else:
        raise FileNotFoundError("Python DLL not found in any of the expected locations.")

if __name__ == '__main__':
    load_python_dll()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sonata_WMS_finale.settings')
    os.environ['RUN_MAIN'] = 'true'  # Disable autoreload

    # Ensure Django setup is called
    import django
    django.setup()

    from django.core.management import call_command
    call_command('runserver', '0.0.0.0:8000')
