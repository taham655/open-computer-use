import pyautogui
import base64
from io import BytesIO

def screenshot_to_base64():
    """
    Take a full screen screenshot and convert it to base64 encoding
    
    Returns:
    str: Base64 encoded string of the screenshot
    """
    
    screenshot = pyautogui.screenshot()
    
    
    buffered = BytesIO()
    screenshot.save(buffered, format='PNG')
    
    
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    return img_base64
