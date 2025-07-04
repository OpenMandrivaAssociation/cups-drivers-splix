%define rname splix

Summary:	CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-drivers-%{rname}
Version:	2.0.0
Release:	22
License:	GPLv2
Group:		System/Printing
URL:		https://splix.ap2c.org/
Source0:	http://downloads.sourceforge.net/splix/%{rname}-%{version}.tar.bz2
Patch0:		splix-2.0.0-ldflags.patch
Patch1:		splix-2.0.0-tools-nojbig.patch
Patch2:		splix-2.0.0-gcc44.patch
Patch3:		splix-2.0.0-gcc45.diff
Patch4:		splix-2.0.0-qt6.patch
Patch5:		splix-2.0.0-compile.patch
BuildRequires:	pkgconfig(com_err)
BuildRequires:	pkgconfig(mit-krb5-gssapi)
BuildRequires:	pkgconfig(mit-krb5)
BuildRequires:	pkgconfig(krb5-gssapi)
BuildRequires:	pkgconfig(kdb)
BuildRequires:	pkgconfig(kadm-server)
BuildRequires:	pkgconfig(kadm-client)
BuildRequires:	pkgconfig(gssrpc)
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	jbig-devel
BuildRequires:	cups
BuildRequires:	cups-devel
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(Qt6Core)
Requires:	cups

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

This package contains CUPS drivers (PPD) for Dell, Samsung and Xerox
printers.

%prep
%autosetup -p1 -n %{rname}-%{version}


%build
%make_build V=1 OPTIM_CXXFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%make_build CXXFLAGS="%{optflags} $(pkg-config Qt6Core --cflags)" \
	LIBS="$(pkg-config Qt6Core --libs) %{ldflags}" -C tools

%install
%make_install
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
