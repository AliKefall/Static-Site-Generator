import os
import shutil

def copy_files_recursive(source, destination):
    """
    Kaynak dizinindeki tüm dosyaları ve alt dizinleri hedefe kopyalar.
    """
    os.makedirs(destination, exist_ok=True)

    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)


        if os.path.isdir(source_item):
            copy_files_recursive(source_item, destination_item)

        else:
            shutil.copy(source_item, destination_item)
            print(f" * {source_item} -> {destination_item}")

