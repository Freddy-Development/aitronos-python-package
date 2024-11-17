from Aitronos import Aitronos, Message, MessageRequestPayload
from config import Config


token = Config.load_token()
api = Aitronos(api_key=token)

message_content = "[{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'The perfect tool for everyday use for opening cans and cutting. Pocket knife with 12 functions, made in Switzerland.', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Height: 14.5 mm\\nLength: 91 mm\\nWeight: 59 g', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'marks': [{'type': 'bold'}], 'value': 'Tools:', 'nodeType': 'text'}], 'nodeType': 'paragraph'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Large and small blade', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Can opener', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Screwdriver 3mm', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Screwdriver 6mm', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Bottle opener', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Wire stripper', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Piercing-drilling-sewer', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Corkscrew', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Toothpick', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Tweezers', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}, {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Key ring', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'list-item'}], 'nodeType': 'unordered-list'}, {'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'The item will be delivered within the next 5 working days.', 'nodeType': 'text'}], 'nodeType': 'paragraph'}]"

payload = MessageRequestPayload(
    organization_id=2,
    assistant_id=15,
    thread_id=0,
    instructions="""
       Say hello
        """,
    messages=[Message(content=f"Hello", role="user")]
)

result = api.execute_run(payload)
print(result)

# payload = MessageRequestPayload(
#     organization_id=2,
#     assistant_id=15,
#     instructions="be funny",
#     messages=[Message(content=f"Hello, who are you", role="user")]
# )
#
# def print_word(event: StreamEvent):
#     print(f"Handled event: {event}")
#
# api.create_stream(payload, print_word)

