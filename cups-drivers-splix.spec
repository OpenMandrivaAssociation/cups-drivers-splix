%define rname splix

Summary:	CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-drivers-%{rname}
Version:	2.0.0
Release:	%mkrel 6
License:	GPL
Group:		System/Printing
URL:		http://splix.ap2c.org/
Source0:	http://downloads.sourceforge.net/splix/%{rname}-%{version}.tar.bz2
Patch0:		splix-2.0.0-ldflags.patch
Patch1:		splix-2.0.0-tools-nojbig.patch
Patch2:		splix-2.0.0-gcc44.patch
Patch3:		splix-2.0.0-gcc45.diff
Requires:	cups
BuildRequires:	cups
BuildRequires:	cups-devel
BuildRequires:	libqt4-devel
BuildRequires:	ghostscript
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

This package contains CUPS drivers (PPD) for Dell, Samsung and Xerox
printers.

%prep
%setup -q -n %{rname}-%{version}
%patch0 -p1 -b .ldflags
%patch1 -p1 -b .tools-nojbig
%patch2 -p1 -b .gcc44
%patch3 -p0 -b .gcc45

%build
# note: build using DISABLE_JBIG=1 because of possible patent issue
%make V=1 OPTIM_CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" DISABLE_JBIG=1
%make CXXFLAGS="%{optflags} `pkg-config QtCore --cflags`" \
      LIBS="`pkg-config QtCore --libs` %{ldflags}" -C tools

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_bindir}
install -m0755 tools/decompress %{buildroot}%{_bindir}/%{name}-decompress

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%{_datadir}/cups/model/dell
%{_datadir}/cups/model/samsung
%{_datadir}/cups/model/xerox
%defattr(0755,root,root,0755)
%{_bindir}/%{name}-decompress
%{_prefix}/lib/cups/filter/pstoqpdl
%{_prefix}/lib/cups/filter/rastertoqpdl


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdv2011.0
+ Revision: 663447
- mass rebuild

* Wed Dec 01 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdv2011.0
+ Revision: 604280
- fix build
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdv2010.1
+ Revision: 518900
- fix deps
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2010.0
+ Revision: 413295
- rebuild

  + Christophe Fergeau <cfergeau@mandriva.com>
    - fix build with gcc 4.4

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.0.0-1mdv2009.1
+ Revision: 360197
- Updated to version 2.0.0
- Redid ldflags patch.
- Build with DISABLE_JBIG=1, and dont build jbgtopbm (tools-nojbig
  patch), because of possible patent issue.

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2009.1
+ Revision: 318082
- really use %%optflags
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2009.0
+ Revision: 220550
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 149157
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2008.0
+ Revision: 75337
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2008.0
+ Revision: 64157
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 62518
- Import cups-drivers-splix



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.0
- initial Mandriva package
