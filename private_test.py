import FreddyApi
from FreddyApi.module import Message, MessageRequestPayload
import time
from config import Config


if __name__ == "__main__":
    token = Config.load_token()
    api = FreddyApi.FreddyApi(token=token)
    payload = MessageRequestPayload(
        organization_id=5,
        assistant_id=6,
        model="gpt-4o",
        messages=[Message(content="Tell me a joke that is very long put into a poem", role="user")]
    )

    def print_word(response):
        print(response)

    result = api.execute_run(payload)
    print(result)

