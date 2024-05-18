import os
import shutil
import hashlib

def disk_operations(file_size_mb):
    data = os.urandom(file_size_mb * 1024 * 1024)
    with open("test_file.bin", "wb") as f:
        f.write(data)
    with open("test_file.bin", "rb") as f:
        _ = f.read()
    os.remove("test_file.bin")

def compute_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def copy_file(source_file, destination_file):
    shutil.copyfile(source_file, destination_file)

def compare_files(file1, file2):
    hash1 = compute_file_hash(file1)
    hash2 = compute_file_hash(file2)
    return hash1 == hash2