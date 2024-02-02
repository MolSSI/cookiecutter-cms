.. {{cookiecutter.repo_name}} documentation master file, created by
   sphinx-quickstart on Thu Mar 15 13:55:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.project_name}}'s documentation!
=========================================================

.. grid:: 1 1 2 2

    .. grid-item-card:: Getting Started
      :margin: 0 3 0 0
      
      Learn the basics of using {{cookiecutter.project_name}}.

      .. button-link:: ./getting_started.html
         :color: primary
         :outline:
         :expand:

         To the Getting Started Guide

      

    .. grid-item-card::  User Guide
      :margin: 0 3 0 0
      
      An in-depth guide for users.

      .. button-link:: ./user_guide.html
         :color: primary
         :outline:
         :expand:

         To the User Guide
      
      

    .. grid-item-card:: API Reference
      :margin: 0 3 0 0
      
      How to use the API of {{cookiecutter.project_name}}.

      .. button-link:: ./api.html
         :color: primary
         :outline:
         :expand:

         To the API Reference.

      

    .. grid-item-card::  Developer Guide
      :margin: 0 3 0 0
      
      How to contribute to {{cookiecutter.project_name}}.

      .. button-link:: ./developer_guide.html
         :color: primary
         :outline:
         :expand:

         To the Developer Guide


.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:

   getting_started
   user_guide
   api
   developer_guide

