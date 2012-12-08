%define module	pyrex
%define name	python-%{module}
%define version 0.9.9
%define release %mkrel 6

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-3mdv2011.0
+ Revision: 668028
- mass rebuild

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.9.9-2mdv2011.0
+ Revision: 591980
- Rebuild

* Mon Apr 12 2010 Lev Givon <lev@mandriva.org> 0.9.9-1mdv2010.1
+ Revision: 533616
- Update to 0.9.9.

* Wed Feb 24 2010 Lev Givon <lev@mandriva.org> 0.9.8.6-1mdv2010.1
+ Revision: 510610
- Update to 0.9.8.6.

* Mon Aug 10 2009 Lev Givon <lev@mandriva.org> 0.9.8.5-3mdv2010.0
+ Revision: 414281
- Disable %%check section so that the python-numeric
  dependency can be removed.

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 0.9.8.5-2mdv2009.1
+ Revision: 318471
- rebuild for new python

* Thu Aug 28 2008 Lev Givon <lev@mandriva.org> 0.9.8.5-1mdv2009.0
+ Revision: 276759
- Update to 0.9.8.5.

* Mon Aug 04 2008 Lev Givon <lev@mandriva.org> 0.9.8.4-2mdv2009.0
+ Revision: 263297
- Make emacs mode available automatically via /etc/emacs/site-start.d.

* Wed Jun 11 2008 Lev Givon <lev@mandriva.org> 0.9.8.4-1mdv2009.0
+ Revision: 217991
- Update to 0.9.8.4.
- Update to 0.9.8.3.

* Wed May 21 2008 Lev Givon <lev@mandriva.org> 0.9.8.2-1mdv2009.0
+ Revision: 209884
- Update to 0.9.8.2.

* Thu May 15 2008 Lev Givon <lev@mandriva.org> 0.9.8-1mdv2009.0
+ Revision: 207584
- Update to 0.9.8.

* Wed May 14 2008 Lev Givon <lev@mandriva.org> 0.9.7.2-1mdv2009.0
+ Revision: 206956
- Update to 0.9.7.2.

* Tue May 13 2008 Lev Givon <lev@mandriva.org> 0.9.7.1-1mdv2009.0
+ Revision: 206568
- Update to 0.9.7.1.

* Fri May 09 2008 Lev Givon <lev@mandriva.org> 0.9.7-1mdv2009.0
+ Revision: 204960
- Update to 0.9.7.
  Make package noarch.

* Mon Jan 07 2008 Lev Givon <lev@mandriva.org> 0.9.6.4-1mdv2008.1
+ Revision: 146250
- Update to 0.9.6.4.
  Remove defunct patch.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Götz Waschk <waschk@mandriva.org> 0.9.5.1a-1mdv2008.0
+ Revision: 18216
- fix buildrequires
- new version
- drop python2.5 patch
- patch to remove a symbol for compatibility with democracy
- update file list
- enable checks


* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.4.1-5mdv2007.0
+ Revision: 96772
- rename package

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.9.4.1-4mdv2007.1
+ Revision: 88106
- Import pyrex

