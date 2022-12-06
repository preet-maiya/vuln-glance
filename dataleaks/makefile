VERSION=v0
DOCKERUSER=ash002019

black:
	python -m black src

isort:
	python -m isort src

build:
	docker build -t dataleaks .

build-dev:
	docker build -t dataleaks:dev .

push:
	docker tag dataleaks $(DOCKERUSER)/dataleaks:$(VERSION)
	docker push $(DOCKERUSER)/dataleaks:$(VERSION)
	docker tag dataleaks $(DOCKERUSER)/dataleaks:latest
	docker push $(DOCKERUSER)/dataleaks:latest

run:
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml