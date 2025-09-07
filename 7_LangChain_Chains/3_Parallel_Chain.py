from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model = 'gemini-1.5-pro')

prompt_1 = PromptTemplate(
    template="Generate a short and simple notes from the follwing text \n {text}",
    input_variables=['text']

)

prompt_2 = PromptTemplate(
    template="Generate a 4 short question answer from the follwoing \n {text}",
    input_variables=['text']
)

prompt_3 = PromptTemplate (
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model | parser ,
    'quiz' : prompt_2 | model | parser
})

merge_chain = prompt_3 | model | parser

output_chain = parallel_chain | merge_chain

text = """
Transformers in Machine Learning
Transformers are a class of deep learning models that have revolutionized natural language processing (NLP) and other AI tasks. They use self-attention mechanisms to process data efficiently and are the backbone of modern models like BERT, GPT, and T5.

Advantages of Transformers:
Parallel Processing: Unlike traditional recurrent models (RNNs, LSTMs), transformers process entire sequences simultaneously, making them highly efficient.

Long-Range Dependencies: The self-attention mechanism allows transformers to capture long-range relationships in data.

Transfer Learning: Pre-trained transformer models can be fine-tuned on various tasks, reducing training time and data requirements.

Scalability: Transformers scale well with large datasets and can be trained on powerful hardware like TPUs and GPUs.

Versatile Applications: Transformers are widely used in NLP, computer vision (Vision Transformers - ViTs), and even protein structure predictions.

Disadvantages of Transformers:
High Computational Cost: Training transformers requires significant computational power and memory.

Data-Hungry: Large-scale transformers need vast amounts of labeled data to perform well.

Interpretability Challenges: The attention mechanism provides some insights, but overall, transformers are still considered black-box models.

Latency in Real-Time Applications: Due to their complexity, transformers may have higher inference latency compared to simpler models.

Transformers are implemented in frameworks like Hugging Face’s transformers library, making it easier to deploy models like GPT, BERT, and T5 for various applications. They continue to advance state-of-the-art AI across multiple domains.


"""
result = output_chain.invoke({'text':text})

print(result)


output_chain.get_graph().print_ascii()