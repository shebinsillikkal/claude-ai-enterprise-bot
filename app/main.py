"""
Claude AI Enterprise Bot — FastAPI Backend
Author: Shebin S Illikkal
"""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic
import os

app = FastAPI(title="Claude AI Enterprise Bot", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an intelligent enterprise assistant. Answer questions
clearly and concisely based on the provided documents. Always cite the source
document and section when answering. If the answer is not in the documents,
say so clearly — do not make things up."""

class ChatRequest(BaseModel):
    message: str
    conversation_history: list = []
    document_context: str = ""

class ChatResponse(BaseModel):
    reply: str
    sources: list = []
    tokens_used: int = 0


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    messages = req.conversation_history.copy()
    user_content = req.message
    if req.document_context:
        user_content = f"Context from documents:\n{req.document_context}\n\nQuestion: {req.message}"
    messages.append({"role": "user", "content": user_content})

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages
    )
    reply = response.content[0].text
    return ChatResponse(
        reply=reply,
        tokens_used=response.usage.input_tokens + response.usage.output_tokens
    )


@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(('.pdf', '.docx', '.txt', '.csv')):
        raise HTTPException(status_code=400, detail="Unsupported file type")
    content = await file.read()
    # In production: parse, chunk, and store in vector DB
    return {"filename": file.filename, "size": len(content), "status": "indexed"}


@app.get("/health")
async def health():
    return {"status": "ok", "model": "claude-opus-4-6"}
