%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	WWW-Robot perl module
Summary(pl):	Modu³ perla WWW-Robot
Name:		perl-WWW-Robot
Version:	0.019
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Robot-%{version}.tar.gz
Patch:		perl-WWW-Robot-paths.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-libwww
Requires:	perl-HTML-Tree
Requires:	perl-HTML-Parser
Obsoletes:	perl-Robot
BuildRoot:	/tmp/%{name}-%{version}-root

%description
WWW-Robot - configurable web traversal engine (for web robots & agents).

%description -l pl
WWW-Robot - konfigurowalny mechanizm analizuj±cy zasoby sieciowe (dla robotów
sieciowych i innych sieciowych agentów).

%prep
%setup -q -n WWW-Robot-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/WWW/Robot
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz examples/poacher

%{perl_sitelib}/WWW/Robot.pm
%{perl_sitearch}/auto/WWW/Robot

%{_mandir}/man3/*
