FROM gitpod/workspace-full

## Avoid using 'root', as it's bad for your dev environments!
USER gitpod

## Just say 'Hello, world!' because our base dependency, Python 3.2.x are okay.
RUN echo "[INFO] Hello, world! Gitpod image for Syper-PyOS completed."