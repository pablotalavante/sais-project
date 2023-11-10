# sais-project
Small project developed in the Swiss AI Safety Camp 2023

In this experimental project I attempt to find the IOI circuit heads by getting the gradients of the examples used in the IOI paper, taking the cost function between the correct label 
(`_Mary`) and the incorrect label (`_John`) for that specific function (and viceversa).

The hypothesis is that the the gradients will try to correct the heads involved in that specific function and thus the absolute values of the gradient will be bigger in the heads 
involved. If succesful this might give us some insights on where to look when looking for circuits for specific functions.

2023

