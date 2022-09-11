import dearpygui.dearpygui as imgui
import openai
import sqlite3


"""
TODO: Fine tune the bot
TODO: sqlite UUID checking
TODO: obfuscation
"""



imgui.create_context()

def send():
    with imgui.child_window(autosize_x=True, label="childwindow", parent="primary window", height=50):
        input_box = imgui.get_value(item="input_field")
        imgui.add_text(f"You: {input_box}")
        
    
with imgui.window(tag="primary window", label=None, width=200, height=2000, no_move=True, no_collapse=True, no_title_bar=True):
    imgui.add_input_text(label="type a prompt",tag="input_field", callback=send, on_enter=True)
    imgui.add_button(label="send",callback=send)


#must be in this order for window to stay
#within the resize range of the view port
imgui.create_viewport(width=1000,height=1000,resizable=True)
imgui.setup_dearpygui()
imgui.show_viewport()
imgui.set_primary_window("primary window", True)
imgui.start_dearpygui()
imgui.destroy_context()