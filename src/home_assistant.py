import os
import requests

all_outdoors_webhook_id = os.environ.get('ALL_OUTDOORS_WEBHOOK_ID')
someone_hone_webhook_id = os.environ.get('SOMEONE_HOME_WEBHOOK_ID')
if not all_outdoors_webhook_id or not someone_hone_webhook_id:
    raise ValueError("Environment variables ALL_OUTDOORS_WEBHOOK_ID and SOMEONE_HOME_WEBHOOK_ID must be set")

home_assistant_endpoint = os.environ.get('HA_ENDPOINT', 'http://host.docker.internal:8123') # 'https://localhost:8123')

def _get_webhook_url(webhook_id: str) -> str:
    return f"{home_assistant_endpoint}/api/webhook/{webhook_id}"

def _send_notification(webhook_id: str) -> int:
    try:
        response = requests.put(
            _get_webhook_url(webhook_id),
        )
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.status_code
    except Exception as e:
        print(f"Failed to send REST notification: {e}")


def notify_someone_is_at_home():
    print(f"REST API notification sent: Someone is at home. Response: {_send_notification(someone_hone_webhook_id)}")

def notify_all_outdoors():
    print(f"REST API notification sent: Nobody is at home. Response: {_send_notification(all_outdoors_webhook_id)}")
