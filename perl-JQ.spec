%define		pnam	JQ
Summary:	JQ - Perl binding for jq
Name:		perl-JQ
Version:	0.01
%define gitref  82a99d257482dca7c768afa32043daac175179c6
%define snap    20151117
Release:	1.%{snap}
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://github.com/spiritloose/JQ/archive/%{gitref}/%{name}.tar.gz
# Source0-md5:	b18ab8e3e41b55ee906782471d6791f9
URL:		https://github.com/spiritloose/JQ
BuildRequires:	jq-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JQ is a Perl binding for jq.

%prep
%setup -q -n %{pnam}-%{gitref}

%build
%{__perl} -I. Build.PL
%{__perl} Build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/JQ
install -d $RPM_BUILD_ROOT/%{_mandir}/man3

%{__cp} blib/arch/auto/JQ/JQ.so $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/JQ
%{__cp} blib/lib/JQ.pm $RPM_BUILD_ROOT/%{perl_vendorarch}
%{__cp} blib/libdoc/JQ.3pm $RPM_BUILD_ROOT/%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/JQ.pm
%dir %{perl_vendorarch}/auto/JQ
%attr(755,root,root) %{perl_vendorarch}/auto/JQ/JQ.so
%{_mandir}/man3/*
