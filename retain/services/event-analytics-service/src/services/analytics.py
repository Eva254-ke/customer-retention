from datetime import datetime
import json
import logging

class AnalyticsService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.logger = logging.getLogger(__name__)

    def log_event(self, event_data):
        event_data['timestamp'] = datetime.utcnow().isoformat()
        self._save_event_to_db(event_data)

    def _save_event_to_db(self, event_data):
        try:
            # Assuming db_connection has a method to save data
            self.db_connection.save(event_data)
            self.logger.info("Event saved successfully: %s", event_data)
        except Exception as e:
            self.logger.error("Error saving event: %s", e)

    def get_events(self, start_time, end_time):
        try:
            events = self.db_connection.query_events(start_time, end_time)
            return events
        except Exception as e:
            self.logger.error("Error retrieving events: %s", e)
            return []

    def analyze_churn_risk(self, user_id):
        events = self.get_events_for_user(user_id)
        churn_risk = self._calculate_churn_risk(events)
        return churn_risk

    def get_events_for_user(self, user_id):
        try:
            events = self.db_connection.query_events_by_user(user_id)
            return events
        except Exception as e:
            self.logger.error("Error retrieving events for user %s: %s", user_id, e)
            return []

    def _calculate_churn_risk(self, events):
        # Placeholder for churn risk calculation logic
        if not events:
            return 1.0  # High risk if no events
        # Example logic: lower risk with more events
        risk_score = max(0, 1 - (len(events) / 10))
        return risk_score

    def export_events_to_json(self, start_time, end_time):
        events = self.get_events(start_time, end_time)
        return json.dumps(events)