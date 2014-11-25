Name:           ros-hydro-ndt-mcl
Version:        1.0.23
Release:        0%{?dist}
Summary:        ROS ndt_mcl package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ndt_mcl
Source0:        %{name}-%{version}.tar.gz

Requires:       freeglut-devel
Requires:       libXmu-devel
Requires:       mrpt-devel
Requires:       pcl-devel
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-filters
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-ndt-map
Requires:       ros-hydro-ndt-registration
Requires:       ros-hydro-ndt-visualisation
Requires:       ros-hydro-rosbag
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  freeglut-devel
BuildRequires:  libXmu-devel
BuildRequires:  mrpt-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-filters
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-ndt-map
BuildRequires:  ros-hydro-ndt-registration
BuildRequires:  ros-hydro-ndt-visualisation
BuildRequires:  ros-hydro-rosbag
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs

%description
ndt_mcl

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Nov 25 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.23-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Jari Saarinen <jari.p.saarinen@gmail.com> - 1.0.22-0
- Autogenerated by Bloom

