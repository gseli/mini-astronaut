# Mini Astronaut

## Description

This is a framework for testing with Selenium and pytest-bdd in a Docker image.

This is also the ship of a tiny astronaut.

## Requirements

You should have installed in your system the following:

- Docker

## Usage

1. Clone this repository
2. On the root of the repository, run `docker-compose up`
3. Wait for a couple of minutes while the Docker image is built

At the end of the process, you should see a message from pytest with the results of the tests.

## Running with different Browsers

Currently this is hard-coded to work with Chrome. If you wish to use either Firefox or Edge, do the following:

1. Open the `docker-compose` file
2. Localize the pytest configuration portion of the file
3. On the command option, replace where it says 'chrome' with 'firefox' or 'microsoftedge'
