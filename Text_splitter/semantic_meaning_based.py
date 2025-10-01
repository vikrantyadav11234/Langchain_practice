from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
text = """
Artificial Intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. It encompasses a variety of techniques and approaches, including machine learning, natural language processing, computer vision, and robotics. AI systems can analyze data, recognize patterns, make decisions, and learn from experience.   
The field of AI has seen significant advancements in recent years, leading to the development of applications such as virtual assistants, autonomous vehicles, and recommendation systems. As AI continues to evolve, it holds the potential to transform various industries and improve our daily lives.
However, the rise of AI also raises important ethical and societal questions, such as the impact on employment, privacy concerns, and the need for responsible AI development and deployment.
"""
splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type ="Standard_deviation",
    breakpoint_threshold_amount=1.0,
)   
   
texts = splitter.create_documents([text])
print(texts)
 