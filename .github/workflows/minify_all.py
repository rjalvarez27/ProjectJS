import os
import subprocess

def minify_file(file_path):
    minified_file_path = file_path.replace('.js', '.min.js')
    command = f'minify {file_path} -o {minified_file_path}'
    subprocess.run(command, shell=True, check=True)
    print(f'Minified {file_path} to {minified_file_path}')

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                minify_file(file_path)

# Inicia el proceso en el directorio actual
if __name__ == "__main__":
    traverse_directory(os.getcwd())
