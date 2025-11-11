from django.core.exceptions import ValidationError
from django.core.Validators import validate_email
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except ValidationError as e:
        logger.warning(f"Invalid email format:{email} | Error: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while validating email: {e}")
        return False