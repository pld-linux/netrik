# $Revision: 1.4 $,11 $Date: 2002-05-05 06:46:46 $
Summary:        The ANTRIK Internet Viewer
Summary(pl):    Przegl±darka internetowa ANTRIK
Name:           netrik
Version:        0.11.1
Release:        1
License:        GPL
Group:          Applications/Networking
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:            http://netrik.sourceforge.net/
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Requires:       wget
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netrik is the ANTRIK Internet Viewer/Browser/Explorer/Navigator/whatever.

%description -l pl
Netrik to przegl±darka/eksplorator/nawigator/cokolwiek ANTRIK.

%prep
%setup -q -n %{name}

%build
%{__make} \
        DEBUG="-I/usr/include/ncurses %{rpmcflags}" \
        CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netrik $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGES doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html doc/*.gz
%attr(755,root,root) %{_bindir}/*
