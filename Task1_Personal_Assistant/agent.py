import re
from google.adk.agents.llm_agent import Agent

def calculator(expression: str) -> str:
    """
    Perform mathematical calculations accurately.
    Args:
        expression: The mathematical expression to evaluate (e.g., '12500 * 18 / 100')
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def text_analyzer(text: str) -> str:
    """
    Analyze a piece of text to find its character, word, and sentence count.
    Args:
        text: The string of text to analyze.
    """
    char_count = len(text)
    word_count = len(text.split())
    # Split by common sentence-ending punctuation to count sentences
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    sentence_count = len(sentences)
    
    return f"Characters: {char_count}\nWords: {word_count}\nSentences: {sentence_count}"

# Here is our agent, equipped with all 3 tools!
root_agent = Agent(
    model='groq/qwen/qwen3.8-27b',
    name='personal_assistant',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. If calculation or text analysis is required, use the provided tools.',
    tools=[calculator, text_analyzer]
)
