from uuid import uuid4


def gerarID() -> str:
    """gerarID gera um GUID em formato str"""
    return str(uuid4())