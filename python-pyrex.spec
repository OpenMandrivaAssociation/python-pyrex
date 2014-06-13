%define module	pyrex

Summary:	Language for Writing Python Extension Modules
Name:		python-%{module}
Version:	0.9.9
Release:	11
License:	Apache License
Group:		Development/Python
Url:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
Source0:	Pyrex-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	emacs
BuildRequires:	pkgconfig(python)
Obsoletes:	pyrex
Requires:	python

%description
Pyrex lets you write code that mixes Python and C data types any way you want,
and compiles it into a C extension for Python. 

%prep
%setup -qn Pyrex-%{version} 

%install
find -name .*hg* | xargs rm -rf

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
pushd Tools
dos2unix pyrex-mode.el
emacs -batch -f batch-byte-compile pyrex-mode.el
install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
install -m 644 pyrex-mode.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d
popd

#%check
#cd Demos
#PYTHONPATH=`pwd`/../build/lib make test clean

%files -f FILELIST
%doc *.txt Demos Doc
%{_sysconfdir}/emacs/site-start.d/*.el*

