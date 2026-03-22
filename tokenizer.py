import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        tokens = [t.strip() for t in tokens if t.strip()]
        ids = [self.str_to_int.get(t, 0) for t in tokens]
        return ids

    def decode(self, ids):
        tokens = [self.int_to_str.get(i, "<|unk|>") for i in ids]
        text = " ".join(tokens)
        text = re.sub(r'\s+([,.:;?_!"\'])', r'\1', text)
        return text

file_path = "the-verdict.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

tokens_for_vocab = re.split(r'([,.:;?_!"()\']|--|\s)', text)
tokens_for_vocab = [t.strip() for t in tokens_for_vocab if t.strip()]

vocab = {token: idx for idx, token in enumerate(tokens_for_vocab, start=1)}

print("vocab size:", len(vocab))
print("first 10 tokens:", list(vocab.items())[:10])

tokenizer = SimpleTokenizerV1(vocab)

ids = tokenizer.encode(text)
print("ids:", ids[:50])

decoded = tokenizer.decode(ids)
print("decoded:", decoded[:200])