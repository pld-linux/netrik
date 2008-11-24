Summary:	The ANTRIK Internet Viewer
Summary(pl.UTF-8):	Przeglądarka internetowa ANTRIK
Name:		netrik
Version:	1.16
Release:	0.beta.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/netrik/%{name}-%{version}.tar.gz
# Source0-md5:	5cc1bbf467b8663531074958c159e9d3
Patch0:		%{name}-tinfo.patch
URL:		http://netrik.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 5.0
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet
Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl.UTF-8
Netrik to przeglądarka/eksplorator/nawigator/cokolwiek ANTRIKA.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
# CFLAGS_OLD is a workaround for getting CFLAGS before AC_INIT
%configure \
	CFLAGS_OLD="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
