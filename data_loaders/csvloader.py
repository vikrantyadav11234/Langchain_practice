from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="/home/ubuntu/Langchain/data_loaders/updated_summary_report.csv")

docs = loader.load()

print(docs[1].page_content)

print(docs[0].metadata)

