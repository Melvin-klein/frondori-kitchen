# frondori-kitchen

`kitchen-v0` : une cuisine coopérative à deux chefs, façon Overcooked, pour
Frondori. Les deux agents reçoivent exactement la même
récompense : +1 par soupe servie. Grille, actions discrètes, pas de
physique, Python pur.

## Installation

```bash
pip install frondori-kitchen      # installe aussi frondori-engine
```

Pour développer, depuis un clone : `pip install -e ".[dev]"`.

## Utilisation

```python
import frondori_engine

env = frondori_engine.make("kitchen-v0")   # découvert automatiquement
observations, infos = env.reset(seed=0)
while env.agents:
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}
    observations, rewards, terminations, truncations, infos = env.step(actions)
```

Paramètres (les matchs de compétition utilisent toujours les valeurs par
défaut) : `layout`, `onions_needed` (2), `cook_time` (5), `max_steps` (200).

Règles, observations et actions : docstring de `frondori_kitchen.env`, et en
anglais sur le site (Documentation > Environments).

## Entraîner un agent

Avec le SDK (`pip install "frondori-sdk[train]"`), en une ligne :

```python
from frondori import Agent
from frondori.agents import PPO

agent = PPO()
Agent(environment="kitchen-v0", local=True).train(agent, total_timesteps=2_000_000)
```

La récompense (+1 par soupe servie) est trop rare pour un agent qui débute :
sans aide, il n'apprend rien. Façonnée par potentiel dans un wrapper
Gymnasium (`PPO(wrap_env=...)`, exemple complet dans la documentation du site,
Train Locally > Shaping the reward), PPO sert 11 soupes par match après 2
millions de pas, environ 8 minutes sur CPU.

## Développer / tester

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ../frondori-engine -e ".[dev]"
python -m pytest
```

## Publier une version

1. Mettre à jour `version` dans `pyproject.toml` et commiter.
2. Pousser un tag du même numéro : `git tag v0.1.0 && git push origin v0.1.0`.

La CI (`.github/workflows/ci.yml`) teste, construit et publie sur PyPI ; elle
refuse un tag qui ne correspond pas à la version. Publication par *Trusted
Publishing*, sans token : à configurer une fois sur PyPI (projet `frondori-kitchen` >
Publishing > trusted publisher GitHub : ce dépôt, workflow `ci.yml`,
environnement `pypi`).

`frondori-engine` doit être publié AVANT ce paquet (il en dépend, et la CI
l'installe depuis PyPI).

Licence : MIT.
