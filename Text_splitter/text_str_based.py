from langchain.text_splitter import RecursiveCharacterTextSplitter
 
text = """
 This is a long text that needs to be split into smaller chunks. The text splitter will ensure that the chunks are of manageable size and do not exceed the specified chunk size. This is particularly useful for processing large documents or texts in natural language processing tasks.
 The text splitter will also handle overlaps between chunks to ensure that important context is not lost during the splitting process.
 """
 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, 
    chunk_overlap=0,   
    separators=["\n\n", "\n", " ", ""]
        
    )


texts = splitter.split_text(text)
print(texts)
print(len(texts))
        