VERSION=v0
DOCKERUSER=${docker_user}

black:
	python -m black src

isort:
	python -m isort src

build:
	docker build -t haveibeenpwned .

build-dev:
	docker build -t haveibeenpwned:dev .

push:
	docker tag haveibeenpwned $(DOCKERUSER)/haveibeenpwned:$(VERSION)
	docker push $(DOCKERUSER)/haveibeenpwned:$(VERSION)
	docker tag haveibeenpwned $(DOCKERUSER)/haveibeenpwned:latest
	docker push $(DOCKERUSER)/haveibeenpwned:latest

deploy:
	kubectl apply -f secrets.yaml
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml

delete:
	kubectl delete deploy/haveibeenpwned
	kubectl delete service/haveibeenpwned-svc
	kubectl delete secret/hibp-api-key