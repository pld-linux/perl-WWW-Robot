%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Robot
Summary:	WWW::Robot perl module
Summary(pl):	Modu³ perla WWW::Robot
Name:		perl-WWW-Robot
Version:	0.023
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
Obsoletes:	perl-Robot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Robot - configurable web traversal engine (for web robots &
agents).

%description -l pl
WWW::Robot - konfigurowalny mechanizm analizuj±cy zasoby sieciowe (dla
robotów sieciowych i innych sieciowych agentów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog examples/poacher
%{perl_vendorlib}/WWW/Robot.pm
%{_mandir}/man3/*
