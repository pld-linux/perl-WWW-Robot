%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Robot
Summary:	WWW::Robot Perl module - configurable web traversal engine
Summary(pl):	Modu³ perla WWW::Robot - konfigurowlny mechanizm do analizy zasobów WWW
Name:		perl-WWW-Robot
Version:	0.023
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d26e7580b75fd7f12dce273755ff635e
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
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

%description -l pl
Modu³ Perla WWW::Robot zawiera konfigurowalny mechanizm analizuj±cy
zasoby sieciowe, przeznaczony dla robotów i innych agentów sieciowych.
Po podaniu strony pocz±tkowej (w postaci URLa) Robot pobierze
zawarto¶æ danej strony oraz wydzieli z niej wszystkie odno¶niki,
dodaj±c je do listy URLi, które bêd± odwiedzane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(use LWP::RobotUA)( 1.171)(.*)$/$1 1.18$3/' lib/WWW/*.pm
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog examples/poacher
%{perl_sitelib}/WWW/Robot.pm
%{_mandir}/man3/*
