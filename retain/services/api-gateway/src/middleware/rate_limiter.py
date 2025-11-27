from flask import request, jsonify
from functools import wraps
import time

RATE_LIMIT = 100  # requests per time window
TIME_WINDOW = 60  # time window in seconds

user_requests = {}

def rate_limiter(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = request.headers.get('X-User-ID')
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400
        
        current_time = time.time()
        if user_id not in user_requests:
            user_requests[user_id] = []

        # Remove timestamps outside the time window
        user_requests[user_id] = [timestamp for timestamp in user_requests[user_id] if timestamp > current_time - TIME_WINDOW]

        if len(user_requests[user_id]) >= RATE_LIMIT:
            return jsonify({"error": "Rate limit exceeded"}), 429

        user_requests[user_id].append(current_time)
        return f(*args, **kwargs)

    return decorated_function