# Google ADK AI Agents

This repository contains the complete implementation for the **Google ADK (Agent Development Kit) Workshop**, featuring both single-agent and multi-agent AI systems built using Python and the Google ADK framework.

Due to Google Cloud free-tier quota limits, this project is fully configured to use the blazing-fast and free **Groq** API (`groq/qwen/qwen3.8-27b`) via the `litellm` extension.

## 🚀 Projects Included

### Task 1: Personal Assistant Agent (`Task1_Personal_Assistant`)
A versatile, single-agent system equipped with custom-built tools to assist users with varying tasks. It intelligently selects and executes the appropriate tool based on user prompts.

**Features:**
- 🧮 **Calculator Tool:** Evaluates complex mathematical string expressions accurately.
- 📝 **Text Analyzer Tool:** Analyzes provided text to count characters, words, and sentences.
- 🧠 **Dynamic Tool Calling:** The agent determines when to use tools vs. when to converse naturally.

### Task 2: SmartStudy Planner (`Task2_SmartStudy_Planner`)
An advanced, multi-agent orchestration workflow designed to generate a comprehensive 10-day exam preparation schedule. It demonstrates complex AI architectures including sequential logic, parallel execution, and iterative review loops.

**Multi-Agent Workflow:**
1. **Coordinator Agent:** Receives user requirements and parses the core exam details.
2. **Planning Agent:** Prepares requirements and parallelizes tasks.
3. **Topic, Practice, & Schedule Agents (Parallel):** Independent agents that analyze topics, determine practice volume, and construct the day-to-day calendar simultaneously.
4. **Study Plan Writer:** Aggregates parallel outputs into a cohesive draft.
5. **Review Agent (Loop):** Critiques the draft against the user's constraints (maximum 2 iterations) before producing the final output.

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/sumitrawat2417/Google-ADK-AI-Agents.git
cd Google-ADK-AI-Agents
```

### 3. Create & Activate Virtual Environment
**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install the Google ADK and the LiteLLM extension (required for Groq model routing):
```bash
pip install google-adk
pip install "litellm>=1.75.5"
```

### 5. Environment Variables
Create a `.env` file in the root directory and add your free Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```
*(Get a free key at [console.groq.com](https://console.groq.com))*

---

## 💻 Usage

To run the agents, use the ADK CLI from the root directory:

**Run Task 1 (Personal Assistant):**
```bash
adk run Task1_Personal_Assistant
```
*Example Prompt: "Calculate 12500 * 18 / 100 and then tell me how many characters are in this sentence: Google ADK Agents Workshop is fun!"*

**Run Task 2 (SmartStudy Planner):**
```bash
adk run Task2_SmartStudy_Planner
```
*Example Prompt: "I have a Data Structures exam in 10 days. My current level is Intermediate. Topics: Arrays, Linked Lists, Trees, Graphs, Dynamic Programming. I can study for 3 hours per day. Create a preparation plan for me."*

---

## 📜 License
This project is created as part of the Google ADK AI Agents Workshop. All custom code is open-source.
