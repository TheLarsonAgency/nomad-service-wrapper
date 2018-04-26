# nomad-service-wrapper
A nomad integration submodule for your project.  Use this to create a
microservices API of your Python applications and libraries.

## Using this in your project

You have a few options:

1. Use this repository as a submodule in your project to integrate all of the
   services in the same way we have here.
2. Fork this project and customize it to your own liking, and use that as a
   submodule.
3. Use the files in this project ad-hoc, verbatim, or at-will within your own
   project.

## Setup

* Add your requirements to `requirements.txt`.
* Customize the provided `Dockerfile` if you've got additional things that need
  to happen.
* Integrate your app with the `runner.py` script.
* Add custom API calls to `runner.py` and `app.py`.


