#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python PE parsing module
Summary(pl.UTF-8):	Moduł Pythona do analizy PE
Name:		python-pefile
Version:	2019.4.18
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pefile/
Source0:	https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz
# Source0-md5:	e328272bc82ddc3170316250e37027ad
URL:		https://pypi.org/project/pefile/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pefile is a multi-platform Python module to parse and work with
Portable Executable (aka PE) files. Most of the information contained
in the PE headers is accessible as well as all sections' details and
their data.

%description -l pl.UTF-8
pefile to wieloplatformowy moduł Pythona do analizy i pracy z plikami
Portable Executable (PE). Umożliwia dostęp do większości informacji
zawartych w nagłówkach PE, a także szczegółów oraz danych wszystkich
sekcji.

%package -n python3-pefile
Summary:	Python PE parsing module
Summary(pl.UTF-8):	Moduł Pythona do analizy PE
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pefile
pefile is a multi-platform Python module to parse and work with
Portable Executable (aka PE) files. Most of the information contained
in the PE headers is accessible as well as all sections' details and
their data.

%description -n python3-pefile -l pl.UTF-8
pefile to wieloplatformowy moduł Pythona do analizy i pracy z plikami
Portable Executable (PE). Umożliwia dostęp do większości informacji
zawartych w nagłówkach PE, a także szczegółów oraz danych wszystkich
sekcji.

%prep
%setup -q -n pefile-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_sitescriptdir}/ordlookup
%{py_sitescriptdir}/pefile.py[co]
%{py_sitescriptdir}/peutils.py[co]
%{py_sitescriptdir}/pefile-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pefile
%defattr(644,root,root,755)
%doc LICENSE README
%{py3_sitescriptdir}/ordlookup
%{py3_sitescriptdir}/pefile.py
%{py3_sitescriptdir}/peutils.py
%{py3_sitescriptdir}/__pycache__/pefile.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/peutils.cpython-*.py[co]
%{py3_sitescriptdir}/pefile-%{version}-py*.egg-info
%endif
