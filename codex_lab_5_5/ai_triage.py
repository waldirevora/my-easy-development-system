"""Triagem sintética: validação determinística, sem modelo ou serviço real.

O callback é código local confiável; esta função não o isola nem autentica.
"""


def triage_request(message, model_call) -> dict:
    """Devolve uma sugestão estruturada, sempre sujeita a revisão humana."""
    manual_review = {
        "status": "manual_review",
        "category": None,
        "priority": None,
        "requires_review": True,
    }
    if (
        not isinstance(message, str)
        or len(message) > 1000
        or not message.strip()
        or not callable(model_call)
    ):
        return manual_review

    try:
        response = model_call(message)
    except (TimeoutError, ConnectionError):
        return manual_review

    if not isinstance(response, dict) or set(response) != {"category", "priority"}:
        return manual_review

    category = response["category"]
    priority = response["priority"]
    if (
        not isinstance(category, str)
        or category not in ("comercial", "financeiro", "operacoes", "outros")
        or not isinstance(priority, str)
        or priority not in ("baixa", "media", "alta")
    ):
        return manual_review

    return {
        "status": "classified",
        "category": category,
        "priority": priority,
        "requires_review": True,
    }
