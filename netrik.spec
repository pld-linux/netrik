Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przeglądarka internetowa ANTRIK
Name:		netrik
Version:	1.15.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/netrik/%{name}-%{version}.tar.gz
# Source0-md5:	5d4b566cb35400284130a777aec33c6d
URL:		http://netrik.sourceforge.net/
BuildRequires:	automake
BuildRequires:	readline-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet
Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl
Netrik to przeglądarka/eksplorator/nawigator/cokolwiek ANTRIKA.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
CPPFLAGS="-I/usr/include/ncurses"
%configure
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
