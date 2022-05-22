# django-boilerplate

Save a few steps in setting up your django project.

Some features:

  - The secret cookie-signing key is automatically generated instead of
    being checked in

  - There’s a modern packager set up for frontend work, including using
    bootstrap for styling

  - docker-compose setup suitable for deploying

  - django-debug-toolbar is configured

  - A sample app is included for reference, with some tests, and it uses
    class-based views

## Usage

Clone the repo and start coding. You can remove, copy, or rename the
`polls` app; it’s there as a helpful starting point.

To get the frontend serving locally:

    cd frontend && yarn && yarn vite

## Deployment

As a deployment mechanism, this project supports running a single server
instance in production, using docker-compose from a git checkout on linux.

The expected setup is a machine somewhere (a vm on digitalocean, an pc
you’re using as a server in your home or office) running nginx, already
configured with https and everything, that serves up a number of backend
sites by proxying.

You *should* be able to do:

    docker-compose up --build

to get the uwsgi listener running, and then configure nginx somewhat like
the included `website.nginx.conf`.

### Ports used

  - 8000: default runserver port in dev mode
  - 8001: uwsgi listener for docker container
  - 8002: nginx frontend when doing dev/testing on uwsgi setup; start with
    `docker-compose --profile=nginx up nginx`

## License

See `LICENSE`, which uses the same terms as the django project.
