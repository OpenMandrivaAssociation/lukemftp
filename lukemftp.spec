%define beta beta2
%define release  %mkrel 0.%{beta}.4
%define version 1.6
%define realver %{version}%{beta}

Summary:	The enhanced ftp client
Name:		lukemftp
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Networking/File transfer
Source0:	ftp://ftp.netbsd.org/pub/NetBSD/misc/lukemftp/%{name}-%{realver}.tar.bz2
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%_tmppath/%{name}-%{version}-buildroot
Conflicts:	ftp-client-krb5
Provides:   ftp
Obsoletes:	ftp6
Provides:   ftp6

%description
The enhancements over the standard ftp client include:
- command-line fetching of URLS, including support for:
     - http proxies
     - authentication
- dynamic progress bar
- IPv6 support
- paging of local and remote files, and of directory listings
- socks4/socks5 support
- TIS Firewall Toolkit gate ftp proxy support
- transfer-rate throttling
- other

%prep
%setup -q -n %{name}-%{realver}

%build
autoconf
%configure \
	--enable-editcomplete --enable-ipv6
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

#%{__make} install \
#	prefix=$RPM_BUILD_ROOT \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir}/man1
%makeinstall
install src/ftp.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README NEWS

rm -rf $RPM_BUILD_ROOT%{_mandir}/cat1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ftp.1*

