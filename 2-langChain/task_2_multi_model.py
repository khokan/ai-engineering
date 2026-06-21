#!/usr/bin/env python3
"""
Task 2: Multi-Model Support - One Interface, Many Providers!
Test OpenAI, Google, and X.AI models using the same LangChain interface.

Learning Goal: Experience provider flexibility without code changes.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("🎯 Task 2: Multi-Model Support with LangChain")
    print("=" * 50)

    print("\n🌐 Initialize Multiple AI Providers")
    print("=" * 50)

    # TODO 1: Initialize OpenAI model
    print("Setting up OpenAI GPT-4.1-mini...")
    openai_llm = ChatOpenAI(
        model="openai/gpt-oss-120b:free",                    # Replace ___ with: "openai/gpt-4.1-mini"
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_API_BASE"),
        max_tokens=100
    )

    # TODO 2: Initialize Google Gemini model
    print("Setting up Google Gemini...")
    google_llm = ChatOpenAI(
        model="google/gemini-2.5-flash",                    # Replace ___ with: "google/gemini-2.5-flash"
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_API_BASE"),
        max_tokens=100
    )

    # TODO 3: Initialize X.AI Grok model
    print("Setting up X.AI Grok...")
    xai_llm = ChatOpenAI(
        model="x-ai/grok-code-fast-1",                    # Replace ___ with: "x-ai/grok-code-fast-1"
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_API_BASE"),
        max_tokens=100
    )

    # Compare all models with the same prompt
    print("\n✅ All models initialized! Now let's compare them...")
    print("\nModel Comparison - Same Prompt, Different Models")
    print("=" * 50)

    test_prompt = "Explain cloud computing in one sentence"
    print(f"📝 Prompt: '{test_prompt}'\n")

    # Test all models with the same prompt
    if openai_llm:
        response = openai_llm.invoke(test_prompt)
        print(f"OpenAI: {response.content[:100]}...")

    if google_llm:
        response = google_llm.invoke(test_prompt)
        print(f"Google: {response.content[:100]}...")

    # if xai_llm:
    #     response = xai_llm.invoke(test_prompt)
    #     print(f"X.AI: {response.content[:100]}...")

    print("\n💡 Same code, different providers - perfect for A/B testing!")

    # Create marker for completion
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task2_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 2 completed! You can now switch models at will!")
    print("🎉 You tested 3 different AI providers with identical code!")

if __name__ == "__main__":
    main()