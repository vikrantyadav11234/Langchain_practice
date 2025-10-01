# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv()

# with_structured_output
# we can define a pydantic model and pass it to the with_structured_output method
# the model will be used to validate the output of the model
# the output will be a dictionary with the keys as the field names of the model
# and the values as the values of the fields
# if the output is not valid, an error will be raised
# we can also use the invoke method to get the output of the model
# the output will be a dictionary with the keys as the field names of the model
# and the values as the values of the fields

llm = HuggingFaceEndpoint(
    repo_id ="TinyLlama/TinyLlama-1.1B-chat-v1.0",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm,
                               temperature=0)

# schema
class Review(BaseModel):
    
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description="Write down all the cons inside a list")
    name: Optional[str] = Field(description="   Write the name of the reviewer")


    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)