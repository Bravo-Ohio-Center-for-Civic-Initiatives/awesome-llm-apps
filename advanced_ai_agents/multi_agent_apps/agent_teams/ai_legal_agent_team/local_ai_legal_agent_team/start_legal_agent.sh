#!/bin/bash

echo "🚀 Starting AI Legal Agent..."

# Kill any existing processes
pkill -f streamlit 2>/dev/null
pkill -f "python.*legal" 2>/dev/null

# Wait a moment
sleep 2

# Start Qdrant if not running
if ! curl -s http://localhost:6333/collections >/dev/null 2>&1; then
    echo "📦 Starting Qdrant database..."
    docker run -d -p 6333:6333 --name qdrant-legal qdrant/qdrant 2>/dev/null
    sleep 5
fi

# Change to the correct directory
cd "$(dirname "$0")"

echo "🔧 Starting Legal Agent on multiple ports..."

# Start on port 8080
streamlit run local_legal_agent.py --server.port 8080 --server.address 0.0.0.0 &
sleep 3

# Start on port 8090 as backup
streamlit run local_legal_agent.py --server.port 8090 --server.address 0.0.0.0 &
sleep 3

echo ""
echo "✅ AI Legal Agent is starting up!"
echo ""
echo "🌐 Try these URLs in your browser:"
echo "   • http://localhost:8080"
echo "   • http://localhost:8090"
echo "   • http://127.0.0.1:8080"
echo "   • http://192.168.50.44:8080"
echo ""
echo "📋 Features available:"
echo "   • Upload PDF legal documents"
echo "   • 3-agent analysis team"
echo "   • Contract review & legal research"
echo "   • All running locally with Llama 3.2"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for user interrupt
wait