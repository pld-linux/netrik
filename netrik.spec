# $Revision: 1.7 $,11 $Date: 2002-05-20 06:23:43 $
Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przegl±darka internetowa ANTRIK
Name:		netrik
Version:	0.12
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://netrik.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet
Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl
Netrik to przegl±darka/eksplorator/nawigator/cokolwiek ANTRIK.

%prep
%setup -q 

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
automake -a -c -f
autoheader
autoconf

%configure

%{__make} \
        DEBUG="%{rpmcflags}" \
        CC=%{__cc} \
	INCLUDES="-I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netrik $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README AUTHORS ChangeLog NEWS  doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html doc/*.gz
%attr(755,root,root) %{_bindir}/*
