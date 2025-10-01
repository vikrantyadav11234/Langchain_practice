from langchain.text_splitter import PythonCodeTextSplitter, RecursiveCharacterTextSplitter,Language

text = """
def example_function(param1, param2):

    if param1 > param2:
        return param1 - param2
    else:
        return param2 - param1
        
class ExampleClass: 
    def __init__(self, value):
        self.value = value  
        def get_value(self):
            return self.value"""
            
splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=100, 
    chunk_overlap=0,   
    language=Language.PYTHON)

texts = splitter.split_text(text)
print(texts)
print(len(texts))