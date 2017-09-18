=====================
terminal-image-viewer
=====================

Simple python script to view images in terminal.

.. image:: sample.gif

Usage
=====

Copy the main script and color_table in to a directory in your $PATH.
Name the script as imagepro for convenience.

::

    $ imagepro [image-name] [crop-size]

Where image-name is the name of the image you want to open in current
directory.  Crop size is the size of the squares the script partitions the
image to print. If ommited default value is 1. Lower the crop size higher the
details.

Example::

    $ imagepro image.jpg 50

Dependencies
============

The scripts requries python image library (pillow) to work. You can install
the library with::

    # pip install pillow

Or with your distro's default package manager, for example::

    # pacman -Syu python-pillow
