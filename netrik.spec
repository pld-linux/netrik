# $Revision: 1.19.2.1 $,11 $Date: 2003-07-11 12:02:07 $
Summary:	The ANTRIK Internet Viewer
Summary(pl):	Przeglądarka internetowa ANTRIK
Name:		netrik
Version:	1.2.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-gzip_fallback.patch
Patch1:		%{name}-curses.patch
PAtch2:		%{name}-ac_fixes.patch
URL:		http://netrik.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
