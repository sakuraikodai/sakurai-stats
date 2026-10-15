def mean(values: list[float]) -> float:
    """数値のリストの算術平均を返す。"""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
