import os
from pathlib import Path
from typing import Optional, Tuple

import africastalking
from decouple import Config, RepositoryEnv, UndefinedValueError


def _load_env_value(key: str) -> Optional[str]:
    env_file = Path(__file__).resolve().parents[5] / '.env'
    if env_file.exists():
        repo = RepositoryEnv(str(env_file))
        config = Config(repo)
        try:
            return config(key)
        except UndefinedValueError:
            pass
    return os.getenv(key)


def _resolve_credentials(username: Optional[str] = None, api_key: Optional[str] = None) -> Tuple[str, str]:
    resolved_username = username or _load_env_value('AFRICASTALKING_USERNAME')
    resolved_api_key = api_key or _load_env_value('AFRICASTALKING_API_KEY')
    if not resolved_username or not resolved_api_key:
        raise RuntimeError("AFRICASTALKING_USERNAME and AFRICASTALKING_API_KEY must be set in the environment or .env file.")
    return resolved_username, resolved_api_key


_USERNAME, _API_KEY = _resolve_credentials()
africastalking.initialize(_USERNAME, _API_KEY)
_SMS_CLIENT = africastalking.SMS


def send_sms(to: str, message: str, username: Optional[str] = None, api_key: Optional[str] = None):
    if username or api_key:
        africastalking.initialize(*_resolve_credentials(username, api_key))
        return africastalking.SMS.send(message, [to])
    return _SMS_CLIENT.send(message, [to])
