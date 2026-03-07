"""
Unit tests for DAL-Aware Agent.
"""

import pytest
from src.agent.memory import DALMemory


class TestDALMemory:

    def test_set_and_get_dal(self):
        memory = DALMemory()
        memory.set_dal("A")
        assert memory.get_dal() == "A"

    def test_all_dal_levels(self):
        memory = DALMemory()
        for level in ["A", "B", "C", "D"]:
            memory.set_dal(level)
            assert memory.get_dal() == level

    def test_reset_clears_dal(self):
        memory = DALMemory()
        memory.set_dal("B")
        memory.reset()
        assert memory.get_dal() is None

    def test_default_dal_is_none(self):
        memory = DALMemory()
        assert memory.get_dal() is None


class TestDALAwareAgent:

    def test_set_invalid_dal_raises(self):
        from src.agent.dal_agent import DALAwareAgent
        agent = DALAwareAgent()
        with pytest.raises(AssertionError):
            agent.set_dal("E")

    def test_query_without_dal_raises(self):
        from src.agent.dal_agent import DALAwareAgent
        agent = DALAwareAgent()
        with pytest.raises(ValueError):
            agent.query("What are the requirements?")
