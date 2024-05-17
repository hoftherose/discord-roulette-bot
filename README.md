# Discord Roulette Bot

## Description
Discord bot for playing russian roulette and variations of the game. Features will include game settings, possible powerups and team based games.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Getting started

## Local Installation
There are multiple components to the project which each needs their own way of running. The easiest is to use docker and docker-compose `docker compose up -d`. Once all of the containers are up and running you can open `player.localhost/docs` on the browser or any other container path to start using the application.

### Running locally
If you instead want to install all of the tooling locally, you can use the makefile to see what commands need to be run. In this project we use poetry for python dependencies. You can use Make commands to install the required dependencies, for development `install-dev`. If you wish to contribute, also run `install-lint,install-test,install-hooks` to place the correct githook checks and their dependencies into your local machine.

### Running on kubernetes
To run on kubernetes you need to setup 3 items: the enable pulling images, generate configmaps and secrets and finally setup the deployment. In order to pull images you need to create the dockerconfigfile secret "registry-credentials". You can use the following command to generate this using gitlab deployment tokens. Make sure it is created in the correct namespace

`kubectl...`
`kubectl apply -f k8s/dev/config.yml`

Once you have the pull secrets you need to create the secrets and fill in the configmap. Secrets file values are not stored in git so it must be generated similar to before or filled in manually. The configmap values should be the same as the ones presented in k8s/dev/config.yml

Once you have both of the previous, run `kubectl apply -f k8s/dev/deployment.yml` and watch over the logs to make sure everything was built correctly.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## License
