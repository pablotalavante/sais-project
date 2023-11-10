from dataclasses import dataclass

@dataclass
class Config:
    d_model=768
    d_head=64
    n_heads=12
    n_layers=2
    n_ctx=1024
    d_vocab=50278
    attention_dir="causal"
    attn_only=True #defaults to False
    tokenizer_name="EleutherAI/gpt-neox-20b"
    seed=398
    use_attn_result=True
    normalization_type=None
    positional_embedding_type="shortformer"