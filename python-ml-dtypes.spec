# scikit-build-core's Release wheel has no debug info, so find-debuginfo
# writes an empty debugsource manifest and rpm aborts.
%global _empty_manifest_terminate_build 0

Name:		python-ml-dtypes
Version:	0.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/ml-dtypes/ml_dtypes-%{version}.tar.gz
Summary:	NumPy dtype extensions for machine learning
URL:		https://pypi.org/project/ml-dtypes/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(scikit-build-core)

%build -p
export SKBUILD_CMAKE_BUILD_TYPE=RelWithDebInfo

%description
Stand-alone NumPy dtype extensions used by machine learning libraries,
including 8-bit floats and low-precision integers.

%files
%{py_platsitedir}/ml_dtypes
%{py_platsitedir}/ml_dtypes-%{version}.dist-info
