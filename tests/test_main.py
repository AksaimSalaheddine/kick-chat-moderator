import main


def test_main_processes_multiple_messages(monkeypatch, capsys):
    messages = iter(["hello", "spam", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(messages))

    main.main()

    output = capsys.readouterr().out

    assert "Message is allowed" in output
    assert "word: spam" in output
    assert "action: timeout" in output