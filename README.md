# Colour Palette Generator

This is a simple colour palette generator built using Flask and containerised using Docker. It uses two backend services to generate the colours and name of the palette.

The full application can be built with the command:

```bash
docker-compose build
```

And run with Docker Compose:

```bash
docker-compose up -d
```

It also includes a Kubernetes configuration. You can deploy it to a cluster using:

```bash
kubectl apply -f k8s
```

## Frontend

This service displays the palette's name and colour. Simply press the `Generate Palette` button to create a new colour palette!

## Name Generator

This service generates a random name from a list of words when it receives an HTTP request to `name-generator/name`.

The name will always be at least one word long, but is usually two words long. There is also a small chance that a three-word long name will be generated!

At the moment, all words are nouns. In the future, I'd like to create a more complex generator to make more interesting names.

## Palette Generator

This service generates a random number of three-integer-long objects from 0 - 255 and returns them as a JSON object when it receives an HTTP request to `palette-generator/palette`.

These three numbers represent RGB (red, green, blue) values which are then used by the frontend service to display a random set of colours.