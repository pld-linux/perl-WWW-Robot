%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Robot
Summary:	WWW::Robot Perl module - configurable web traversal engine
Summary(pl.UTF-8):	Moduł Perla WWW::Robot - konfigurowlny mechanizm do analizy zasobów WWW
Name:		perl-WWW-Robot
Version:	0.025
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0deb04563e80c1b576ee0b3fdd86f21b
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
Obsoletes:	perl-Robot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The WWW::Robot Perl module implements a configurable web traversal
engine, for a robot or other web agent. Given an initial web page
(URL), the Robot will get the contents of that page, and extract all
links on the page, adding them to a list of URLs to visit.

%description -l pl.UTF-8
Moduł Perla WWW::Robot zawiera konfigurowalny mechanizm analizujący
zasoby sieciowe, przeznaczony dla robotów i innych agentów sieciowych.
Po podaniu strony początkowej (w postaci URLa) Robot pobierze
zawartość danej strony oraz wydzieli z niej wszystkie odnośniki,
dodając je do listy URLi, które będą odwiedzane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(use LWP::RobotUA)( 1.171)(.*)$/$1 1.18$3/' lib/WWW/*.pm
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog examples/poacher
%{perl_vendorlib}/WWW/Robot.pm
%{_mandir}/man3/*
