Summary:	The ANTRIK Internet Viewer
Summary(pl.UTF-8):	Przeglądarka internetowa ANTRIK
Name:		netrik
Version:	1.16.1
Release:	1
License:	GPL v3+
Group:		Applications/Networking
Source0:	http://download.sourceforge.net/netrik/%{name}-%{version}.tar.gz
# Source0-md5:	73e4603491d185b0580a8fad83518f42
Patch0:		%{name}-tinfo.patch
URL:		http://netrik.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
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
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
# CFLAGS_OLD is a workaround for getting CFLAGS before AC_INIT
%configure \
	CFLAGS_OLD="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/netrik

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README TODO doc/*.html
%attr(755,root,root) %{_bindir}/netrik
%{_mandir}/man1/netrik.1*
%{_mandir}/man5/netrikrc.5*
