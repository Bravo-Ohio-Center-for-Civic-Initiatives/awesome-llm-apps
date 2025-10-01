import streamlit as st
import asyncio
import random
import time

# Optional: Hugging Face fallback
try:
    from huggingface_hub import InferenceClient
    hf_client = InferenceClient(model="teknium/OpenHermes-2.5-Mistral-7B")
except ImportError:
    hf_client = None


# -----------------------------
# Simulated inference functions
# Replace with real Ollama/HF calls
# -----------------------------
async def local_infer(prompt: str):
    """Simulate local model (llama3.2:3b) inference"""
    await asyncio.sleep(2)  # simulate latency
    return (
        "Local agent draft:\n"
        f"→ Query: {prompt[:50]}...\n"
        "Line 2 of response\n"
        "Line 3 of response\n" +
        "Lorem ipsum dolor sit amet " * 20
    )

async def huggingface_infer(prompt: str):
    """Simulate Hugging Face fallback inference"""
    if hf_client is None:
        await asyncio.sleep(4)
        return (
            "Hugging Face fallback draft:\n"
            "Line 2\nLine 3\n" +
            "Lorem ipsum dolor sit amet " * 40
        )
    # Real HF inference (sync wrapped in async)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        lambda: hf_client.text_generation(
            prompt, max_new_tokens=400
        )
    )


async def cascade(prompt: str, placeholder):
    """Parallel cascade with progressive reveal"""
    # Launch local + Hugging Face
    tasks = [
        asyncio.create_task(local_infer(prompt)),
        asyncio.create_task(huggingface_infer(prompt)),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first_result = list(done)[0].result()

    # Show first 3 lines immediately
    preview = "\n".join(first_result.splitlines()[:3]) + "\n[...Generating full text...]"
    placeholder.text(preview)

    # Wait for remaining tasks
    remaining = await asyncio.gather(*pending, return_exceptions=True)
    all_results = [first_result] + [
        r for r in remaining if isinstance(r, str)
    ]

    # Pick longest response as "best"
    best_result = max(all_results, key=len)

    # Final update
    placeholder.text(best_result)


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Legal AI Agent", page_icon="⚖️", layout="wide")
st.title("⚖️ Multi‑Tier Legal Agent")
st.write(
    "Local → Hugging Face → (future OpenAI/Claude)\n"
    "Fast partial response first, full text after refinement."
)

prompt = st.text_area("Enter your legal query:", "Explain Rule 60(B) motion in Ohio family court.")

if st.button("Generate Response"):
    placeholder = st.empty()
    asyncio.run(cascade(prompt, placeholder))
