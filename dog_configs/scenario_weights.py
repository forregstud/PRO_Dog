# Универсальные весовые коэффициенты
UNIVERSAL_WEIGHTS = {
    "small_park": 1,
    "large_park": 1,
    "dog_walk_park": 3,
    "dog_train_park": 2,
    "veterinary": 0.75,
    "petshop": 0.5,
}

# Сценарии с порогами и сервисами
SCENARIOS = {
    "Сценарий 1": {"threshold": 15, "services": ["small_park", "petshop"]},
    "Сценарий 2": {"threshold": 30, "services": ["small_park", "large_park", "dog_walk_park", "veterinary"]},
    "Сценарий 3": {"threshold": 45, "services": ["small_park", "large_park", "dog_walk_park", "veterinary", "petshop", "dog_train_park"]},
}