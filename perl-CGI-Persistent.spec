#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Persistent
Summary:	CGI::Persistent - transparent state persistence for CGI applications
Summary(pl.UTF-8):   CGI::Persistent - przezroczyste zachowywanie stanu dla aplikacji CGI
Name:		perl-CGI-Persistent
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0669a0720c8c0992cb0ccf43622311ca
BuildRequires:	perl-CGI
BuildRequires:	perl-Persistence-Object-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP is a stateless protocol; a HTTP server closes connection after
serving an object. It retains no memory of the request details and
doesn't relate subsequent requests with what it has already served.

CGI::Persistent solves this problem by introducing persistent CGI
sessions that store their state data on the server side. When a new
session starts, CGI::Persistent automatically generates a unique state
identification string and associates it with a persistent object on
the server. The identification string is used in URLs or forms to
refer to the particular session. Request attributes are transparently
committed to the associated object and the object data is bound to the
query.

CGI::Persistent is derived from CGI.pm. CGI.pm methods have been
overridden as appropriate. Very few new methods have been added.

%description -l pl.UTF-8
HTTP jest protokołem bezstanowym; serwer HTTP zamyka połączenie po
podaniu obiektu. Nie przechowuje w pamięci szczegółów dotyczących
żądań i nie wiąże następnych żądań z tym, co już zostało podane.

CGI::Persistent rozwiązuje ten problem wprowadzając trwałe sesje CGI
przechowujące dane o stanie po stronie serwera. Kiedy zaczyna się nowa
sesja, CGI::Persistent automatycznie generuje unikalny łańcuch
identyfikujący stan i wiąże go z trwałym obiektem na serwerze. Łańcuch
identyfikujący jest używany w URL-ach lub formularzach, aby wskazywał
na konkretną sesję. Atrybuty żądania są w sposób przezroczysty
dodawane do powiązanego obiektu, a dane obiektu są przypisane do
zapytania.

CGI::Persistent wywodzi się z CGI.pm, którego metody zostały
odpowiednio przykryte. Dodano tylko kilka nowych metod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/CGI/Persistent.pm
%{_mandir}/man3/*
