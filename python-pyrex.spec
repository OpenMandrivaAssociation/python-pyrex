%define module	pyrex
%define name	python-%{module}
%define version 0.9.9
%define release %mkrel 3

Summary: 	Language for Writing Python Extension Modules
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source:     	Pyrex-%{version}.tar.gz
URL:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
License:	Apache License
Group:		Development/Python
Obsoletes:      pyrex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python
BuildRequires:	python-devel
BuildRequires:	dos2unix, emacs
BuildArch:	noarch

%description
Pyrex lets you write code that mixes Python and C data types any way you want,
and compiles it into a C extension for Python. 

%prep
%setup -q -n Pyrex-%{version} 

%install
%__rm -rf %{buildroot}
find -name .*hg* | xargs rm -rf

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
pushd Tools
dos2unix pyrex-mode.el
emacs -batch -f batch-byte-compile pyrex-mode.el
%__install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
%__install -m 644 pyrex-mode.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d
popd

#%check
#cd Demos
#PYTHONPATH=`pwd`/../build/lib make test clean

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt Demos Doc
%{_sysconfdir}/emacs/site-start.d/*.el*
