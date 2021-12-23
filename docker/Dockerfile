FROM python:slim-bullseye

ARG USERNAME=aoc
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt install -y git \
    && pip install --upgrade pip

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME
# Add user's home route to path
ENV PATH="/home/$USERNAME/.local/bin:${PATH}"

WORKDIR /advent_of_code

# Copy package references and install them
COPY --chown=$USER_UID:$USER_GID requirements.txt requirements.txt
COPY --chown=$USER_UID:$USER_GID token /home/$USERNAME/.config/aocd/token

RUN pip install -r requirements.txt

##Ejecutamos la bash por defecto##
CMD ["/bin/bash"]%