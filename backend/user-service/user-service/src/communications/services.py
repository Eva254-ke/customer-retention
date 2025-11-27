import os
from pathlib import Path
from typing import Optional, Tuple

import africastalking
from decouple import Config, RepositoryEnv, UndefinedValueError


def _find_env_config() -> Optional[Config]:
    for parent in Path(__file__).resolve().parents:
        env_file = parent / '.env'
        if env_file.exists():
            return Config(RepositoryEnv(str(env_file)))
    return None


_ENV_CONFIG = _find_env_config()


def _load_env_value(key: str) -> Optional[str]:
    if _ENV_CONFIG:
        try:
            return _ENV_CONFIG(key)
        except UndefinedValueError:
            pass
    return os.getenv(key)


def _resolve_credentials(username: Optional[str] = None, api_key: Optional[str] = None) -> Tuple[str, str]:
    resolved_username = username or _load_env_value('AFRICASTALKING_USERNAME')
    resolved_api_key = api_key or _load_env_value('AFRICASTALKING_API_KEY')
    if not resolved_username or not resolved_api_key:
        raise RuntimeError("AFRICASTALKING_USERNAME and AFRICASTALKING_API_KEY must be set in the environment or .env file.")
    return resolved_username, resolved_api_key


def _resolve_sender() -> Optional[str]:
    return _load_env_value('AFRICASTALKING_SENDER_ID')


_USERNAME, _API_KEY = _resolve_credentials()
africastalking.initialize(_USERNAME, _API_KEY)
_SMS_CLIENT = africastalking.SMS
_SENDER_ID = _resolve_sender()


def send_sms(
    to: str,
    message: str,
    username: Optional[str] = None,
    api_key: Optional[str] = None,
    sender: Optional[str] = None,
):
    """Send an SMS using the documented africastalking.SMS.send(message, recipients, sender_id) signature."""
    recipients = [to]
    resolved_sender = sender or _SENDER_ID
    client = _SMS_CLIENT
    if username or api_key:
        africastalking.initialize(*_resolve_credentials(username, api_key))
        client = africastalking.SMS
    return client.send(message, recipients, resolved_sender)
