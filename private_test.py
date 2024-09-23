import FreddyApi
from FreddyApi.module import Message, MessageRequestPayload, StreamEvent
import time
from config import Config


if __name__ == "__main__":
    token = Config.load_token()
    api = FreddyApi.FreddyApi(token=token)

    # Define the message content
    # message_content = "[{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'The perfect tool for everyday use for opening cans and cutting. Pocket knife with 12 functions, made in Switzerland.', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Height: 14.5 mm\\nLength: 91 mm\\nWeight: 59 g', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'marks': [{'type': 'bold'}], 'value': 'Tools:', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Large and small blade', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Can opener', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Screwdriver 3mm', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Screwdriver 6mm', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Bottle opener', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Wire stripper', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Piercing-drilling-sewer', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Corkscrew', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Toothpick', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Tweezers', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Key ring', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}], 'nodeType': 'unordered-list'}, {'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'The item will be delivered within the next 5 working days.', 'nodeType': 'text'}], 'nodeType': 'paragraph'}]"
    #
    # # Create the payload
    # payload = MessageRequestPayload(
    #     organization_id=2,
    #     assistant_id=15,
    #     thread_id=0,
    #     model="gpt-4o",
    #     instructions="""
    #         Return the response in the exact same format as the input. As long as the json format is valid, set your priority on a valid json format so I can then simply load the json with code.
    #         Return the requested language, so always only return one language and no other and keep the format, only translate the content.
    #         Ensure that the response is in JSON format, return all the contents inside the first language content array, and keep the format intact.
    #     """,
    #     additional_instructions="Translate to English (US), Dutch, French, Italian, German",
    #     messages=[Message(content=f"Translate the following content '{message_content}' into English (US), Dutch, French, Italian, German from the default language: en.", role="user")]
    # )

    payload = MessageRequestPayload(
        organization_id=2,
        assistant_id=15,
        thread_id=0,
        model="gpt-4o",
        instructions="be funny",
        messages=[Message(content=f"Hello, who are you", role="user")]
    )

    def print_word(event: StreamEvent):
        print(f"Handled event: {event}")

    api.create_stream(payload, print_word)

