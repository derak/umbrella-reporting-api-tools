IMAGE=umbrella-reporting
NAME=umbrella-reporting
CMD_GET_IDENTITIES=python get-identities.py

all: clean build run

build:
	docker build -t $(IMAGE) .

get-identities-by-catagory:
	@docker run -v $$PWD:/opt $(IMAGE) $(CMD_GET_IDENTITIES)

shell:
	docker exec -it $(NAME) /bin/bash

stop:
	docker stop $(NAME)

clean:
	docker rm $(NAME)
