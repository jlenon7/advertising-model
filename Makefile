# Remove compiled bytecode of source files
dev-clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*.pytest_cache' -exec rm -fr {} +

# Install all libraries of package
install-all:
	pipenv install --system --dev

# Install a package 
install:
	pipenv install $(pkg)

# Install a package in dev mode
install-dev:
	pipenv install --dev $(pkg)

# Run the model
model:
	pipenv run python src/main.py
