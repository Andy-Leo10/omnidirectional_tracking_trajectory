# omnidirectional_tracking_trajectory

Author: Andrés Alamo 

Date: October 2023

## Descripción

Control de robot omnidireccional dentro de un edificio

![robots](https://github.com/Andy-Leo10/omnidirectional_tracking_trajectory/assets/60716487/d2564283-9cdb-4260-84b3-d3527d60c7f5)

## Uso

``` 
roslaunch neo_description mpo_500_controller.launch
roslaunch neo_description mpo_500_controller.launch world_name_global:=/home/user/catkin_ws/src/omni_pkg/src/miDepaWorld.world

cd /home/user/catkin_ws/src/omni_pkg/src
python control_seguimiento_trayectoria.py
```

