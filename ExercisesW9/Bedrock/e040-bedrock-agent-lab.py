from pydantic import BaseModel, Field
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from typing import Optional
# =====================================================================
# 1. Pydantic Structured Output Schema
# =====================================================================
# TODO: Define a 'StockRecommendation' class inheriting from BaseModel.
# Fields:
#   - ticker (str): The stock ticker (e.g. "TSLA")
#   - recommendation (str): "BUY", "SELL", or "HOLD"
#   - reasoning (str): A one-sentence justification.
class StockRecommendation(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol (e.g., 'TSLA')")
    recommendation: Optional[str] = Field(None, description="Recommendation: 'BUY', 'SELL', or 'HOLD'")
    reasoning: Optional[str] = Field(None, description="One-sentence justification for the recommendation")

# =====================================================================
# 2. Tool Definition
# =====================================================================
# TODO: Define a @tool function named 'get_stock_sentiment'.
# It should accept 'ticker: str' and return a str.
# Write a clear docstring — the LLM reads it to know when to call this tool.
# Include mock sentiment data for at least 3 tickers (AAPL, TSLA, AMZN).

# @tool
# def get_stock_sentiment(ticker: str) -> str:
#     """..."""
#     pass

@tool
def get_stock_sentiment(ticker: str) -> str:
    """Returns the current stock price for a given ticker."""
    data = {'AAPL': '$110.98', 'TSLA': '$23.44', 'AMZN': '$44.74'}
    return data.get(ticker.upper(), 'Ticker not found')

# =====================================================================
# 3. Agent Initialization
# =====================================================================
# TODO: Use init_chat_model() to initialize Amazon Bedrock.
# Use model="us.anthropic.claude-3-5-sonnet-20240620-v1:0"
# Use model_provider="bedrock" and temperature=0

llm = init_chat_model(
    model="mistral.mistral-7b-instruct-v0:2", 
    model_provider="bedrock", 
    temperature=0
)

# =====================================================================
# 4. Create the ReAct Agent
# =====================================================================
# TODO: Use create_react_agent with your llm, tools list, and a
# professional financial-analyst system_prompt (via state_modifier).

# agent = create_react_agent(...)

sysPrompt = "You are a financial analyst. Use the stock tool for any financial queries."
tools = [get_stock_sentiment]
agent = create_agent(llm, tools, system_prompt=sysPrompt, context_schema=StockRecommendation)

# =====================================================================
# 5. Stream the Agent Response
# =====================================================================
def run_exercise():
    
    # TODO: Stream the agent using .stream(query, stream_mode="values")
    # For each chunk, print the last message's type and content.
    print("=== e040: Your First Bedrock Agent ===")
    # YOUR CODE HERE
    query = {"messages": [
        ("user", "What is your recommendation for Tesla (TSLA) stock?")
    ]}

    for chunk in agent.stream(query, stream_mode='values'):  # type: ignore
        message = chunk["messages"][-1]
        if message.content:
            print(f"[{message.type.upper()}]: {message.content}")

        
        # # Each chunk contains the full state at that point
        # latest_message = chunk["messages"][-1]
        # if latest_message.content:
        #     if isinstance(latest_message, HumanMessage):
        #         print(f"User: {latest_message.content}")
        #     elif isinstance(latest_message, AIMessage):
        #         print(f"Agent: {latest_message.content}")
        # elif latest_message.tool_calls:
        #     print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
if __name__ == "__main__":
    run_exercise()
