# omnidirectional_tracking_trajectory

Author: Andrés Alamo 

Date: September 2023

## Descripción

Control de robot omnidireccional dentro de un edificio

![Diseño sin título](https://github.com/Andy-Leo10/omnidirectional_tracking_trajectory/assets/60716487/847c7b85-67c1-45cb-ac8d-e80625f7dd12)


## Uso

``` 
roslaunch neo_description mpo_500_controller.launch
roslaunch neo_description mpo_500_controller.launch world_name_global:=/home/user/catkin_ws/src/omni_pkg/src/miDepaWorld.world

cd /home/user/catkin_ws/src/omni_pkg/src
python control_seguimiento_trayectoria.py
``` 
