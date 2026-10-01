"""Le contrat commun à tous les environnements Frondori, vérifié par
`frondori-engine` : PettingZoo, reproductibilité, spaces, métadonnées,
action neutre, rendu."""

import frondori_engine
from frondori_engine.testing import check_environment

from frondori_kitchen import KitchenEnv


def test_kitchen_is_discovered_once_installed():
    # Par l'entry point du pyproject.toml, sans aucun register() à la main.
    assert "kitchen-v0" in frondori_engine.registered_ids()
    assert frondori_engine.get_spec("kitchen-v0").package == "frondori-kitchen"
    assert isinstance(frondori_engine.make("kitchen-v0"), KitchenEnv)


def test_kitchen_respects_the_contract():
    check_environment("kitchen-v0")


def test_make_passes_kwargs_to_the_kitchen():
    env = frondori_engine.make("kitchen-v0", max_steps=3)
    env.reset()

    for _ in range(3):
        *_, truncations, _ = env.step({agent: 0 for agent in env.agents})

    assert all(truncations.values())
    assert env.agents == []
