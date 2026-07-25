
Skip to content
shrishail07
Rag_model_2
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights
Files
Go to file
t
T
README.md
app.py
config.py
prompt.py
rag.py
requirements.txt
utils.py
Rag_model_2
/prompt.py
shrishail07
shrishail07
Create prompt.py
7e911af
 · 
8 hours ago

Code

Blame
17 lines (11 loc) · 224 Bytes
PROMPT = """
You are an AI assistant.

Answer only using the provided context.

If the answer is not in the context, say

"I don't know based on the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""
 Rag_model_2/prompt.py at main · shrishail07/Rag_model_2
