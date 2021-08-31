# Project Title

## Table of Contents
- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Model Results](#model-results)
  - [Additional Information](#additional-information)

```bash
|   ReadMe.md
|
+---assets
|       0_0.jpeg
|       1_1.jpeg
|       1_2.jpeg
|       2_2.jpeg
|
+---docs
|       index.html
|       main.html
|       search.json
|       ui.html
|
+---Fastapi
|   |   decoder.h5
|   |   Dockerfile
|   |   main.py
|   |   requirements.txt
|   |

|
+---models
|       decoder.h5
|
+---notebooks
|       requirements.txt
|       vae.ipynb
|
\---User_interface
    |   decoder.h5
    |   Dockerfile
    |   requirements.txt
    |   ui.py
    |
  
```
## Introduction
Experimentation of VAE models and simple docker deployment of a streamlit app as well as a post api
## Getting Started
To deploy FASPTPI use the dockerfile in the fastapi to generate the 

## Model Results
Here is a generated image from the CVAE by tweaking the latent variables while using the label of bag 

![Image of bag](./assets/0_0.jpeg)
![Image of bag](./assets/1_1.jpeg)
![Image of bag](./assets/1_2.jpeg)
![Image of bag](./assets/2_2.jpeg)

## Additional Information
basecode for CVAE models gotten from:
(https://github.com/nnormandin/Conditional_VAE)