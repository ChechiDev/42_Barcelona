#!/usr/bin/env python3

"""Test M06 alchemy imports and script behaviour"""

import ast
import subprocess
import sys
from pathlib import Path

import pytest


M06_DIR = Path(__file__).resolve().parents[1]

FIRE = "Fire element created"
WATER = "Water element created"
EARTH = "Earth element created"
AIR = "Air element created"
STRENGTH = f"Strength potion brewed with '{FIRE}' and '{WATER}'"
HEALING = f"Healing potion brewed with '{EARTH}' and '{AIR}'"
GOLD = (
    "Recipe transmuting Lead to Gold: brew "
    f"'{AIR}' and '{STRENGTH}' mixed with '{FIRE}'"
)


def run_script(script_name: str) -> subprocess.CompletedProcess[str]:
    """Run an M06 script from the module directory"""

    return subprocess.run(
        [sys.executable, script_name],
        cwd=M06_DIR,
        check=False,
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize(
    ("script_name", "expected_stdout"),
    [
        (
            "ft_alembic_0.py",
            "=== Alembic 0 ===\n"
            "Using: 'import ...' structure to access elements.py\n"
            f"Testing create_fire: {FIRE}\n",
        ),
        (
            "ft_alembic_1.py",
            "=== Alembic 1 ===\n"
            "Using: 'from ... import ...' structure to access elements.py\n"
            f"Testing create_water: {WATER}\n",
        ),
        (
            "ft_alembic_2.py",
            "=== Alembic 2 ===\n"
            "Accessing alchemy/elements.py using 'import ...' structure\n"
            f"Testing create_earth: {EARTH}\n",
        ),
        (
            "ft_alembic_3.py",
            "=== Alembic 3 ===\n"
            "Accessing alchemy/elements.py using 'from ... import ...' "
            "structure\n"
            f"Testing create_air: {AIR}\n",
        ),
        (
            "ft_alembic_5.py",
            "=== Alembic 5 ===\n"
            "Accessing the alchemy module using 'from alchemy import ...'\n"
            f"Testing create_air: {AIR}\n",
        ),
        (
            "ft_distillation_0.py",
            "=== Distillation 0 ===\n"
            "Direct access to alchemy/potions.py\n"
            f"Testing strength_potion: {STRENGTH}\n"
            f"Testing healing_potion: {HEALING}\n",
        ),
        (
            "ft_distillation_1.py",
            "=== Distillation 1 ===\n"
            "Using: 'import alchemy' structure to access potions\n"
            f"Testing strength_potion: {STRENGTH}\n"
            f"Testing heal alias: {HEALING}\n",
        ),
        (
            "ft_transmutation_0.py",
            "=== Transmutation 0 ===\n"
            "Using file alchemy/transmutation/recipes.py directly\n"
            f"Testing lead to gold: {GOLD}\n",
        ),
        (
            "ft_transmutation_1.py",
            "=== Transmutation 1 ===\n"
            "Import transmutation module directly\n"
            f"Testing lead to gold: {GOLD}\n",
        ),
        (
            "ft_transmutation_2.py",
            "=== Transmutation 2 ===\n"
            "Import alchemy module only\n"
            f"Testing lead to gold: {GOLD}\n",
        ),
        (
            "ft_kaboom_0.py",
            "=== Kaboom 0 ===\n"
            "Using grimoire module directly\n"
            "Testing record light spell: "
            "Spell recorded: Fantasy (Earth, wind and fire - VALID)\n",
        ),
    ],
)
def test_successful_scripts(script_name: str, expected_stdout: str) -> None:
    """Check successful scripts print the subject output"""

    result = run_script(script_name)

    assert result.returncode == 0
    assert result.stdout == expected_stdout
    assert result.stderr == ""


def test_elements_and_package_exports(monkeypatch: pytest.MonkeyPatch) -> None:
    """Check element factories and selected package exports"""

    monkeypatch.syspath_prepend(str(M06_DIR))

    import alchemy
    import elements
    from alchemy import elements as alchemy_elements

    assert elements.create_fire() == FIRE
    assert elements.create_water() == WATER
    assert alchemy_elements.create_earth() == EARTH
    assert alchemy.create_air() == AIR
    assert not hasattr(alchemy, "create_earth")


def test_potions_transmutation_and_light_grimoire(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Check reusable alchemy functions return subject strings"""

    monkeypatch.syspath_prepend(str(M06_DIR))

    import alchemy
    from alchemy.grimoire.light_spellbook import light_spell_record
    from alchemy.grimoire.light_validator import validate_ingredients

    assert alchemy.strength_potion() == STRENGTH
    assert alchemy.heal() == HEALING
    assert alchemy.lead_to_gold() == GOLD
    assert validate_ingredients("moon dust") == "moon dust - INVALID"
    assert validate_ingredients("Earth, wind and fire") == (
        "Earth, wind and fire - VALID"
    )
    assert light_spell_record("Fantasy", "Earth, wind and fire") == (
        "Spell recorded: Fantasy (Earth, wind and fire - VALID)"
    )
    assert light_spell_record("Void", "moon dust") == (
        "Spell rejected: Void (moon dust - INVALID)"
    )


def test_ft_alembic_4_fails_with_intentional_attribute_error() -> None:
    """Check alembic four fails after printing the expected prelude"""

    result = run_script("ft_alembic_4.py")

    assert result.returncode != 0
    assert result.stdout == (
        "=== Alembic 4 ===\n"
        "Accessing the alchemy module using 'import alchemy'\n"
        f"Testing create_air: {AIR}\n"
        "Now show that not all functions can be reached\n"
        "This will raise an exception!\n"
    )
    assert "AttributeError" in result.stderr
    assert "create_earth" in result.stderr


def test_ft_kaboom_1_fails_with_intentional_circular_import() -> None:
    """Check kaboom one fails with the expected circular import"""

    result = run_script("ft_kaboom_1.py")
    assert result.returncode != 0
    assert result.stdout == (
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION\n"
    )
    assert "ImportError" in result.stderr
    assert "circular import" in result.stderr


def test_functions_and_classes_follow_project_docstring_style() -> None:
    """Check M06 function and class docstrings follow project style"""

    for source_path in M06_DIR.rglob("*.py"):
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef),
            ):
                docstring = ast.get_docstring(node, clean=False)
                if (
                    isinstance(node, ast.FunctionDef)
                    and node.name == "__init__"
                ):
                    assert docstring is None, f"{source_path}:{node.lineno}"
                    continue
                assert docstring is not None, f"{source_path}:{node.lineno}"
                assert "\n" not in docstring, f"{source_path}:{node.lineno}"
                assert not docstring.endswith("."), (
                    f"{source_path}:{node.lineno}"
                )
