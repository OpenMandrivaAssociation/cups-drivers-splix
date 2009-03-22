%define rname splix

Summary:	CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-drivers-%{rname}
Version:	2.0.0
Release:	%mkrel 1
License:	GPL
Group:		System/Printing
URL:		http://splix.ap2c.org/
Source0:	http://downloads.sourceforge.net/splix/%{rname}-%{version}.tar.bz2
Patch0:		splix-2.0.0-ldflags.patch
Patch1:		splix-2.0.0-tools-nojbig.patch
Requires:	cups
BuildRequires:	cupsddk
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
