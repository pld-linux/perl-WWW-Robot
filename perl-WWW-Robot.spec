%define	pdir	WWW
%define	pnam	Robot
%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Robot perl module
Summary(pl):	Modu³ perla WWW-Robot
Name:		perl-WWW-Robot
Version:	0.022
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
Obsoletes:	perl-Robot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW-Robot - configurable web traversal engine (for web robots &
agents).

%description -l pl
WWW-Robot - konfigurowalny mechanizm analizuj±cy zasoby sieciowe (dla
robotów sieciowych i innych sieciowych agentów).

%prep
%setup -q -n WWW-Robot-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/poacher
%{perl_sitelib}/WWW/Robot.pm
%{_mandir}/man3/*
