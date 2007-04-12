%define module	pyrex
%define name	python-%{module}
%define version 0.9.4.1
%define release %mkrel 5

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Language for Writing Python Extension Modules
Source:     http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-%{version}.tar.bz2 
Patch:      pyrex-python-2.5.patch
URL:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
License:	Public Domain
Group:		Development/Python
Obsoletes:      pyrex
BuildRequires:	python-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Pyrex lets you write code that mixes Python and C data types any way you want,
and compiles it into a C extension for Python. 

%prep
%setup -q -n Pyrex-%{version} 
%patch

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
install -m 644 Tools/pyrex-mode.el -D %{buildroot}%{_datadir}/emacs/site-lisp/pyrex-mode.el

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt Demos Doc
%_bindir/pyrexc
%dir %py_puresitedir/Pyrex
%py_puresitedir/Pyrex/*.py*
%py_puresitedir/Pyrex/Compiler/*
%py_puresitedir/Pyrex/Distutils/*
%py_puresitedir/Pyrex/Mac/*
%py_puresitedir/Pyrex/Plex/*
%if %mdkversion > 200700
%py_puresitedir/Pyrex*.egg-info
%endif
%_datadir/emacs/site-lisp/pyrex-mode.el


