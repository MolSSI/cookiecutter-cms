Warnings and Caveats from the Cookiecutter
==========================================

We encourage users to look at the parent Computational Molecular Sciences Cookiecutter as ways to template their own output
projects from the `Cookiecutter <https://github.com/audreyr/cookiecutter>`_. However, there are a few things the
parent does to make the illustration work, but should probably not be followed in your projects. These are mostly
because the parent has to simulate an output, then test the output of the cookiecutter, which is something you will
not have to do with your project... Unless you are making a Cookiecutter which makes Cookiecutters, but that is
beyond the scope of this project.

Continuous Integration (CI) Caveats
-----------------------------------

The parent Cookiecutter must emulate the the process of creating and running tests, while in its own tests. Since
Travis and AppVeyor are not intended to do this, we have to do some trickery to manually process the YAML output files
after executing the Cookiecutter. This is something you, the user of this Cookiecutter, should not have to worry about
and can instead just use Travis and AppVeyor as those programs intend.


Writing helpful documentation
-----------------------------
The primary documentation for this Cookiecutter is mostly just a copy of the main README.md file. Your docs should be
more detailed in ways the README.md cannot. The README.md file is rendered by GitHub, but will (should) not contain all
of the detailed instructions, settings, applications, benchmarking which can be elaborated on in full documentations.
