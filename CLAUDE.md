# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the "Awesome LLM Apps" repository - a curated collection of LLM applications built with RAG, AI Agents, Multi-agent Teams, MCP, Voice Agents, and more. The repository features apps using models from OpenAI, Anthropic, Google, and open-source models like DeepSeek, Qwen, or Llama that can run locally.

## Architecture and Code Patterns

### Core Frameworks Used

**Agno (Phi Framework)** - Primary agent framework (used in 70%+ of projects):
- Unified interface for multiple LLM providers (OpenAI, Anthropic, Ollama)
- Key components: `Agent`, `OpenAIChat`/`Ollama` models, built-in tools
- Supports both cloud and local model deployments
- Built-in integrations: web search, financial data, file operations

**CrewAI** - Multi-agent orchestration:
- Used for complex multi-agent workflows in `/agent_teams/` directories
- Pattern: Agents with roles, goals, backstories, and sequential/hierarchical tasks

**LangChain** - Traditional RAG implementations:
- Primarily used in `/rag_tutorials/` for document processing pipelines
- Common components: document loaders, text splitters, vector stores, retrieval chains

**OpenAI Swarm** - Lightweight multi-agent systems:
- Used for simple multi-agent orchestration with direct OpenAI integration

### LLM Provider Integration

**Cloud Providers:**
- OpenAI: GPT-4o, GPT-4o-mini (most common)
- Anthropic: Claude models (growing adoption)
- Google: Gemini (via ADK framework)

**Local Models via Ollama:**
- llama3.2, llama3.1, qwen, deepseek
- Same codebase often supports both cloud and local variants

### UI Framework Standards

**Streamlit** (90%+ of projects):
- Standard UI across all categories
- Common patterns: API key input, text inputs, spinners, markdown output
- Session state management for conversations and data persistence

### Directory Structure

```
awesome-llm-apps/
├── starter_ai_agents/          # Simple, beginner-friendly agents
├── advanced_ai_agents/         # Complex single and multi-agent systems
│   ├── single_agent_apps/      # Individual specialized agents
│   ├── multi_agent_apps/       # Multi-agent orchestration
│   └── autonomous_game_playing_agent_apps/
├── rag_tutorials/              # RAG implementations and variations
├── voice_ai_agents/            # Voice-enabled AI agents
├── mcp_ai_agents/              # Model Context Protocol integrations
├── advanced_llm_apps/          # Memory, chat, and fine-tuning tutorials
└── ai_agent_framework_crash_course/ # Framework-specific tutorials
```

## Common Development Commands

### Running Applications

Most applications follow this pattern:
```bash
cd [project_directory]
pip install -r requirements.txt
streamlit run [main_script].py
```

### Testing Local Models

Many projects support local models via Ollama:
```bash
# Start Ollama service first
ollama serve

# Pull required model
ollama pull llama3.2

# Run app with local model configuration
```

### Environment Setup

Standard environment variables:
```bash
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"
export GOOGLE_API_KEY="your-key"
```

## Code Architecture Patterns

### Agent Configuration Pattern

```python
from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama

# Cloud version
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[SerpApiTools(), YFinanceTools()],
    instructions="Agent instructions here"
)

# Local version
agent = Agent(
    model=Ollama(id="llama3.2"),
    tools=[DuckDuckGoTools()],
    instructions="Agent instructions here"
)
```

### Streamlit UI Pattern

```python
import streamlit as st

# API key handling
api_key = st.text_input("API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# Session state management
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Processing with feedback
with st.spinner("Processing..."):
    result = agent.run(user_input)
```

### RAG Implementation Pattern

```python
# Vector store setup (ChromaDB/LanceDB common)
# Document processing with chunking
# Embedding generation and storage
# Retrieval and context injection
```

## Key Dependencies

### Core Infrastructure
- `streamlit` - Universal UI framework
- `agno` - Primary agent framework
- `openai` - OpenAI API client
- `python-dotenv` - Environment management

### AI/ML Libraries
- `langchain`, `langchain-community` - Traditional AI workflows
- `crewai` - Multi-agent orchestration
- `ollama` - Local model inference

### Specialized Tools
- `yfinance` - Financial data access
- `duckduckgo-search` - Web search capabilities
- `chromadb`, `lancedb` - Vector databases
- `pypdf`, `pdfplumber` - PDF processing

## Development Best Practices

### Error Handling
- Validate API keys before model initialization
- Implement try-catch blocks for external API calls
- Provide user-friendly error messages in Streamlit

### User Experience
- Use `st.spinner()` for processing feedback
- Implement clear instructions and examples
- Handle graceful fallbacks for failed operations

### Code Organization
- Separate agent logic from UI components
- Create reusable utility functions
- Follow consistent naming conventions
- Include comprehensive README files for each project

### Security
- Never commit API keys to the repository
- Use environment variables or Streamlit secrets for credentials
- Implement proper input validation

## Model Context Protocol (MCP)

Several agents integrate with MCP for enhanced tool capabilities:
- Browser automation tools
- GitHub integration
- Notion workspace access
- Calendar and file system operations

## Memory and State Management

- **Session State**: Streamlit session state for UI persistence
- **Persistent Storage**: SQLite for agent conversations (Agno framework)
- **Vector Storage**: ChromaDB/LanceDB for knowledge persistence

This architecture supports rapid development of LLM applications across various domains while maintaining consistency in patterns, dependencies, and user experience.