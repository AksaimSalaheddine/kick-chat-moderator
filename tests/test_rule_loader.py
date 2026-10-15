import json
import pytest

from rule_loader import load_rules

#  Previous code
# def test_load_rules(tmp_path):
#     rules_data = [
#         {
#             "word": "spam",
#             "severity": "medium",
#             "action": "timeout",
#         }
#     ]
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     result = load_rules(rules_file)
#
#     assert result == rules_data
#
#
# def test_load_rules_rejects_non_dictionary_item(tmp_path):
#     rules_data = ["not a rule"]
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     with pytest.raises(
#             ValueError,
#             match="Each moderation rule must be a dictionary"
#     ):
#         load_rules(rules_file)
#
#
# def test_load_rules_rejects_missing_fields(tmp_path):
#     rules_data = [
#         {
#             "word": "spam",
#             "severity": "medium"
#         }
#     ]
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     with pytest.raises(
#         ValueError,
#         match="Each rule must contain word, severity, and action"
#     ):
#         load_rules(rules_file)
#
#
# def test_load_rules_rejects_invalid_severity(tmp_path):
#     rules_data = [
#         {
#             "word": "spam",
#             "severity": "extreme",
#             "action": "timeout"
#         }
#     ]
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     with pytest.raises(
#             ValueError,
#             match="Invalid severity"
#     ):
#         load_rules(rules_file)
#
#
# def test_load_rules_rejects_invalid_action(tmp_path):
#     rules_data = [
#         {
#             "word": "spam",
#             "severity": "medium",
#             "action": "delete"
#         }
#     ]
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     with pytest.raises(
#             ValueError,
#             match="Invalid action"
#     ):
#         load_rules(rules_file)
#
#
# def test_load_rules_rejects_missing_file(tmp_path):
#     missing_file = tmp_path / "missing.json"
#
#     with pytest.raises(FileNotFoundError):
#         load_rules(missing_file)
#
#
# def test_load_rules_rejects_invalid_json(tmp_path):
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text("{ invalid json")
#
#     with pytest.raises(json.JSONDecodeError):
#         load_rules(rules_file)
#
#
# def test_load_rules_rejects_non_list_json(tmp_path):
#     rules_data = {
#         "word": "spam",
#         "severity": "medium",
#         "action": "timeout"
#     }
#
#     rules_file = tmp_path / "rules.json"
#     rules_file.write_text(json.dumps(rules_data))
#
#     with pytest.raises(
#             ValueError,
#             match="Moderation rules must be a list"
#     ):
#         load_rules(rules_file)
#  Previous code

def test_load_rules(tmp_path):
    rules_data = {
        "ban": ["example prohibited term"],
        "timeout": ["spam"],
        "warn": ["idiot"]
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    result = load_rules(rules_file)

    assert result == rules_data


def test_load_rules_rejects_non_dictionary_json(tmp_path):
    rules_data = ["spam", "idiot"]

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(
        ValueError,
        match="Moderation rules must be a dictionary"
    ):
        load_rules(rules_file)


def test_load_rules_rejects_missing_action(tmp_path):
    rules_data = {
        "ban": [],
        "timeout": []
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(
        ValueError,
        match="Rules must contain ban, timeout, and warn"
    ):
        load_rules(rules_file)


def test_load_rules_rejects_invalid_action(tmp_path):
    rules_data = {
        "ban": [],
        "timeout": [],
        "warn": [],
        "delete": ["spam"]
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(ValueError, match="Invalid moderation action"):
        load_rules(rules_file)


def test_load_rules_rejects_non_list_action_value(tmp_path):
    rules_data = {
        "ban": [],
        "timeout": "spam",
        "warn": []
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(
        ValueError,
        match="Each action must contain a list of words"
    ):
        load_rules(rules_file)


def test_load_rules_rejects_empty_word(tmp_path):
    rules_data = {
        "ban": [],
        "timeout": [],
        "warn": [""]
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(
        ValueError,
        match="Each word must be a non-empty string"
    ):
        load_rules(rules_file)


def test_load_rules_rejects_non_string_word(tmp_path):
    rules_data = {
        "ban": [],
        "timeout": [123],
        "warn": []
    }

    rules_file = tmp_path / "rules.json"
    rules_file.write_text(json.dumps(rules_data))

    with pytest.raises(
        ValueError,
        match="Each word must be a non-empty string"
    ):
        load_rules(rules_file)


def test_load_rules_rejects_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_rules(missing_file)


def test_load_rules_rejects_invalid_json(tmp_path):
    rules_file = tmp_path / "rules.json"
    rules_file.write_text("{ invalid json")

    with pytest.raises(json.JSONDecodeError):
        load_rules(rules_file)

