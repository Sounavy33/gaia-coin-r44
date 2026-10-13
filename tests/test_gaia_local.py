from scripts.gaia_context import GaiaContext, GaiaLLMAdapter, GaiaReport


def test_gaia_context_add_and_summary():
    ctx = GaiaContext(user_name="Sounavy", storage_dir=".tmp_gaia_test")
    ctx.add("user", "Quero resumir minhas ideias para a borda.")
    ctx.add("assistant", "Vamos organizar contexto e relatórios locais.")
    summary = ctx.summarize(limit=2)
    assert "borda" in summary.lower()
    assert "organizar" in summary.lower()


def test_gaia_llm_adapter_offline_mode():
    adapter = GaiaLLMAdapter(model_path=None, allow_online=False)
    text = adapter.infer("Explica o projeto", lang="pt")
    assert "MODO OFFLINE" in text


def test_gaia_report_is_signed_and_contains_hash():
    ctx = GaiaContext(user_name="Sounavy", storage_dir=".tmp_gaia_report")
    ctx.add("user", "Relatório de contexto para Gaia.")
    adapter = GaiaLLMAdapter(model_path=None, allow_online=False)
    report = GaiaReport(ctx, adapter).build("Explique o projeto", lang="pt")
    assert "hash" in report
    assert len(report["hash"]) > 10
    assert "answer" in report
