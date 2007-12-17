%define rname splix

Summary:	CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-drivers-%{rname}
Version:	1.0.1
Release:	%mkrel 3
License:	GPL
Group:		System/Printing
URL:		http://splix.ap2c.org/
Source0:	http://downloads.sourceforge.net/splix/%{rname}-%{version}.tar.bz2
Requires:	cups
BuildRequires:	cupsddk
BuildRequires:	cups-devel
BuildRequires:	ghostscript
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

This package contains CUPS drivers (PPD) for the following printers:

 o Samsung CLP-300
 o Samsung CLP-500
 o Samsung CLP-510
 o Samsung CLP-600
 o Samsung ML-1510
 o Samsung ML-1520
 o Samsung ML-1610
 o Samsung ML-1710
 o Samsung ML-1740
 o Samsung ML-1750
 o Samsung ML-2010
 o Samsung ML-2150
 o Samsung ML-2250
 o Samsung ML-2550
 o Xerox Phaser 6100

%prep

%setup -q -n %{rname}-%{version}

%build

%make
%make -C src pbmtospl2
%make -C tools

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/cups
install -d %{buildroot}%{_prefix}/lib/cups/filter
install -d %{buildroot}%{_datadir}/cups/model/%{name}

install -m0755 src/pbmtospl2 %{buildroot}%{_bindir}/%{name}-pbmtospl2
install -m0755 tools/decompress %{buildroot}%{_bindir}/%{name}-decompress
install -m0755 src/rastertospl2 %{buildroot}%{_prefix}/lib/cups/filter/rastertospl2
install -m0644 ppd/*.ppd* %{buildroot}%{_datadir}/cups/model/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%attr(0755,root,root) %{_bindir}/%{name}-pbmtospl2
%attr(0755,root,root) %{_bindir}/%{name}-decompress
%attr(0755,root,root) %{_prefix}/lib/cups/filter/rastertospl2
%attr(0755,root,root) %dir %{_datadir}/cups/model/%{name}
%attr(0644,root,root) %{_datadir}/cups/model/%{name}/*.ppd*
