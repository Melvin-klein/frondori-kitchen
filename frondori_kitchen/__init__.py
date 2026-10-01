"""`kitchen-v0` : cuisine coopérative à deux chefs, pour Frondori.

Installé, l'environnement est découvert automatiquement par
`frondori-engine` (entry point `frondori.environments`, cf.
`pyproject.toml`) :

    import frondori_engine
    env = frondori_engine.make("kitchen-v0")

Les règles complètes sont dans `frondori_kitchen.env` (et en anglais, dans
`KitchenEnv.metadata["documentation"]`, affichées par le site).
"""

from frondori_kitchen.env import DEFAULT_LAYOUT, KitchenEnv

__all__ = ["DEFAULT_LAYOUT", "KitchenEnv"]
