DC_FILE=test.yaml

start: stop
	@docker-compose -f $(DC_FILE) up -d

stop:
	@docker-compose -f $(DC_FILE) down
