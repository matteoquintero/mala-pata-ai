"""Factory que abstrae el LLM provider para Graphiti.

TODO (siguiente agente):
- Según `config.LLM_PROVIDER`, devolver el cliente Graphiti-compatible correspondiente:
    - anthropic → AnthropicClient con ANTHROPIC_API_KEY
    - openai   → OpenAIClient
    - google   → GoogleClient
    - ollama   → OpenAIClient con base_url = http://localhost:11434/v1
- Verificar que la API key/endpoint funciona (fail-fast).
- Devolver también el modelo string que Graphiti usa.
"""


def get_llm_client():
    raise NotImplementedError
