execute_process(COMMAND "/home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
