%define rname splix

Summary:	CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-drivers-%{rname}
Version:	2.0.0
Release:	14
License:	GPLv2
Group:		System/Printing
URL:		http://splix.ap2c.org/
Source0:	http://downloads.sourceforge.net/splix/%{rname}-%{version}.tar.bz2
Patch0:		splix-2.0.0-ldflags.patch
Patch1:		splix-2.0.0-tools-nojbig.patch
Patch2:		splix-2.0.0-gcc44.patch
Patch3:		splix-2.0.0-gcc45.diff
BuildRequires:	cups
BuildRequires:	cups-devel
BuildRequires:	ghostscript
BuildRequires:	qt4-devel
Requires:	cups

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

This package contains CUPS drivers (PPD) for Dell, Samsung and Xerox
printers.

%prep
%setup -qn %{rname}-%{version}
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
%makeinstall_std
mkdir -p %{buildroot}%{_bindir}
install -m0755 tools/decompress %{buildroot}%{_bindir}/%{name}-decompress

%files
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%{_datadir}/cups/model/dell
%{_datadir}/cups/model/samsung
%{_datadir}/cups/model/xerox
%{_bindir}/%{name}-decompress
%{_prefix}/lib/cups/filter/pstoqpdl
%{_prefix}/lib/cups/filter/rastertoqpdl

