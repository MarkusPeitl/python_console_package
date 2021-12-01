import os

#author = input("What is your name (author)? ")
#package = input("What is the name of your package? ")
author="max max"
package="new_package_name"

replacements = [
    ("python_console_package", package),
    ("entrypoint", package),
    ("Markus Peitl", author)
]

ignore_paths = [
    '.git'
]

def perform_replacements(text, replacements):
    new_text = text
    for replacement in replacements:
        new_text = new_text.replace(replacement[0], replacement[1])
    return new_text

for root, dirs, file_names in os.walk(".", topdown=True):

    is_filtered = any(ignore_path in root for ignore_path in ignore_paths)
    if not is_filtered:

        renamed_root_path = perform_replacements(root, replacements)
        if(root != renamed_root_path):
            print(renamed_root_path)
            os.rename(root, renamed_root_path)

for root, dirs, file_names in os.walk(".", topdown=True):

    is_filtered = any(ignore_path in root for ignore_path in ignore_paths)
    if not is_filtered:

        for file_name in file_names:
            path = os.path.join(root, file_name)
            out_path = perform_replacements(path, replacements)

            if(path != out_path):
                os.rename(path, out_path)

for root, dirs, file_names in os.walk(".", topdown=True):

    is_filtered = any(ignore_path in root for ignore_path in ignore_paths)
    if not is_filtered:
    
        for file_name in file_names:
            path = os.path.join(root, file_name)
            try:

                content = None
                with open(path, 'r') as file:
                    content = file.read()

                if(content is not None and len(content) > 0):

                    with open(path, 'w+') as file:
                        content = perform_replacements(content, replacements)

                        if(content is not None and len(content) > 0):
                            file.write(content)

            except:
                print("Binary file")

            