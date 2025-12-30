Name:		python-ml-dtypes
Version:	0.5.3
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/m/ml-dtypes/ml_dtypes-%{version}.tar.gz
Summary:	ml_dtypes is a stand-alone implementation of several NumPy dtype extensions used in machine learning.
URL:		https://pypi.org/project/ml-dtypes/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	pkgconfig(python3)

%description
ml_dtypes is a stand-alone implementation of several NumPy dtype extensions used in machine learning.

%files
%{py_platsitedir}/ml_dtypes
%{py_platsitedir}/ml_dtypes-%{version}.dist-info
