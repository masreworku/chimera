.PHONY: setup test docker-build docker-test spec-check

setup:
	pip install -r requirements.txt

test:
	python -m pytest tests/

docker-build:
	docker build -t chimera .

docker-test:
	docker run --rm -it chimera

spec-check:
	@echo "Checking for mandatory spec files..."
	@test -f specs/_meta.md && echo "✅ _meta.md found" || echo "❌ _meta.md missing"
	@test -f specs/technical.md && echo "✅ technical.md found" || echo "❌ technical.md missing"
	@test -f specs/functional.md && echo "✅ functional.md found" || echo "❌ functional.md missing"
