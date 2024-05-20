# Blog_Genration

Welcome to the Blog Generation App, a Streamlit-based application designed to generate blogs using the Llama model from ctransformers. This tool allows users to generate blog posts tailored to different audiences by specifying the topic, number of words, and target audience(["Researchers", "Common People", "Data Scientists"] in this case).

**It can generate blogs on any topic with specified number of words and target audience**
![WhatsApp Image 2024-05-20 at 10 37 47_a0ff6526](https://github.com/Sudhanshu480/Blog_Genration/assets/96736479/bdf60fc4-10c0-4607-bdea-bede4bc698f3)


## Features:

- **Customizable Blog Generation**: Generate blogs based on user-defined topics, word count, and target audience.
- **Easy to Use Interface**: Simple and intuitive UI built with Streamlit.
- **Advanced Language Model**: Leverages the power of the Llama model from ctransformers for high-quality content generation.

**It can even generate response on Games and Sports**
![WhatsApp Image 2024-05-20 at 10 32 32_0ad8cb32](https://github.com/Sudhanshu480/Blog_Genration/assets/96736479/626d8551-3a31-4e79-9cdb-539a0068fd0e)

**Literature:**
![WhatsApp Image 2024-05-20 at 10 36 02_1e97051b](https://github.com/Sudhanshu480/Blog_Genration/assets/96736479/f8d0fe59-64e2-4b5c-98c1-ff16fa80eb32)


## How it Works:

The core functionality of the Blog Generation App revolves around the `getLlamaResponse` function. This function effectively combines user input with a language model to generate custom blog content. Here’s a breakdown of how it works:

- **User Input**: The function takes three inputs from the user: `topic`, which is the subject of the blog post, `no_of_words`, which is the desired length of the blog post in words, and `blog_style`, which is the intended audience for the blog (e.g., Researchers, Common People, Data Scientists).

- **Language Model Initialization**: The function initializes a language model using the `CTransformers` class from the `langchain` library's `ctransformers` module, which provides access to the Llama model. The model file (`llama-2-7b-chat.ggmlv3.q8_0.bin`) should be placed in the `models` directory. The model type is specified as 'llama'. Configuration parameters for the model are set, including `max_new_tokens`, which defines the maximum number of tokens (words or parts of words) that the model will generate in its response, and `temperature`, which controls the randomness of the output. A lower temperature (like 0.01) makes the output more deterministic and focused.

- **Prompt Template Definition**: A string template is defined to structure the prompt, with placeholders for the user inputs. The `PromptTemplate` class helps in creating the prompt by replacing these placeholders with the actual values provided by the user.

- **Prompt Formatting**: The prompt is formatted with the input variables provided by the user. This formatted prompt is then passed to the language model, which processes the prompt and generates a response.

- **Response Generation**: The generated blog post is returned by the function.

This produces high-quality blog content tailored to specific topics, lengths, and audiences. This makes it a powerful tool for quickly generating blog posts across various subjects and styles.

**Generating Blogs for different audience**
![WhatsApp Image 2024-05-20 at 10 39 09_e2170a99](https://github.com/Sudhanshu480/Blog_Genration/assets/96736479/7a167ee0-8e4e-4b2f-9685-6bff31068839)


### Prerequisites:

- Python 3.8 or higher (3.10.0 used by me)
- Streamlit
- langchain
- ctransformers


### **Download the Llama Model**:

Place the `llama-2-7b-chat.ggmlv3.q8_0.bin` model file in the `models` directory. Ensure that the path in the script (`models/llama-2-7b-chat.ggmlv3.q8_0.bin`) matches the location of the model file. This or any other model according to user requirements can be downloaded from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main).
   
We are using the `llama-2-7b-chat.ggmlv3.q8_0.bin` model because it is a state-of-the-art language model that excels in generating coherent and contextually relevant text. This model is part of the Llama (Large Language Model) series and has 7 billion parameters (7B), which allows it to understand and generate detailed and nuanced content. The large number of parameters enables the model to capture complex patterns in data, making it highly effective for natural language processing tasks. Additionally, it uses advanced techniques for optimizing performance and generating high-quality outputs, making it an ideal choice for our blog generation application. The `ggmlv3.q8_0` variant indicates a specific quantization method used to optimize the model's efficiency and performance without compromising its accuracy. However, any other relevant model can also be used.

## Usage:

1. **Run the Streamlit App**:
   ```
   streamlit run app.py
   ```

2. **Generate a Blog**:
   - Enter the blog topic in the input field.
   - Specify the desired number of words.
   - Select the target audience from the dropdown menu.
   - Click the "Generate" button.

3. **View the Generated Blog**:
   - The generated blog will be displayed on the screen once the model completes the generation process.

## File Structure

```
blog-generation-app/
│
├── models/
│   └── llama-2-7b-chat.ggmlv3.q8_0.bin  # Place the model file here
│
├── app.py                                # Main application script
│
├── requirements.txt                      # Required Python packages
│
└── README.md                             # Project documentation
```

## Contributions

Contributions are welcome!

