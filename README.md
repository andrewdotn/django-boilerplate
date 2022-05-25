# django-boilerplate

Save a few steps in setting up your django project.

Some features:

  - The secret cookie-signing key is automatically generated instead of
    being checked in

  - There’s a modern packager set up for frontend work

  - docker-compose setup suitable for deploying behind nginx

  - django-debug-toolbar is configured

  - A sample app is included for reference, with some tests, that uses
    class-based views, and has bootstrap configured for styling

  - Media uploads are configured.

    *Note*: there are many additional issues, not handled by this
    boilerplate, that need to be addressed for public-facing sites and/or
    sites that allow uploads from untrusted users, such as:

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

The expected setup is a machine somewhere (like a vm on a laptop, or on
digitalocean, or a pc you’re using as a server in your home or office)
running nginx, already configured with https and everything, that serves up
a number of backend sites by proxying.

You *should* be able to do:

    docker-compose up --build

to get the uwsgi listener running, and then configure nginx somewhat like
the included `website.nginx.conf`.

Make sure that you edit `ALLOWED_HOSTS` in `website/prod_settings.py` or
you’ll get a 400 Bad Request error when you try to view the site.

### How to access `manage.py`

Use the `migrate` init container.

    docker-compose run migrate ./manage.py help

If you try to run a shell in the `website` container, the init container
will run as well, attempting migrations, which usually won’t be what you
want.

### UIDs

Root in a docker container is generally really root on the host as well,
which is a bit scary. This is noticeable on linux when a website creates
files in the `db` or `media` folders that are owned by root. (On mac,
docker-desktop hides this by (1) using mac files that are owned by the user
running docker-desktop and (2) making whatever the current linux container
is believe that it owns those files.)

What user/group should own those files created on the host by the
container?

While there a few other options available such as using filesystem ACLs,
uid mapping, and rootless docker, this repo chooses to use traditional unix
users and groups.

The following users and groups are used here:

  - A `website-build` user

    This should never make files on the host.

  - A `website-run` user

    Database and media files created by the container will be owned by this
    user.

  - A `website-data` group which allows other users on the host to
    inspect database and media files.

For the data group ID, you can use the default somewhat-randomly selected
one, 65942, or enter your own `DATA_GID` in the required places in
`docker-compose.yml`. Either way, you will probably want to create a group
entry on the host for the group ID so that `ls -l` shows the group owner:

        sudo groupadd --gid 65942 website-data
        sudo usermod -aG website-data $LOGNAME

### Ports used

  - 8000: default runserver port in dev mode
  - 8001: uwsgi listener for docker container
  - 8002: nginx frontend when doing dev/testing on uwsgi setup; start with
    `docker-compose --profile=nginx up nginx`
  - 8003: tls port for nginx frontend tests

## License

See `LICENSE`, which uses the same terms as the django project.
