import streamlit as st
import requests

st.title("🔍 Debug Legal Agent")

st.header("1. Basic Connection Test")
st.write("Testing basic connectivity...")

st.header("2. Qdrant Connection Test")
try:
    response = requests.get("http://localhost:6333/collections")
    if response.status_code == 200:
        st.success("✅ Qdrant is responding!")
        st.json(response.json())
    else:
        st.error(f"❌ Qdrant error: {response.status_code}")
except Exception as e:
    st.error(f"❌ Cannot connect to Qdrant: {str(e)}")

st.header("3. Import Test")
try:
    from agno.embedder.ollama import OllamaEmbedder
    st.success("✅ OllamaEmbedder imported successfully")
    
    # Test embedder creation
    try:
        embedder = OllamaEmbedder()
        st.success("✅ OllamaEmbedder created successfully")
    except Exception as e:
        st.error(f"❌ OllamaEmbedder creation failed: {str(e)}")
        
except Exception as e:
    st.error(f"❌ Import failed: {str(e)}")

st.header("4. Qdrant Integration Test")
try:
    from agno.vectordb.qdrant import Qdrant
    from agno.embedder.ollama import OllamaEmbedder
    
    vector_db = Qdrant(
        collection="test_collection",
        url="http://localhost:6333", 
        embedder=OllamaEmbedder()
    )
    st.success("✅ Qdrant vector database initialized!")
    
except Exception as e:
    st.error(f"❌ Qdrant integration failed: {str(e)}")
    st.exception(e)

st.header("5. Ollama Model Test")
try:
    from agno.models.ollama import Ollama
    model = Ollama(id="llama3.2:3b")
    st.success("✅ Ollama model created successfully")
except Exception as e:
    st.error(f"❌ Ollama model failed: {str(e)}")
    st.exception(e)