%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Robot perl module
Summary(pl):	Modu³ perla WWW-Robot
Name:		perl-WWW-Robot
Version:	0.021
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Robot-%{version}.tar.gz
Patch0:		perl-WWW-Robot-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-Robot
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
