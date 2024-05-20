import streamlit as st
from langchain.llms.ctransformers import CTransformers
from langchain.prompts import PromptTemplate

# Run this command in terminal to install all the requirements:
# pip install -r requirements.txt

def getLlamaResponse(topic, no_of_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config={'max_new_tokens': 256, 'temperature': 0.01})

    # Defining the prompt template
    template = """
    Write a blog for {blog_style} on the topic "{topic}" within {no_of_words} words.
    """
    prompt = PromptTemplate(input_variables=["topic", "blog_style", "no_of_words"], template=template)

    # Format the prompt with the input variables
    formatted_prompt = prompt.format(topic=topic, blog_style=blog_style, no_of_words=no_of_words)

    # Generate the response from the model
    response = llm(formatted_prompt)
    return response

def main():
    st.set_page_config(page_title="Blog Generation", page_icon=":bulb:", layout="centered", initial_sidebar_state="collapsed")
    st.header("Generate Blogs :bulb:")

    # Input fields for topic
    topic = st.text_input("Enter the Blog Topic!")
    
    # Creating two more fields for number of words, and blog style
    col1, col2 = st.columns([5, 5])
    with col1:
        no_of_words = st.text_input("Enter the number of words")
    with col2:
        blog_style = st.selectbox("Blog is for:", ("Researchers", "Common People", "Data Scientists"), index=0)

    submit = st.button("Generate")

    if submit:
        with st.spinner("In progress..."):

            # Call the function to generate the blog
            response = getLlamaResponse(topic, no_of_words, blog_style)
            st.write(response)

            st.success("DONE!")

if __name__ == '__main__':
    main()