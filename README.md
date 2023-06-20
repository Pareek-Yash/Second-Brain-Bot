# Second-Brain-Bot

Welcome to Second-Brain-Bot! This repository contains a stateful chatbot powered by OpenAI's large language model (LLM). The chatbot is capable of handling customer queries or working as your personal assistant/second brain. With the use of natural language processing (NLP) techniques and prompt engineering, this chatbot aims to achieve 90% accuracy in response generation. When integrated with existing customer service platforms, it's able to reduce customer wait time by up to 50%.

## Overview

Second-Brain-Bot can be used for a variety of applications, including customer support, personal assistance, task management, and more. The chatbot keeps track of the conversation history, enabling context-aware responses.

## Features

- Stateful conversation handling
- Integration with customer service platforms
- High accuracy in response generation through NLP and prompt engineering
- Retrieval of relevant information from past conversations
- Scalable and customizable

## Directory Structure

```
Second-Brain-Bot/
│
├── Chatbot.ipynb                   # Main chatbot notebook
├── Upsert.ipynb                     # Notebook for updating/inserting chat history
├── vector_retrieval.py              # Script for retrieving relevant information from vectors
├── chat_history.py                  # Script for handling chat history
│
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.6 or later
- Jupyter Notebook
- OpenAI Python Library

Install the required libraries using `pip`:

```sh
pip install jupyter openai
```

### Usage

1. Clone this repository:

    ```sh
    git clone https://github.com/pareek-yash/Second-Brain-Bot.git
    cd Second-Brain-Bot
    ```

2. Launch Jupyter Notebook:

    ```sh
    jupyter notebook
    ```

3. Open `Chatbot.ipynb` and run the cells to start the chatbot.

4. Use `Upsert.ipynb` to handle chat history - updating and inserting conversations as required.

5. `vector_retrieval.py` and `chat_history.py` are Python scripts that are used in the notebooks for handling information retrieval and chat history respectively.

## Customization

- You can customize the chatbot prompts and responses in the `Chatbot.ipynb` notebook.
- For advanced customizations like changing the vector retrieval mechanism, you can modify the `vector_retrieval.py` script.

## Integration

To integrate Second-Brain-Bot with an existing customer service platform, you need to use the respective OpenAI’s API and weaviate account. Modify the `Chatbot.ipynb` to send and receive messages through the platform’s API instead of the notebook’s interface.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests or issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or concerns, please open an issue or contact the repository owner.

Thank you for checking out Second-Brain-Bot! 🤖🧠
