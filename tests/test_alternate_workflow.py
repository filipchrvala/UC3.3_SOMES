"""Legacy sustainable `run_workflow.py` tests — not part of operational UC3.3 DAG."""
from __future__ import annotations

import pytest

pytest.skip(
    "Operational UC3.3 no longer ships UserInput/Sizing/Feasibility pieces "
    "or the local run_workflow.py investment path.",
    allow_module_level=True,
)
