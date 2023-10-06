# omnidirectional_tracking_trajectory

Author: Andrés Alamo 

Date: October 2023

## Descripción

Control de robot omnidireccional dentro de un edificio

![Diseño sin título](https://github.com/Andy-Leo10/omnidirectional_tracking_trajectory/assets/60716487/847c7b85-67c1-45cb-ac8d-e80625f7dd12)

![depa](https://github.com/Andy-Leo10/omnidirectional_tracking_trajectory/assets/60716487/4389b250-c541-4cc0-8214-b4ad16d931f3)


## Uso

``` 
roslaunch neo_description mpo_500_controller.launch
roslaunch neo_description mpo_500_controller.launch world_name_global:=/home/user/catkin_ws/src/omni_pkg/src/miDepaWorld.world

cd /home/user/catkin_ws/src/omni_pkg/src
python control_seguimiento_trayectoria.py
```

![goEscaleras(1)](https://github.com/Andy-Leo10/omnidirectional_tracking_trajectory/assets/60716487/8ba6ddb6-1080-4c10-9c90-7f63370ea45d)
