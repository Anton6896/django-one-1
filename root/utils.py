import os
from uuid import uuid4


def customer_image_file_path(instance, filename: str):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('uploaded/', filename)


def generate_id(num=None) -> str:
    # max amount 36 chars
    if num:
        return str(uuid4())[:num]
    else:
        return str(uuid4())
