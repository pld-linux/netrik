Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przegl±darka internetowa ANTRIK
Name:		netrik
Version:	1.12.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b88ec1cab044c13643a2c44a982ffc9a
URL:		http://netrik.sourceforge.net/
BuildRequires:	readline-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet
Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl
Netrik to przegl±darka/eksplorator/nawigator/cokolwiek ANTRIKA.

%prep
%setup -q

%build
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
