import tiktoken


coder = tiktoken.encoding_for_model("gpt-3.5-turbo-16k")
token_list = coder.encode("Você é um categorizador de produtos.")

print(token_list)
print(len(token_list))
input_cost = (len(token_list)/1000) * 0.0015
print(f"Custo: {input_cost}")