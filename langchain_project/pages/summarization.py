from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredPDFLoader
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

# Summarizing Using Refine Chain
# https://python.langchain.com/docs/use_cases/summarization#option-3-refine
"""
The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. 
For each document, it passes all non-document inputs, the current document, and the latest intermediate answer to an LLM chain to get a new answer.
"""


def summarization_refine():
    loader = UnstructuredPDFLoader('files/attention_is_all_you_need.pdf')
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
    print(f"{len(chunks) = }")

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    # chain = load_summarize_chain(
    #     llm=llm,
    #     chain_type='refine',
    #     verbose=False
    # )
    # output_summary = chain.run(chunks)
    # print(f"{output_summary = }")

    prompt_template = """
    Write a concise summary of the following extracting the key information:
    Text: `{text}`
    CONCISE SUMMARY:
    """

    initial_prompt = PromptTemplate(
        template=prompt_template,
        input_variables=['text']
    )

    refine_template = '''
        Your job is to produce a final summary.
        I have provided an existing summary up to a certain point: {existing_answer}.
        Please refine the existing summary with some more context below.
        ------------
        {text}
        ------------
        Start the final summary with an INTRODUCTION PARAGRAPH that gives an overview of the topic FOLLOWED
        by BULLET POINTS if possible AND end the summary with a CONCLUSION PHRASE.
    
    '''
    refine_prompt = PromptTemplate(
        template=refine_template,
        input_variables=['existing_answer', 'text']
    )

    chain = load_summarize_chain(
        llm=llm,
        chain_type='refine',
        question_prompt=initial_prompt,
        refine_prompt=refine_prompt,
        return_intermediate_steps=False
    )

    refined_output_summary = chain.run(chunks)
    return refined_output_summary
    # print(f"{refined_output_summary = }")


if __name__ == "__main__":
    st.markdown("# LLM Summarization ❄️")
    input_upload_file = st.file_uploader('Upload a file:')
    st.write("input_upload_file", input_upload_file)
    btn_click = st.button(label='start summarizing')
    if btn_click:
        
        with st.spinner('Reading, chunking and embedding file ...'):
            output = summarization_refine()
            st.write(output)
