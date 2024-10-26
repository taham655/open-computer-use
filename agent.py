import os 
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import AnyMessage, add_messages
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from typing import Union, List, Annotated
from typing_extensions import TypedDict
import time

import pyautogui
from tools import key_combination, wait, press_key, type_text, click_at_position
from prompts import sys_message
from utils import create_tool_node_with_fallback, convert_image_to_base64

import logging
import base64
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

tools = [click_at_position, press_key, key_combination, type_text, wait]

llm_with_tools = llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    screen_size: str
    latest_image: str
    initialized: bool
    
def assistant(state: State):
    """ Handles the initial user message and image, combining them into a properly formatted HumanMessage
    
    Args:
        state (State): Contains latest_image and messages history
        
    Returns:
        dict: Contains messages list with LLM response
        
    Raises:
        ValueError: If state is missing required fields or has invalid data
        ImageProcessingError: If there's an error processing the image
        LLMError: If there's an error with the language model response
        Exception: For any other unexpected errors
    """
    try:
        
        if not isinstance(state, dict):
            raise ValueError("State must be a dictionary")
            
        if "messages" not in state:
            raise ValueError("State must contain 'messages' field")
            
        if "latest_image" not in state:
            raise ValueError("State must contain 'latest_image' field")
            
        messages = state["messages"]
        image_base64 = state["latest_image"]
        
        
        if not isinstance(image_base64, str):
            raise ValueError("Image data must be a base64 string")
            
        try:
            
            if state["initialized"] == True:
                multimodal_message = HumanMessage(
                    content=[
                        {
                            "type": "text",
                            "text": messages[-1]
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                        },
                    ],
                )
                state["initialized"] = False
            else:
                multimodal_message = HumanMessage(
                    content=[
                        {
                            "type": "text",
                            "text": "This is the latest image"
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                        },
                    ],
                )
                
            
            try:
                response = llm_with_tools.invoke([sys_message] + messages)
                time.sleep(1)
                return {"messages": [response]}
                
            except Exception as llm_error:
                raise LLMError(f"Error getting LLM response: {str(llm_error)}")
                
        except Exception as img_error:
            raise ImageProcessingError(f"Error processing image: {str(img_error)}")
            
    except (ValueError, ImageProcessingError, LLMError) as e:
        
        logging.error(f"Error in assistant function: {str(e)}")
        raise
        
    except Exception as e:
        
        logging.error(f"Unexpected error in assistant function: {str(e)}")
        raise Exception(f"An unexpected error occurred: {str(e)}")


class ImageProcessingError(Exception):
    """Raised when there's an error processing the image"""
    pass

class LLMError(Exception):
    """Raised when there's an error with the language model response"""
    pass


def screenshot(state: State):
    """
    Takes a screenshot and adds it to the message history
    
    Args:
        state (State): Contains screen_size and messages
        
    Returns:
        State: Updated state with new screenshot message
    """
    temp_file = "temp_screenshot.png"
    
    try:
        screen_size = state["screen_size"]
        screenshot = pyautogui.screenshot()
        screenshot.save(temp_file)
        print(f"Screenshot saved to {temp_file}")
        
        with open(temp_file, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
            
        state["latest_image"] = base64_string
    
        return state
        
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Temporary file {temp_file} removed")
            
def initialize(state: State):
    """
    Initializes the assistant with the first message
    
    Args:
        state (State): Contains messages
        
    Returns:
        State: Updated state with initialized flag set to True
    """
    temp_file = "temp_screenshot.png"
    
    try:
        screen_size = state["screen_size"]
        screenshot = pyautogui.screenshot()
        screenshot.save(temp_file)
        print(f"Screenshot saved to {temp_file}")
        
        with open(temp_file, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
            
        state["latest_image"] = base64_string
    
        return state
        
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Temporary file {temp_file} removed")
            
builder = StateGraph(State)



builder.add_node("assistant", assistant)
builder.add_node("tools", create_tool_node_with_fallback((tools)))
builder.add_node("screenshot", screenshot)
builder.add_node("initialize", initialize)

builder.add_edge(START, "initialize")
builder.add_edge("initialize", "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition,
    {"tools": "tools", "end": END} 
)
builder.add_edge("tools", "screenshot")
builder.add_edge("screenshot", "assistant")


graph = builder.compile()