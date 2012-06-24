#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Persistent
Summary:	CGI::Persistent - transparent state persistence for CGI applications
Summary(pl):	CGI::Persistent - przezroczyste zachowywanie stanu dla aplikacji CGI
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

%description -l pl
HTTP jest protoko�em bezstanowym; serwer HTTP zamyka po��czenie po
podaniu obiektu. Nie przechowuje w pami�ci szczeg��w dotycz�cych
��da� i nie wi��e nast�pnych ��da� z tym, co ju� zosta�o podane.

CGI::Persistent rozwi�zuje ten problem wprowadzaj�c trwa�e sesje CGI
przechowuj�ce dane o stanie po stronie serwera. Kiedy zaczyna si� nowa
sesja, CGI::Persistent automatycznie generuje unikalny �a�cuch
identyfikuj�cy stan i wi��e go z trwa�ym obiektem na serwerze. �a�cuch
identyfikuj�cy jest u�ywany w URL-ach lub formularzach, aby wskazywa�
na konkretn� sesj�. Atrybuty ��dania s� w spos�b przezroczysty
dodawane do powi�zanego obiektu, a dane obiektu s� przypisane do
zapytania.

CGI::Persistent wywodzi si� z CGI.pm, kt�rego metody zosta�y
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
