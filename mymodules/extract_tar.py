import tarfile


def extract_tar(tar_file_path, extract_file_path):
    tar = tarfile.open(tar_file_path)
    tar.extractall(path=extract_file_path)
    tar.close()
