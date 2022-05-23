# django-boilerplate

Save a few steps in setting up your django project.

Some features:

  - The secret cookie-signing key is automatically generated instead of
    being checked in

  - There’s a modern packager set up for frontend work

  - docker-compose setup suitable for deploying

  - django-debug-toolbar is configured

  - A sample app is included for reference, with some tests, that uses
    class-based views, and has bootstrap configured for styling

  - Media uploads are configured.

    *Note*: there are many additional issues not handled by this
    boilerplate to address for public-facing sites and/or sites that allow
    uploads from untrusted users, such as:

      - an uploaded .html file can contain js can steal cookies and
        impersonate the site in other ways, so media uploads are generally
        hosted on separate top-level domains

      - as normally set up, anyone with the URL can access the file; note
        that if you’re using a different top-level domain because you
        aren’t sure you can secure cookies, you probably don’t have auth
        cookies to work with

      - if uploads have predictable names they can be enumerated by
        attackers

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
  - 8003: tls port for nginx frontend tests

## License

See `LICENSE`, which uses the same terms as the django project.
