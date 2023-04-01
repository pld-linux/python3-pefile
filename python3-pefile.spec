Summary:	Python PE parsing module
Summary(pl.UTF-8):	Moduł Pythona do analizy PE
Name:		python3-pefile
Version:	2023.2.7
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pefile/
Source0:	https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz
# Source0-md5:	fa0eba7c91f4e696771ddbfacdca25e4
URL:		https://pypi.org/project/pefile/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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

%prep
%setup -q -n pefile-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py3_sitescriptdir}/ordlookup
%{py3_sitescriptdir}/pefile.py
%{py3_sitescriptdir}/peutils.py
%{py3_sitescriptdir}/__pycache__/pefile.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/peutils.cpython-*.py[co]
%{py3_sitescriptdir}/pefile-%{version}-py*.egg-info
