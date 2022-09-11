import dearpygui.dearpygui as imgui
import openai
import os

"""
TODO: Fine tune the bot
TODO: sqlite UUID checking
TODO: obfuscation
"""

openai.api_key = ""

imgui.create_context()

for_export = []

def export():
    with open('export.txt','w') as file:
        file.write(str(for_export))

def send():  
    input_box = str(imgui.get_value(item="input_field")).lstrip().rstrip()
    imgui.add_text(f"You: {input_box}", parent="child window")
    imgui.add_text(f"Alice:\n {ai(input_box)}", parent="child window")

def ai(input_box):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=input_box,
      temperature=0.7,
      max_tokens=4000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    text = str(response['choices'][0]['text']).strip()
    for_export.append(text)
    return text
    
with imgui.window(tag="primary window", label=None,no_move=True, no_collapse=True, no_title_bar=True):
    imgui.add_input_text(label="type a prompt",tag="input_field", callback=send, on_enter=True)
    imgui.add_button(label="send",callback=send)
    imgui.add_checkbox(label="check to export prompt", callback=export)
    imgui.add_child_window(tag="child window",horizontal_scrollbar=True,autosize_x=True,autosize_y=True)


#must be in this order for window to stay
#within the resize range of the view port
imgui.create_viewport(title="Alice",width=600,height=600,resizable=True)
imgui.setup_dearpygui()
imgui.show_viewport()
imgui.set_primary_window("primary window", True)
imgui.start_dearpygui()
imgui.destroy_context()
