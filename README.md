# Open Computer Use

An open-source alternative to Anthropic's Computer Use, leveraging Vision Language Models for desktop automation and RPA (Robotic Process Automation).

![System Architecture](https://raw.githubusercontent.com/yourusername/opencomputeruse/main/docs/architecture.png)

## 🤖 Overview

Open Computer Use is a framework that enables AI to interact with your computer through:
- Visual understanding of your screen using Vision Language Models
- Direct control of keyboard and mouse inputs
- Automated screenshot capture and analysis
- Continuous feedback loop for complex tasks

### Key Differentiators
- **Vision-First Approach**: Uses advanced Vision LLMs to understand screen context
- **Basic I/O Operations**: Performs fundamental computer interactions that can solve complex automation problems
- **Ideal for RPA**: Perfect for repetitive task automation and business process automation
- **Open Architecture**: Fully open-source and customizable

## 🚀 Features

- **Visual Understanding**: Uses GPT-4 Vision to interpret screen contents
- **Automated Actions**: Performs keyboard and mouse actions programmatically
- **State Management**: Maintains conversation context and screen state
- **Error Handling**: Robust error handling for image processing and LLM interactions
- **Modular Design**: Built using LangGraph's node-based architecture

## 🔄 Process Flow

1. **Start**: Application initialization
2. **Initialization**: System setup and initial state configuration
3. **AI Processing**: Vision LLM analyzes screen content
4. **Tools Execution**: 
   - Keyboard operations
   - Mouse control
5. **Screenshot**: Captures new screen state
6. **Loop/End**: Continues process or terminates based on task completion

## 📋 Prerequisites

- Python 3.x
- OpenAI API key (for GPT-4 Vision)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install required dependencies:
```bash
pip install langchain-openai langgraph pyautogui python-dotenv
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## 🏗️ Project Structure

```
├── tools.py            # Custom automation tools (keyboard/mouse)
├── prompts.py         # System prompts and messages
├── utils.py           # Utility functions
└── main.py           # Main application logic
```

## 💻 Core Components

### State Management
```python
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    screen_size: str
    latest_image: str
    initialized: bool
```

### Tools
The framework includes several automation tools:
- `click_at_position`: Mouse clicking
- `press_key`: Keyboard key pressing
- `key_combination`: Complex keyboard shortcuts
- `type_text`: Text input
- `wait`: Time-based delays

### Graph Architecture
The application uses LangGraph's StateGraph to manage the flow:
1. Initialize -> Takes initial screenshot
2. Assistant -> Processes user input and current screen state
3. Tools -> Executes required actions
4. Screenshot -> Captures new state
5. Loop back to Assistant or END

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This is an open-source alternative to commercial computer control solutions. Use responsibly and ensure compliance with your system's security policies.
