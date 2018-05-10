include Makefile.inc

SERVER_IMAGE=aws-test-server
SERVER_TAG=1.0
AWS_TARGET=$(AWS_ECR)/myfirstref:$(SERVER_TAG)
CMD_REPOLOGIN := "eval $$\( aws ecr get-login --no-include-email \)"

build-server:
	@cp ../server/server.py delivery/
	@docker build -t $(SERVER_IMAGE):$(SERVER_TAG) .
	@docker tag $(SERVER_IMAGE):$(SERVER_TAG) $(AWS_TARGET)

run-server:
	@docker run -d -p 5002:5002 --name awsserver --rm $(SERVER_IMAGE):$(SERVER_TAG)

_aws-login:
	@eval $(CMD_REPOLOGIN)

 
aws-publish: _aws-login
	@docker push $(AWS_TARGET) 

