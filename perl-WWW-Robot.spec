%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Robot perl module
Summary(pl):	Modu� perla WWW-Robot
Name:		perl-WWW-Robot
Version:	0.022
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Robot-%{version}.tar.gz
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
WWW-Robot - konfigurowalny mechanizm analizuj�cy zasoby sieciowe (dla
robot�w sieciowych i innych sieciowych agent�w).

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
