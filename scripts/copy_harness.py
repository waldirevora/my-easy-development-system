"""Copie as instruções do MEDS para um projeto novo, sem sobrescrever arquivos."""

import argparse
import hashlib
from pathlib import Path
import sys

from check import find_root


HARNESS_FILES = (
    "AGENTS.md", "LICENSE",
    "standards/README.md", "standards/product-system-v4.md",
    "standards/web-experience-business-systems-v1.md",
    "standards/capability-routing-v1.md", "standards/authentication-security-v1.md",
    "standards/environment-variables-secrets-v1.md", "standards/ai-engineering-v1.md",
    "standards/ai-assisted-secure-development-threat-v1.md",
    "templates/README.md", "templates/gate-a-task-brief.md",
    "templates/qa-review-report.md", "templates/security-gate-review.md",
    "templates/gate-b-release-approval.md", "templates/continuity-prompt.md",
    *tuple(f".agents/skills/{name}/SKILL.md" for name in (
        "ai-engineering-production", "ai-search-visibility",
        "clara-premium-copywriting", "data-persistence-engineering",
        "julian-premium-design", "kael-interface-engineering",
        "quality-engineering-testing", "release-deployment-reliability",
        "seo-technical", "software-design-solid", "vera-architecture-security",
        "visual-interface-qa",
    )),
)


def copy_harness(source: Path, destination: Path) -> Path:
    """Prepare somente um destino ausente ou vazio, com pai já existente."""
    source = source.resolve()
    destination = destination.expanduser().absolute()
    for part in (destination, *destination.parents):
        if part.is_symlink():
            raise ValueError("Destino e ancestrais não podem ser links simbólicos.")
    destination = destination.resolve()
    if destination.is_relative_to(source):
        raise ValueError("Crie o projeto fora da instalação MEDS de origem.")
    if not destination.parent.is_dir():
        raise ValueError("O diretório pai do destino deve existir e estar autorizado.")
    if destination.exists() and (
        not destination.is_dir() or any(destination.iterdir())
    ):
        raise ValueError("Destino ocupado: nenhum arquivo foi sobrescrito.")

    # Carregar o inventário aprovado antes da primeira escrita no destino.
    payloads = {}
    for relative in HARNESS_FILES:
        path = source / relative
        for part in (path, *path.parents):
            if part == source:
                break
            if part.is_symlink():
                raise ValueError(f"Fonte contém link simbólico: {relative}")
        if not path.resolve().is_relative_to(source) or not path.is_file():
            raise ValueError(f"Fonte essencial ausente ou externa: {relative}")
        payloads[relative] = path.read_bytes()

    agents = payloads["AGENTS.md"].decode("utf-8")
    old_objective = "Este repositório contém o My Easy Development System."
    if old_objective not in agents:
        raise ValueError("Objetivo de AGENTS.md mudou; revisar adaptação antes de copiar.")
    agents = agents.replace(old_objective,
        "Este projeto aplica o My Easy Development System aos seus próprios requisitos.", 1)
    # O destino externo usa sua própria raiz, sem criar workspaces recursivos.
    start = "<!-- MEDS-WORKSPACE-START -->"
    end = "<!-- MEDS-WORKSPACE-END -->"
    if (agents.count(start) != 1 or agents.count(end) != 1
            or agents.index(end) < agents.index(start)):
        raise ValueError("Marcadores de escopo MEDS ausentes ou inválidos; revisar adaptação.")
    before, scoped = agents.split(start, 1)
    _, after = scoped.split(end, 1)
    agents = (before + "## Raiz do projeto independente\n\n"
              "Desenvolver exclusivamente na raiz autorizada deste projeto, incluindo "
              "testes, assets, documentação e temporários. Não criar workspaces/ "
              "por rotina nem modificar a instalação MEDS de origem ou outros projetos. "
              "Git próprio exige solicitação explícita. Respeitar permissões reais; "
              "a regra de escopo não substitui o sandbox.\n" + after)
    agents += ("\nAs fontes copiadas do MEDS usam Apache-2.0; consulte "
               "[MEDS-LICENSE](MEDS-LICENSE). A licença do produto é definida separadamente.\n")
    payloads["AGENTS.md"] = agents.encode("utf-8")

    destination.mkdir(exist_ok=True)
    for relative, content in payloads.items():
        target = destination / ("MEDS-LICENSE" if relative == "LICENSE" else relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as output:
            output.write(content)
        if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(content).digest():
            raise OSError(f"Integridade divergente: {relative}")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path,
                        help="Pasta nova ou vazia; o pai deve estar autorizado e existir.")
    args = parser.parse_args()
    try:
        root = find_root(Path(__file__))
        destination = copy_harness(root, args.destination)
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: 28 arquivos preparados em {destination}.")
    print("Objetivo de AGENTS adaptado; licença em MEDS-LICENSE; confira a descoberta no Codex.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
