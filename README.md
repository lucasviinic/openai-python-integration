# OpenAI Python Integration

This repository comprises my studies regarding the integration of a Python project with the OpenAI API.

**Step 1:** API Integration

- Adjusting Playground parameters such as temperature and maximum length to control the creativity and output of GPT, aiming to generate more coherent and context-adapted responses.
- Utilizing the OpenAI library to make requests to the API and generate responses from a GPT-3.5 model, learning how to pass system and user messages, as well as safeguarding the API key for security.
- Hiding identification keys in environment variables to protect sensitive information when performing API integrations.

**Step 2:** Prompt engineering and prompt template

- Using the GPT-3 API to categorize products in an e-commerce context, adjusting parameters to obtain multiple responses, and exploring the API documentation to understand its operation and available options.
- Enhancing the system prompt to guide GPT model responses with strategies such as specifying the desired output format and providing examples.
- Creating a product categorization function using a prompt template to dynamically insert parameters such as valid categories and product names, enabling a more flexible and organized interaction with the code.

**Step 3:** Costs, models and token count

- Selecting the appropriate language model for our tasks, taking into account token limits, context, and cost, and choosing based on the specific needs of the project.
- Utilizing the TikToken library to count and estimate the number of tokens in a text to assess the usage of language models, understand the internal structure of tokens, and calculate processing costs.
- Dynamically choosing language models based on the number of input tokens and calculating the expected size of the output to ensure proper functioning of text generation.

**Step 4:** Batch and error handler

- Using language models to perform sentiment analysis on product reviews, summarizing the evaluations, determining the overall sentiment (positive, neutral, or negative), identifying strengths and weaknesses, and saving the results in files.
- Refactoring the code to process sentiment analyses in batches, utilizing a function to perform the analysis for each product in the list, and adding prints to track progress and identify potential errors during batch analysis.
- Handling exceptions when making batch calls to an API using try and except code blocks to capture and handle different types of errors.
- Implementing a retry logic, where we attempt the call again after a short interval in case of an error, to address temporary issues.
- Managing rate limits in the use of the GPT API, which are defined by the number of requests per day (RPD), requests per minute (RPM), and the number of tokens per minute (TPM).

**Step 5:** Product Recommendation Email Challenge

- Transform the result of the GPT call into a structured JSON object, allowing iteration for each client and the execution of product recommendation and email writing operations based on the identified profiles.
- Load a list of products from a text file, create a function to recommend products based on customer purchase profiles, and format the output of recommendations in a readable manner.