This project was made for the sp 2024 CSU CHICO PHYS312 Computational Physics final with the help of Dr. Nelson. 

main.py handles all simulations and creates the animation. 

Selecting initial and boundary conditions requires commenting out certain lines of code. They are labeled accordingly. 
If the animation is acting funny, try adjusting the spatial and temporal resolution at the top of the file.

This program mainly handles square boundary conditions, though I did experiment with funky BC's like triangle. 
Initial conditions include delta function in center of membrane, normal mode excitation, uniform displacement. 

The simulation is created using the [central difference method](https://en.wikipedia.org/wiki/Finite_difference) of appoximating partial derivatives.  
