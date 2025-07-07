# tests/test_basic_substitution.py
import os
from pathlib import Path

def test_poscar_exists():
    assert Path("POSCAR").exists(), "POSCAR file is missing"

