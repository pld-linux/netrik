# $Revision: 1.14 $,11 $Date: 2002-06-23 20:32:32 $
Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przeglądarka internetowa ANTRIK
Name:		netrik
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://netrik.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet
Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl
Netrik to przeglądarka/eksplorator/nawigator/cokolwiek ANTRIK.

%prep
%setup -q 

%build
rm -f missing
%{__libtoolize}
gettextize --copy --force
aclocal
%{__automake}
autoheader
%{__autoconf}

%configure

%{__make} \
        DEBUG="%{rpmcflags}" \
        CC=%{__cc} \
	INCLUDES="-I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netrik $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS  NEWS  doc/*.txt
%attr(755,root,root) %{_bindir}/*
