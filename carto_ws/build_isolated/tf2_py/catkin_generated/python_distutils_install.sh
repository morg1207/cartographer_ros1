#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/tortoisebot/catkin_ws/carto_ws/src/geometry2_python3/tf2_py"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/tortoisebot/catkin_ws/carto_ws/install_isolated/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/tortoisebot/catkin_ws/carto_ws/install_isolated/lib/python3/dist-packages:/home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_py/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_py" \
    "/usr/bin/python3" \
    "/home/tortoisebot/catkin_ws/carto_ws/src/geometry2_python3/tf2_py/setup.py" \
    egg_info --egg-base /home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_py \
    build --build-base "/home/tortoisebot/catkin_ws/carto_ws/build_isolated/tf2_py" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/tortoisebot/catkin_ws/carto_ws/install_isolated" --install-scripts="/home/tortoisebot/catkin_ws/carto_ws/install_isolated/bin"
