VERSION=v0
DOCKERUSER=ash002019

black:
	python -m black src

isort:
	python -m isort src

build:
	docker build -t recentcves .

build-dev:
	docker build -t recentcves:dev .

push:
	docker tag recentcves $(DOCKERUSER)/recentcves:$(VERSION)
	docker push $(DOCKERUSER)/recentcves:$(VERSION)
	docker tag recentcves $(DOCKERUSER)/recentcves:latest
	docker push $(DOCKERUSER)/recentcves:latest

deploy:
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml

delete:
	kubectl delete deploy/recentcves
	kubectl delete service/recentcves-svc