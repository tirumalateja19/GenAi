import tiktoken

encoder=tiktoken.encoding_for_model('gpt-4o');
print("Vocab size :",encoder.n_vocab) # 2,00,019 (200K)

text="teja sat on a mat"
tokens=encoder.encode(text)
print("Tokens :",tokens) # [411, 2067, 10139, 402, 261, 2450]

my_tokens = [6352, 2067, 10139, 402, 290, 2450]
decoded = encoder.decode(my_tokens)
print("Decoded :", decoded) # Teja sat on the mat