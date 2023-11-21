# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include;/usr/include/eigen3;/usr/include/pcl-1.10;/usr/include/vtk-7.1;/usr/include/freetype2;/usr/include/aarch64-linux-gnu;/usr/include/ni;/usr/include/openni2".split(';') if "${prefix}/include;/usr/include;/usr/include/eigen3;/usr/include/pcl-1.10;/usr/include/vtk-7.1;/usr/include/freetype2;/usr/include/aarch64-linux-gnu;/usr/include/ni;/usr/include/openni2" != "" else []
PROJECT_CATKIN_DEPENDS = "dynamic_reconfigure;geometry_msgs;message_filters;nodelet;nodelet_topic_tools;pcl_conversions;pcl_msgs;rosbag;roscpp;sensor_msgs;std_msgs;tf;tf2;tf2_eigen;tf2_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lpcl_ros_filter;-lpcl_ros_tf;/usr/lib/aarch64-linux-gnu/libboost_thread.so;-lpthread;/usr/lib/aarch64-linux-gnu/libboost_chrono.so;/usr/lib/aarch64-linux-gnu/libboost_atomic.so;/usr/lib/aarch64-linux-gnu/libpcl_common.so;/usr/lib/aarch64-linux-gnu/libpcl_kdtree.so;/usr/lib/aarch64-linux-gnu/libpcl_octree.so;/usr/lib/aarch64-linux-gnu/libpcl_search.so;/usr/lib/aarch64-linux-gnu/libpcl_features.so;/usr/lib/aarch64-linux-gnu/libpcl_sample_consensus.so;/usr/lib/aarch64-linux-gnu/libpcl_filters.so;/usr/lib/aarch64-linux-gnu/libpcl_io.so;/usr/lib/aarch64-linux-gnu/libpcl_ml.so;/usr/lib/aarch64-linux-gnu/libpcl_segmentation.so;/usr/lib/aarch64-linux-gnu/libpcl_surface.so;/usr/lib/aarch64-linux-gnu/libboost_system.so;/usr/lib/aarch64-linux-gnu/libboost_filesystem.so;/usr/lib/aarch64-linux-gnu/libboost_date_time.so;/usr/lib/aarch64-linux-gnu/libboost_iostreams.so;/usr/lib/aarch64-linux-gnu/libboost_regex.so;/usr/lib/aarch64-linux-gnu/libqhull.so;/usr/lib/libOpenNI.so;/usr/lib/libOpenNI2.so;/usr/lib/aarch64-linux-gnu/libvtkChartsCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonColor-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtksys-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonDataModel-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonMath-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonMisc-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonSystem-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonTransforms-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonExecutionModel-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersGeneral-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonComputationalGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInfovisCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersExtraction-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersStatistics-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingFourier-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkalglib-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingContext2D-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersSources-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingFreeType-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libfreetype.so;/usr/lib/aarch64-linux-gnu/libz.so;/usr/lib/aarch64-linux-gnu/libvtkFiltersModeling-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingSources-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInteractionStyle-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInteractionWidgets-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersHybrid-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingColor-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingGeneral-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingHybrid-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOImage-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkDICOMParser-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkmetaio-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libjpeg.so;/usr/lib/aarch64-linux-gnu/libpng.so;/usr/lib/aarch64-linux-gnu/libtiff.so;/usr/lib/aarch64-linux-gnu/libvtkRenderingAnnotation-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingVolume-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOXML-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOXMLParser-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libexpat.so;/usr/lib/aarch64-linux-gnu/libvtkIOGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOLegacy-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOPLY-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingLOD-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkViewsContext2D-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkViewsCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingContextOpenGL2-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingOpenGL2-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libflann_cpp.so".split(';') if "-lpcl_ros_filter;-lpcl_ros_tf;/usr/lib/aarch64-linux-gnu/libboost_thread.so;-lpthread;/usr/lib/aarch64-linux-gnu/libboost_chrono.so;/usr/lib/aarch64-linux-gnu/libboost_atomic.so;/usr/lib/aarch64-linux-gnu/libpcl_common.so;/usr/lib/aarch64-linux-gnu/libpcl_kdtree.so;/usr/lib/aarch64-linux-gnu/libpcl_octree.so;/usr/lib/aarch64-linux-gnu/libpcl_search.so;/usr/lib/aarch64-linux-gnu/libpcl_features.so;/usr/lib/aarch64-linux-gnu/libpcl_sample_consensus.so;/usr/lib/aarch64-linux-gnu/libpcl_filters.so;/usr/lib/aarch64-linux-gnu/libpcl_io.so;/usr/lib/aarch64-linux-gnu/libpcl_ml.so;/usr/lib/aarch64-linux-gnu/libpcl_segmentation.so;/usr/lib/aarch64-linux-gnu/libpcl_surface.so;/usr/lib/aarch64-linux-gnu/libboost_system.so;/usr/lib/aarch64-linux-gnu/libboost_filesystem.so;/usr/lib/aarch64-linux-gnu/libboost_date_time.so;/usr/lib/aarch64-linux-gnu/libboost_iostreams.so;/usr/lib/aarch64-linux-gnu/libboost_regex.so;/usr/lib/aarch64-linux-gnu/libqhull.so;/usr/lib/libOpenNI.so;/usr/lib/libOpenNI2.so;/usr/lib/aarch64-linux-gnu/libvtkChartsCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonColor-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtksys-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonDataModel-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonMath-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonMisc-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonSystem-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonTransforms-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonExecutionModel-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersGeneral-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkCommonComputationalGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInfovisCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersExtraction-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersStatistics-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingFourier-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkalglib-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingContext2D-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersSources-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingFreeType-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libfreetype.so;/usr/lib/aarch64-linux-gnu/libz.so;/usr/lib/aarch64-linux-gnu/libvtkFiltersModeling-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingSources-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInteractionStyle-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkInteractionWidgets-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkFiltersHybrid-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingColor-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingGeneral-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkImagingHybrid-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOImage-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkDICOMParser-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkmetaio-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libjpeg.so;/usr/lib/aarch64-linux-gnu/libpng.so;/usr/lib/aarch64-linux-gnu/libtiff.so;/usr/lib/aarch64-linux-gnu/libvtkRenderingAnnotation-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingVolume-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOXML-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOXMLParser-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libexpat.so;/usr/lib/aarch64-linux-gnu/libvtkIOGeometry-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOLegacy-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkIOPLY-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingLOD-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkViewsContext2D-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkViewsCore-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingContextOpenGL2-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libvtkRenderingOpenGL2-7.1.so.7.1p.1;/usr/lib/aarch64-linux-gnu/libflann_cpp.so" != "" else []
PROJECT_NAME = "pcl_ros"
PROJECT_SPACE_DIR = "/home/tortoisebot/catkin_ws/carto_ws/install_isolated"
PROJECT_VERSION = "1.7.5"
