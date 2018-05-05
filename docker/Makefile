SERVER_IMAGE=aws-test-server
SERVER_TAG=1.0

build-server:
	@cp ../server/server.py delivery/
	@docker build -t $(SERVER_IMAGE):$(SERVER_TAG) .

run-server:
	@docker run -d -p 5002:5002 --name awsserver --rm $(SERVER_IMAGE):$(SERVER_TAG)
