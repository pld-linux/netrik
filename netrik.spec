# $Revision: 1.18 $,11 $Date: 2003-01-21 08:32:17 $
Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przegl±darka internetowa ANTRIK
Name:		netrik
Version:	1.2.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-curses.patch
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
Netrik to przegl±darka/eksplorator/nawigator/cokolwiek ANTRIK.

%prep
%setup -q 
#%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}
