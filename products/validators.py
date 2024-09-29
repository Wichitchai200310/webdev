from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_mb = 5  # Max size allowed: 5MB
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size should not exceed {max_size_mb} MB.")
