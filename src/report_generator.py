def normalize_decisions(decisions):
    rows = []

    for status, items in decisions.items():
        for item in items:
            rows.append({
                "campanha": item.get("campanha"),
                "status": status,
                "motivo": item.get("motivo")
            })

    return rows
