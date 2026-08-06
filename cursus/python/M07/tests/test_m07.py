#!/usr/bin/env python3

"""Test M07 Creature factories, capabilities, and strategies"""

import ast
import subprocess
import sys
from pathlib import Path

import pytest


M07_DIR = Path(__file__).resolve().parents[1]


def run_script(script_name: str) -> subprocess.CompletedProcess[str]:
    """Run an M07 script from the module directory"""

    return subprocess.run(
        [sys.executable, script_name],
        cwd=M07_DIR,
        check=False,
        capture_output=True,
        text=True,
    )


def test_battle_script_prints_subject_scenario() -> None:
    """Check battle script output for the abstract factory scenario"""

    result = run_script("battle.py")

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == (
        "Testing factory\n"
        "Flameling is a Fire type Creature\n"
        "Flameling uses Ember!\n"
        "Pyrodon is a Fire/Flying type Creature\n"
        "Pyrodon uses Flamethrower!\n"
        "Testing factory\n"
        "Aquabub is a Water type Creature\n"
        "Aquabub uses Water Gun!\n"
        "Torragon is a Water type Creature\n"
        "Torragon uses Hydro Pump!\n"
        "Testing battle\n"
        "Flameling is a Fire type Creature\n"
        "vs.\n"
        "Aquabub is a Water type Creature\n"
        "fight!\n"
        "Flameling uses Ember!\n"
        "Aquabub uses Water Gun!\n"
    )


def test_capacitor_script_prints_subject_scenario() -> None:
    """Check capacitor script output for capability scenarios"""

    result = run_script("capacitor.py")

    assert result.returncode == 0
    assert result.stderr == ""
    assert "Testing Creature with healing capability\n" in result.stdout
    assert "Sproutling heals itself for a small amount\n" in result.stdout
    assert (
        "Bloomelle heals itself and others for a large amount\n"
        in result.stdout
    )
    assert "Testing Creature with transform capability\n" in result.stdout
    assert "Shiftling performs a boosted strike!\n" in result.stdout
    assert "Morphagon unleashes a devastating morph strike!\n" in result.stdout


def test_tournament_script_prints_strategy_scenarios() -> None:
    """Check tournament script output for all strategy scenarios"""

    result = run_script("tournament.py")

    assert result.returncode == 0
    assert result.stderr == ""
    assert "Tournament 0 (basic)\n" in result.stdout
    assert "[ (Flameling+Normal), (Healing+Defensive) ]\n" in result.stdout
    assert "Tournament 1 (error)\n" in result.stdout
    assert (
        "Battle error, aborting tournament: Invalid Creature 'Flameling' "
        "for this aggressive strategy\n"
    ) in result.stdout
    assert "[ (Aquabub+Normal), (Healing+Defensive), " in result.stdout
    assert "(Transform+Aggressive) ]\n" in result.stdout


def test_packages_expose_factories_without_concrete_creatures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Check package interfaces hide concrete Creature classes"""

    monkeypatch.syspath_prepend(str(M07_DIR))

    import ex0
    import ex1

    assert hasattr(ex0, "FlameFactory")
    assert hasattr(ex0, "AquaFactory")
    assert not hasattr(ex0, "Flameling")
    assert not hasattr(ex0, "Aquabub")
    assert hasattr(ex1, "HealingCreatureFactory")
    assert hasattr(ex1, "TransformCreatureFactory")
    assert not hasattr(ex1, "Sproutling")
    assert not hasattr(ex1, "Shiftling")


def test_strategy_validation_and_invalid_action(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Check strategy validity and dedicated invalid strategy errors"""

    monkeypatch.syspath_prepend(str(M07_DIR))

    from ex0 import FlameFactory
    from ex1 import HealingCreatureFactory, TransformCreatureFactory
    from ex2 import AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

    flame = FlameFactory().create_base()
    healing = HealingCreatureFactory().create_base()
    transform = TransformCreatureFactory().create_base()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    assert not aggressive.is_valid(flame)
    assert aggressive.is_valid(transform)
    assert defensive.is_valid(healing)
    assert not defensive.is_valid(flame)
    with pytest.raises(
        InvalidStrategyError,
        match="Invalid Creature 'Flameling'",
    ):
        aggressive.act(flame)


def test_functions_and_classes_follow_project_docstring_style() -> None:
    """Check M07 function and class docstrings follow project style"""

    for source_path in M07_DIR.rglob("*.py"):
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
