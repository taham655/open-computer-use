
from langchain_core.tools import tool
from typing import Union, List, Annotated
from typing_extensions import TypedDict
import pyautogui
import time

@tool
def click_at_position(x: int, y: int) -> None:
    """
    Click the mouse at specified screen coordinates (x, y).
    Origin is top-left (0,0).
    
    Args:
        x (int): Horizontal position in pixels from left
        y (int): Vertical position in pixels from top
    
    Example: click_at_position(500, 300)
    """
    pyautogui.click(x, y)

@tool
def type_text(text: str, interval: float = 0.1) -> None:
    """
    Type text with delay between keystrokes.
    
    Args:
        text (str): Text to type
        interval (float): Delay between keystrokes in seconds
    
    Example: type_text("Hello", 0.2)
    """
    pyautogui.write(text, interval=interval)

@tool
def press_key(key: str) -> None:
    """
    Press a single keyboard key.
    
    Args:
        key (str): Key name to press. Valid keys:
            - Letters: a-z
            - Numbers: 0-9
            - Special: enter, tab, space, backspace, delete, escape
            - Function: f1-f12
            - Modifiers: shift, ctrl, alt, command
            - Arrows: up, down, left, right
    
    Example: press_key('enter')
    """
    pyautogui.press(key)

@tool
def key_combination(keys: Union[str, List[str]]) -> None:
    """
    Press multiple keys simultaneously.
    
    Args:
        keys: Either string with '+' separator or list of keys
            Example string: 'ctrl+c'
            Example list: ['ctrl', 'alt', 'delete']
    
    Example: key_combination('ctrl+v')
    """
    if isinstance(keys, str):
        keys = keys.split('+')
    pyautogui.hotkey(*keys)
    
    
@tool 
def wait(seconds= 2) -> None:
    """
    This is used to wait for a specifc task to be performed. 
    
    Args:
        seconds (float): Number of seconds to wait
    
    """
    time.sleep(seconds)




# import pyautogui
# import time
# import platform
# from langchain_core.tools import tool
# from langchain_core.messages import HumanMessage
# import pyautogui
# import base64
# from langchain_openai import ChatOpenAI
# import time
# import os
# from pathlib import Path

# from typing import Annotated

# from typing_extensions import TypedDict

# from langgraph.graph.message import AnyMessage, add_messages


# # class State(TypedDict):
# #     messages: Annotated[list[AnyMessage], add_messages]
# #     latest_image: str
    


# def screenshot_to_base64():
#     """
#     Takes a screenshot, saves it temporarily, converts to base64,
#     deletes the temporary file, and returns the base64 string
    
#     Returns:
#     str: Base64 encoded string of the screenshot
#     """
#     # Create temp filename
#     temp_file = "temp_screenshot.png"
    
#     try:
#         # Take and save screenshot
#         screenshot = pyautogui.screenshot()
#         screenshot.save(temp_file)
#         print(f"Screenshot saved to {temp_file}")
        

#         with open(temp_file, "rb") as image_file:
#             base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        
#         return base64_string
        
        
#         message = HumanMessage(
#             content=[
#                 {"type": "text", "text": "Describe this image:"},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_string}"
#                     },
#                 },
#             ]
#         )
        
#         llm = ChatOpenAI(model='gpt-4o', temperature=0.5)
        

#         text = llm.invoke([message])
        
        
#         return text
        
#     finally:
        
#         if os.path.exists(temp_file):
#             os.remove(temp_file)


# @tool
# def move_mouse(x, y, duration=0.5):
#     """
#     Move mouse to specific coordinates
#     :param x: x coordinate
#     :param y: y coordinate
#     :param duration: time taken for movement (seconds)
#     """
#     pyautogui.moveTo(x, y, duration=duration)


# @tool
# def click_at_position(x: int, y: int, state: State):
#     """
#     Click at specific coordinates
#     :param x: x coordinate
#     :param y: y coordinate
#     """
#     pyautogui.click(x, y)




# @tool
# def type_text(text:str, state: State, interval=0.1):
#     """
#     Type text with specified interval between keystrokes
#     :param text: text to type
#     :param interval: delay between keystrokes
#     """
#     pyautogui.write(text, interval=interval)


# @tool
# def press_key(key:str , state: State):
#     """
#     Press a single key
#     :param key: key to press (e.g., 'enter', 'tab', 'shift')
#     """
#     pyautogui.press(key)

    


# @tool
# def key_combination(keys: str, state: State):
#     """
#     Press a combination of keys
#     :param keys: list of keys to press simultaneously
#     """
#     pyautogui.hotkey(*keys)



# def get_screen_size():
#     """
#     Get screen size
#     :return: tuple of (width, height)
#     """
#     return pyautogui.size()

# # def get_mouse_position():
# #     """
# #     Get current mouse position
# #     :return: tuple of (x, y) coordinates
# #     """
# #     return pyautogui.position()
# # state['latest_image'] = screenshot_to_base64()


# # @tool
# # def drag_mouse(start_x, start_y, end_x, end_y, duration=0.5):
# #     """
# #     Drag mouse from start to end position
# #     :param start_x: starting x coordinate
# #     :param start_y: starting y coordinate
# #     :param end_x: ending x coordinate
# #     :param end_y: ending y coordinate
# #     :param duration: time taken for drag operation
# #     """
# #     pyautogui.mouseDown(start_x, start_y)
# #     pyautogui.moveTo(end_x, end_y, duration=duration)
# #     pyautogui.mouseUp()

# # if __name__ == "__main__":
# #     time.sleep(3)

    
# #     press_key('shift')  
# #     press_key('tab')    
    
    
# #     if platform.system() == 'Darwin':  # macOS
# #         key_combination(['command', 'space'])
# #     else:  
# #         key_combination(['win', 's'])
    
# #     time.sleep(1)

# #     screen_width, screen_height = get_screen_size()
# #     print(f"Screen size: {screen_width}x{screen_height}")
    
# #     move_mouse(screen_width/2, screen_height/2)
    
# #     click_at_position(screen_width/2, screen_height/2)
    
# #     type_text("Chrome")
    
# #     press_key('enter')
    
# #     time.sleep(1)
# #     move_mouse(screen_width/2, 80) 
    

# #     type_text("youtube.com")
# #     press_key('enter')
# #     time.sleep(1)
# #     move_mouse(650, 145)
# #     click_at_position(650, 145)
# #     type_text("RICK ROLL")
# #     press_key('enter')
    
# #     time.sleep(4)
# #     move_mouse(650, 300)
# #     click_at_position(650, 300)
    
# #     key_combination(['ctrl', 'a'])
    
# #     x, y = get_mouse_position()
# #     print(f"Current mouse position: {x}, {y}")