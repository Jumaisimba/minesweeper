import settings



def get_height_by_percentage(percentage: int) -> float:
    """Вычисляет процент от высоты"""
    return (settings.HEIGHT / 100) * percentage

def get_width_by_percentage(percentage: int) -> float:
    """Вычисляет процент от ширины"""
    return (settings.WIDTH / 100) * percentage

