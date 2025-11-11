.PHONY: install build package-install test lint format brain-games brain-even brain-calc brain-gcd brain-progression brain-prime clean

install:
    @pip install -e .

build:
    @python -m build

package-install:
    @pip install dist/*.whl

test:
    @pytest tests/

lint:
    @ruff check brain_games

format:
    @black brain_games/
    @isort brain_games/

brain-games:
    @python -m brain_games.scripts.brain_games

brain-even:
    @python -m brain_games.scripts.brain_even

brain-calc:
    @python -m brain_games.scripts.brain_calc

brain-gcd:
    @python -m brain_games.scripts.brain_gcd

brain-progression:
    @python -m brain_games.scripts.brain_progression

brain-prime:
    @python -m brain_games.scripts.brain_prime

clean:
    @rm -rf build/ dist/ .egg-info
    @rm -f .coverage .pytest_cache/
    @find . -type d -name '__pycache__' -exec rm -rf {} +
    @find . -type f -name '*.pyc' -delete
    @find . -type f -name '*.pyo' -delete
    @find . -type f -name '*~' -delete
